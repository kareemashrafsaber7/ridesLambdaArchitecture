{{ config(
    materialized='table',
    schema='batchgold'
) }}

SELECT
    {{ dbt_utils.generate_surrogate_key(['passenger_id','dbt_valid_from']) }} as passenger_sk,
    passenger_id,
    passenger_name,
    passenger_email,
    passenger_phone,
    event_timestamp as passenger_updated_at,
    dbt_valid_from as valid_from,
    dbt_valid_to as valid_to
FROM
    {{ ref('passenger_ss') }}