{{ config(
    materialized='table',
    schema='batchgold'
) }}

SELECT
    city_id,
    city,
    state,
    region

FROM VALUES
    (1, 'New York', 'NY', 'Northeast'),
    (2, 'Los Angeles', 'CA', 'West'),
    (3, 'Chicago', 'IL', 'Midwest'),
    (4, 'Houston', 'TX', 'South'),
    (5, 'Phoenix', 'AZ', 'Southwest'),
    (6, 'Philadelphia', 'PA', 'Northeast'),
    (7, 'San Antonio', 'TX', 'South'),
    (8, 'San Diego', 'CA', 'West'),
    (9, 'Dallas', 'TX', 'South'),
    (10, 'San Jose', 'CA', 'West')
AS t(
    city_id,
    city,
    state,
    region
)