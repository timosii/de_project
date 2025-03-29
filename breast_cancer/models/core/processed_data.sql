{{ config(materialized='table') }}

with source_data as (
  select * from {{ source('raw', 'breast_cancer') }}
)

select
    {{ generate_uuid() }} as patient_id,
    source_data.*,
    current_timestamp as load_ts
from source_data