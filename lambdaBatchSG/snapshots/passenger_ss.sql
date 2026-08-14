{% snapshot passenger_ss %}

{{
    config(
        target_schema='batchgold',
        unique_key='passenger_id',
        strategy='timestamp',
        updated_at = 'event_timestamp') }}

SELECT
    passenger_id,
    passenger_name,
    passenger_email,
    passenger_phone,
    event_timestamp
FROM
    {{ ref('rides_silver_batch') }}
{% endsnapshot %}