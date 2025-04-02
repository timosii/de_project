# Health Data Analytics Pipeline

An end-to-end data pipeline for processing and analyzing breast cancer patient data using modern data tools.

![pipeline](/assets/pipeline.jpg)

## Table of Contents
1. [Problem & Solution](#problem--solution)
2. [Tech Stack](#tech-stack)
3. [Features](#features)
4. [Quick Start](#quick-start)
   - [Prerequisites](#prerequisites)
   - [Setup Steps](#steps)
5. [Access Services](#access-services)
6. [Database Structure](#database-structure)
   - [Raw Data](#raw-data)
   - [Processed Data](#processed-data)
7. [Development](#development)
8. [Uninstall](#uninstall)

## Problem & Solution
### Outdated medical data practices:
- Paper records → slow retrieval, risk of loss
- Manual processing → errors and delays
- Isolated Excel files → version chaos
- Disconnected systems → lost or duplicate records
- No data validation → "garbage in, garbage out" analytics
- Monthly or weekly updates → decisions made on stale data

### Solution:
An automated batch pipeline that:
- Loads data periodically
- Validates quality
- Updates dashboards

#### Result:  
Always up-to-date, reliable data.

## Tech Stack

- **Data Ingestion**: [dlt](https://dlthub.com/)
- **Data Warehouse**: [PostgreSQL](https://www.postgresql.org/)
- **Transformation**: [dbt](https://www.getdbt.com/)
- **Visualization**: [Apache Superset](https://superset.apache.org/)
- **Orchestration**: [Airflow](https://airflow.apache.org/)
- **Containerization**: [Docker](https://www.docker.com/)

## Features

✔️ Automated data loading with schema detection  
✔️ Data quality testing with dbt  
✔️ Interactive dashboards in Superset  
✔️ Scheduled pipeline execution  
✔️ Local development environment  
✔️ One-command deployment 🚀

## Quick Start

### Prerequisites
- Docker 20.10.13+
- 2GB RAM, 8GB disk space
- Linux/WSL (Windows/Mac not fully tested)

### Steps
```bash
# Clone repository
git clone https://github.com/timosii/de_project.git
cd de_project

# Initialize environment
cp .env_example .env

# Start services
make up
```
And that's it!

#### Additional commands:
```bash
# Stop all services while preserving data
make stop
# Rebuild containers after code/Dockerfile changes  
make build
```
## Access Services

### 🚀 Airflow
- **URL**: [http://localhost:8080](http://localhost:8080)
- **Credentials**: 
  - Username: `admin`
  - Password: `admin`

> Airflow orchestrates the daily pipeline execution. DAGs are located in `airflow/dags/`

### 📊 pgAdmin
- **URL**: [http://localhost:8085](http://localhost:8085)
- **Credentials**:
  - Email: `admin@admin.com`
  - Password: `admin`
- **Connection Details**:
  ```ini
  Host=postgres_zoomcamp
  Port=5432
  Maintenance DB=breast_cancer
  Username=postgres
  Password=postgres

### 📈 Superset
- **URL**: [http://localhost:8088](http://localhost:8088)
- **Credentials**: `admin`/`admin`
- **Sample Dashboard**: [http://localhost:8088/superset/dashboard/1](http://localhost:8088/superset/dashboard/1)

![base_dashboard](/assets/base_dashboard.jpg)

## Database Structure

### Raw Data
- **Schema**: `public`
- **Table**: `breast_cancer`
  - Contains original source data in raw format

### Processed Data  
- **Schema**: `dwh`  
- **Table**: `processed_data`  
  - `patient_id`: Unique UUID identifier  
  - `load_ts`: Timestamp of data processing  
  - Automated data quality tests including:  
    - Null checks  
    - Uniqueness validation  
    - Data type verification  

## Development  
- Add **Airflow DAGs** to `airflow/dags/`
- Add some **scripts** for automatization to `app/`
- Add **dbt models** to `breast_cancer/models/`

## Uninstall
- `make remove` - use for remove volumes
- `make remove-images` - for remove all non-official project images
- `rm -rf de_project/` - delete project folder

## 🎉 Enjoy!
Thank you for your time! For questions or contributions, please [open an issue on GitHub](https://github.com/timosii/de_project/issues)
