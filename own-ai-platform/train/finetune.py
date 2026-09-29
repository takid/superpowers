"""LoRA fine-tune a small open model on your own data, then export to GGUF.

Data: JSONL, one example per line:  {"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]}
Run on any NVIDIA GPU: your own, or free Colab/Kaggle GPUs (see README).

  python finetune.py --data data.jsonl --base unsloth/Llama-3.2-3B-Instruct --name coventry-assistant
"""
import argparse

p = argparse.ArgumentParser()
p.add_argument("--data", required=True)
p.add_argument("--base", default="unsloth/Llama-3.2-3B-Instruct")
p.add_argument("--name", required=True, help="model name you will call from the API")
p.add_argument("--epochs", type=int, default=2)
p.add_argument("--max-len", type=int, default=2048)
p.add_argument("--out", default="out")
a = p.parse_args()

from unsloth import FastLanguageModel  # noqa: E402  (heavy import after arg parsing)
from datasets import load_dataset  # noqa: E402
from trl import SFTConfig, SFTTrainer  # noqa: E402

model, tok = FastLanguageModel.from_pretrained(a.base, max_seq_length=a.max_len, load_in_4bit=True)
model = FastLanguageModel.get_peft_model(
    model, r=16, lora_alpha=16, lora_dropout=0,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
)

ds = load_dataset("json", data_files=a.data, split="train")
ds = ds.map(lambda ex: {"text": tok.apply_chat_template(ex["messages"], tokenize=False)})

SFTTrainer(
    model=model, tokenizer=tok, train_dataset=ds,
    args=SFTConfig(
        dataset_text_field="text", max_seq_length=a.max_len, num_train_epochs=a.epochs,
        per_device_train_batch_size=2, gradient_accumulation_steps=4, learning_rate=2e-4,
        logging_steps=5, output_dir=a.out, report_to="none",
    ),
).train()

model.save_pretrained_gguf(f"{a.out}/{a.name}", tok, quantization_method="q4_k_m")
print(f"\nDone. Copy the .gguf from {a.out}/{a.name}/ into ../models/ then run:\n  make register NAME={a.name} GGUF={a.name}.gguf")
