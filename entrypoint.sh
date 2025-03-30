#!/bin/bash
python data_ingest.py
cd /code/breast_cancer && dbt build --profiles-dir ../.dbt