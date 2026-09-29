COMPOSE=docker compose
.PHONY: up up-gpu down pull key usage register backup test
up:        ; @test -f .env || cp .env.example .env; $(COMPOSE) up -d --build
up-gpu:    ; @test -f .env || cp .env.example .env; $(COMPOSE) -f docker-compose.yml -f docker-compose.gpu.yml up -d --build
down:      ; $(COMPOSE) down
pull:      ; $(COMPOSE) exec ollama ollama pull $(MODEL)          # make pull MODEL=llama3.2:3b
key:       ; @curl -s -X POST "localhost:8080/admin/keys?name=$(NAME)" -H "Authorization: Bearer $$(grep ^ADMIN_KEY .env | cut -d= -f2 | cut -d' ' -f1)"; echo
usage:     ; @curl -s localhost:8080/admin/usage -H "Authorization: Bearer $$(grep ^ADMIN_KEY .env | cut -d= -f2 | cut -d' ' -f1)"; echo
register:  ; ./scripts/register-model.sh $(NAME) $(GGUF)
backup:    ; ./scripts/backup.sh
test:      ; cd gateway && python -m pytest -q
