{{ config(
    materialized='table',
    schema='batchgold'
) }}

SELECT
    ride_status_id,
    ride_status,
    is_active

FROM VALUES
    (1, 'Completed', TRUE),
    (2, 'Cancelled', FALSE)
AS t(
    ride_status_id,
    ride_status,
    is_active
)