{{ config(
    materialized='table',
    schema='batchgold'
) }}

SELECT
    vehicle_make_id,
    vehicle_make

FROM VALUES
    (1, 'Toyota'),
    (2, 'Honda'),
    (3, 'Ford'),
    (4, 'Chevrolet'),
    (5, 'Nissan'),
    (6, 'BMW'),
    (7, 'Mercedes')
AS t(
    vehicle_make_id,
    vehicle_make
)