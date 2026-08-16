{% snapshot vehicle_ss %}

{{
    config(
        target_schema='batchgold',
        unique_key='vehicle_id',
        strategy='timestamp',
        updated_at = 'vehicle_updated_at') }}

SELECT
    vehicle_id,
    vehicle_make,
    vehicle_model,
    vehicle_color,
    license_plate,
    vehicle_updated_at
FROM
    {{ ref('rides_silver_batch') }}
{% endsnapshot %}