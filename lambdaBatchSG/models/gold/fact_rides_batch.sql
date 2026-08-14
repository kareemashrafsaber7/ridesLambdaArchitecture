{{ config(
    materialized='table',
    schema='batchgold'
) }}

SELECT
r.ride_id, r.confirmation_number, p.passenger_sk,d.driver_sk,v.vehicle_sk,r.vehicle_type_id, r.payment_method_id, r.ride_status_id, r.pickup_city_id, r.dropoff_city_id, r.cancellation_reason_id,
r.pickup_location_id, r.dropoff_location_id, r.distance_miles, r.duration_minutes, r.pickup_timestamp, r.dropoff_timestamp, r.base_fare, r.distance_fare, r.time_fare, r.surge_multiplier, r.subtotal, r.tip_amount, r.total_fare, r.rating, r.event_timestamp

from {{ ref('rides_silver_batch') }} r
left join
{{ ref('dim_passenger') }} p
on r.passenger_id = p.passenger_id
and r.event_timestamp >= p.valid_from
and (
    r.event_timestamp < p.valid_to
    or p.valid_to is null)

left join
{{ ref('dim_driver') }} d
on d.driver_id = r.driver_id
and r.event_timestamp >= d.valid_from
and (
    r.event_timestamp < d.valid_to
    or d.valid_to is null)

left JOIN
{{ ref('dim_vehicle') }} v
on v.vehicle_id = r.vehicle_id
and r.event_timestamp >= v.valid_from
and (
    r.event_timestamp < v.valid_to
    or v.valid_to is null
)