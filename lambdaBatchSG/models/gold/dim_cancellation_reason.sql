{{ config(
    materialized='table',
    schema='batchgold'
) }}
SELECT
    cancellation_reason_id,
    cancellation_reason

FROM VALUES
    (1, 'Driver cancelled'),
    (2, 'Passenger cancelled'),
    (3, 'No show'),
    (4, 'Unknown')
AS t(
    cancellation_reason_id,
    cancellation_reason
)