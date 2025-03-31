up:
	docker compose up -d

build:
	docker compose build --no-cache

stop:
	docker compose down

remove:
	docker compose down -v

remove-images:
	docker rmi de_project-airflow-webserver de_project-airflow-scheduler de_project-airflow-init de_project-app