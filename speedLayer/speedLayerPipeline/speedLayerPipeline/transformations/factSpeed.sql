CREATE OR REFRESH STREAMING TABLE
ridesstream.gold.fact_rides
AS

SELECT
r.ride_id, r.confirmation_number, p.passenger_sk,d.driver_sk,v.vehicle_sk,r.vehicle_type_id, r.payment_method_id, r.ride_status_id, r.pickup_city_id, r.dropoff_city_id, r.cancellation_reason_id,
r.pickup_location_id, r.dropoff_location_id, r.distance_miles, r.duration_minutes, r.pickup_timestamp, r.dropoff_timestamp, r.base_fare, r.distance_fare, r.time_fare, r.surge_multiplier, r.subtotal, r.tip_amount, r.total_fare, r.rating, r.event_timestamp

from stream(ridesstream.silver.rides_silver)
WATERMARK event_timestamp delay of interval 10 minutes
as r
left join
stream(ridesstream.gold.dim_passenger)
WATERMARK __start_at delay of interval 10 minutes 
as p
on r.passenger_id = p.passenger_id
and r.event_timestamp >= p.__START_AT
and (
    r.event_timestamp < p.__END_AT
    or p.__END_AT is null)

left join
stream(ridesstream.gold.dim_driver)
WATERMARK __start_at delay of interval 10 minutes 
as d
on d.driver_id = r.driver_id
and r.event_timestamp >= d.__START_AT
and (
    r.event_timestamp < d.__END_AT
    or d.__END_AT is null
)
left JOIN
stream(ridesstream.gold.dim_vehicle)
WATERMARK __start_at delay of interval 10 minutes 
as v
on v.vehicle_id = r.vehicle_id
and r.event_timestamp >= v.__START_AT
and (
    r.event_timestamp < v.__END_AT
    or v.__END_AT is null
);