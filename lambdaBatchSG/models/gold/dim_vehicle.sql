{{ config(
    materialized='table',
    schema='batchgold'
) }}

SELECT
    {{ dbt_utils.generate_surrogate_key(['vehicle_id','dbt_valid_from']) }} as vehicle_sk,
    vehicle_id,
    vehicle_make,
    vehicle_model,
    vehicle_color,
    license_plate,
    event_timestamp as vehicle_updated_at,
    dbt_valid_from as valid_from,
    dbt_valid_to as valid_to
FROM
    {{ ref('vehicle_ss') }}