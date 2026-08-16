{% snapshot driver_ss %}

{{
    config(
        target_schema='batchgold',
        unique_key='driver_id',
        strategy='timestamp',
        updated_at = 'driver_updated_at') }}

SELECT
    driver_id,
    driver_name,
    driver_rating,
    driver_phone,
    driver_license,
    driver_updated_at
FROM
    {{ ref('rides_silver_batch') }}
{% endsnapshot %}