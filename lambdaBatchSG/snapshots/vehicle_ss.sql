{% snapshot vehicle_ss %}

{{
    config(
        target_schema='batchgold',
        unique_key='vehicle_id',
        strategy='timestamp',
        updated_at = 'event_timestamp') }}

SELECT
    vehicle_id,
    vehicle_make,
    vehicle_model,
    vehicle_color,
    license_plate,
    event_timestamp
FROM
    {{ ref('rides_silver_batch') }}
{% endsnapshot %}