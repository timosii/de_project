FROM python:3.12 as requirements-stage
WORKDIR /tmp

RUN pip install poetry poetry-plugin-export

COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12
WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./breast_cancer /code/breast_cancer
COPY ./.dbt /code/.dbt
COPY ./data_ingest.py /code/data_ingest.py
COPY ./entrypoint.sh /code/entrypoint.sh 
RUN chmod +x /code/entrypoint.sh
CMD ["./entrypoint.sh"]