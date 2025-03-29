#!/bin/bash
python data_ingest.py
cd /code/breast_cancer && dbt run --profiles-dir ../.dbt