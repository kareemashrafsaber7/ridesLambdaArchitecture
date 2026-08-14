{% snapshot driver_ss %}

{{
    config(
        target_schema='batchgold',
        unique_key='driver_id',
        strategy='timestamp',
        updated_at = 'event_timestamp') }}

SELECT
    driver_id,
    driver_name,
    driver_rating,
    driver_phone,
    driver_license,
    event_timestamp
FROM
    {{ ref('rides_silver_batch') }}
{% endsnapshot %}