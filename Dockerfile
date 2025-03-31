FROM python:3.12 as requirements-stage
WORKDIR /tmp

RUN pip install poetry poetry-plugin-export

COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12 as base
WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /code/requirements.txt

FROM base as app
COPY ./breast_cancer /code/breast_cancer
COPY ./.dbt /code/.dbt
COPY ./app /code/app
COPY ./entrypoint.sh /code/entrypoint.sh 
RUN chmod +x /code/entrypoint.sh
CMD ["./entrypoint.sh"]

FROM apache/airflow:2.9.0-python3.12 as airflow
USER root

COPY --from=requirements-stage /tmp/requirements.txt /tmp/requirements.txt
RUN chown airflow /tmp/requirements.txt && \
    su -c "pip install --no-cache-dir --upgrade -r /tmp/requirements.txt" airflow

USER airflow

