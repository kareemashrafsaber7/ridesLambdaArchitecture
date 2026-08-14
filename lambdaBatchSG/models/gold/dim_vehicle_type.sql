{{ config(
    materialized='table',
    schema='batchgold'
) }}
SELECT
    vehicle_type_id,
    vehicle_type,
    description,
    base_rate,
    per_mile,
    per_minute

FROM VALUES
    (1, 'UberX', 'Standard', 2.50, 1.75, 0.35),
    (2, 'UberXL', 'Extra Large', 3.50, 2.25, 0.45),
    (3, 'UberPOOL', 'Shared Ride', 2.00, 1.50, 0.30),
    (4, 'Uber Comfort' ,'Comfortable', 3.00, 2.00, 0.40),
    (5, 'Uber Black', 'Premium', 5.00, 3.50, 0.60)
AS t(
    vehicle_type_id,
    vehicle_type,
    description,
    base_rate,
    per_mile,
    per_minute
)