{{ config(
    materialized='incremental',
    unique_key='ride_id',
    schema = 'batchsilver'
) }}

WITH parsed AS (

    SELECT
        from_json(
            CAST(value AS STRING),
            '''
            STRUCT<
                ride_id: STRING,
                confirmation_number: STRING,

                passenger: STRUCT<
                    passenger_id: STRING,
                    passenger_name: STRING,
                    passenger_email: STRING,
                    passenger_phone: STRING,
                    updated_at: STRING,
                    operation: STRING
                >,

                driver: STRUCT<
                    driver_id: STRING,
                    driver_name: STRING,
                    driver_rating: DOUBLE,
                    driver_phone: STRING,
                    driver_license: STRING,
                    updated_at: STRING,
                    operation: STRING
                >,

                vehicle: STRUCT<
                    vehicle_id: STRING,
                    vehicle_make_id: INT,
                    vehicle_make: STRING,
                    vehicle_model: STRING,
                    vehicle_color: STRING,
                    license_plate: STRING,
                    updated_at: STRING,
                    operation: STRING
                >,

                vehicle_type_id: INT,
                payment_method_id: INT,
                ride_status_id: INT,

                pickup_city_id: INT,
                dropoff_city_id: INT,
                cancellation_reason_id: INT,

                pickup_location_id: STRING,
                dropoff_location_id: STRING,

                pickup_address: STRING,
                pickup_latitude: DOUBLE,
                pickup_longitude: DOUBLE,

                dropoff_address: STRING,
                dropoff_latitude: DOUBLE,
                dropoff_longitude: DOUBLE,

                distance_miles: DOUBLE,
                duration_minutes: INT,

                booking_timestamp: STRING,
                pickup_timestamp: STRING,
                dropoff_timestamp: STRING,

                base_fare: DOUBLE,
                distance_fare: DOUBLE,
                time_fare: DOUBLE,
                surge_multiplier: DOUBLE,
                subtotal: DOUBLE,
                tip_amount: DOUBLE,
                total_fare: DOUBLE,

                rating: INT,

                event_timestamp: STRING
            >
            '''
        ) AS data

    FROM {{ source('bronze', 'rides_bronze') }}

),

cleaned AS (

    SELECT

        data.ride_id,
        data.confirmation_number,

        data.passenger.passenger_id,
        data.passenger.passenger_name,
        data.passenger.passenger_email,
        data.passenger.passenger_phone,
        TO_TIMESTAMP(data.passenger.updated_at)
            AS passenger_updated_at,

        data.driver.driver_id,
        data.driver.driver_name,
        data.driver.driver_rating,
        data.driver.driver_phone,
        data.driver.driver_license,
        TO_TIMESTAMP(data.driver.updated_at)
            AS driver_updated_at,

        data.vehicle.vehicle_id,
        data.vehicle.vehicle_make_id,
        data.vehicle.vehicle_make,
        data.vehicle.vehicle_model,
        data.vehicle.vehicle_color,
        data.vehicle.license_plate,
        TO_TIMESTAMP(data.vehicle.updated_at)
            AS vehicle_updated_at,

        data.vehicle_type_id,
        data.payment_method_id,
        data.ride_status_id,

        data.pickup_city_id,
        data.dropoff_city_id,
        data.cancellation_reason_id,

        data.pickup_location_id,
        data.dropoff_location_id,

        data.pickup_address,
        data.pickup_latitude,
        data.pickup_longitude,

        data.dropoff_address,
        data.dropoff_latitude,
        data.dropoff_longitude,

        data.distance_miles,
        data.duration_minutes,

        TO_TIMESTAMP(data.booking_timestamp) AS booking_timestamp,
        TO_TIMESTAMP(data.pickup_timestamp) AS pickup_timestamp,
        TO_TIMESTAMP(data.dropoff_timestamp) AS dropoff_timestamp,

        data.base_fare,
        data.distance_fare,
        data.time_fare,
        data.surge_multiplier,
        data.subtotal,
        data.tip_amount,
        data.total_fare,

        COALESCE(data.rating, 5) AS rating,

        TO_TIMESTAMP(data.event_timestamp) AS event_timestamp

    FROM parsed

)

SELECT *
FROM cleaned

{% if is_incremental() %}
WHERE event_timestamp > (SELECT MAX(event_timestamp) - INTERVAL 10 MINUTES FROM {{ this }})
{% endif %}