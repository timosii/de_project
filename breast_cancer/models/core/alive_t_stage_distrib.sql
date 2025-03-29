{{ config(materialized='table') }}

SELECT t_stage, COUNT('*') as pats_count
FROM {{ source('staging','breast_cancer')}}
WHERE status = 'Alive'
GROUP BY t_stage