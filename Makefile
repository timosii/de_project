up:
	docker compose up -d

build:
	docker compose build --no-cache

stop:
	docker compose down

remove:
	docker compose down -v