#!/usr/bin/env python3
"""Run the same prompts through two models and print the answers side by side.

  API_KEY=sk-own-... ./scripts/compare.py llama3.2:3b my-model-v2 prompts.txt

prompts.txt: one prompt per line. Judge the answers yourself; keep the better model.
Stdlib only. Set BASE_URL if the gateway isn't on localhost:8080.
"""
import json
import os
import sys
import textwrap
import time
import urllib.request

BASE = os.environ.get("BASE_URL", "http://localhost:8080")
KEY = os.environ.get("API_KEY", "")


def ask(model, prompt):
    req = urllib.request.Request(
        f"{BASE}/v1/chat/completions",
        data=json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}]}).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {KEY}"},
    )
    t = time.time()
    with urllib.request.urlopen(req, timeout=600) as r:
        text = json.load(r)["choices"][0]["message"]["content"].strip()
    return text, time.time() - t


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    a, b, path = sys.argv[1:]
    prompts = [l.strip() for l in open(path) if l.strip()]
    for i, p in enumerate(prompts, 1):
        print(f"\n=== {i}. {p}")
        for m in (a, b):
            text, secs = ask(m, p)
            print(f"\n--- {m} ({secs:.1f}s)")
            print(textwrap.fill(text, 100, replace_whitespace=False))


if __name__ == "__main__":
    main()
