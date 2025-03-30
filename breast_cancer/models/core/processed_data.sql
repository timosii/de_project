{{ config(materialized='table') }}

with source_data as (
  select * from {{ source('raw', 'breast_cancer') }}
)

select
    distinct {{ generate_deterministic_uuid(source('raw', 'breast_cancer')) }} as patient_id,
    source_data.*,
    current_timestamp as load_ts
from source_data