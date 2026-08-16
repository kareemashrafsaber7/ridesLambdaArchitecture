{{ config(
    materialized='table',
    schema='batchgold'
) }}

SELECT
    {{ dbt_utils.generate_surrogate_key(['driver_id','dbt_valid_from']) }} as driver_sk,
    driver_id,
    driver_name,
    driver_rating,
    driver_phone,
    driver_license,
    driver_updated_at,
    dbt_valid_from as valid_from,
    dbt_valid_to as valid_to
FROM
    {{ ref('driver_ss') }}