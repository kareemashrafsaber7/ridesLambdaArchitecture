{% snapshot passenger_ss %}

{{
    config(
        target_schema='batchgold',
        unique_key='passenger_id',
        strategy='timestamp',
        updated_at = 'passenger_updated_at') }}

SELECT
    passenger_id,
    passenger_name,
    passenger_email,
    passenger_phone,
    passenger_updated_at
FROM
    {{ ref('rides_silver_batch') }}
{% endsnapshot %}