from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

rules_silver = {

    "rule1": "ride_id is not null",
    "rule2": "confirmation_number is not null",

    "rule3": "vehicle_type_id is not null and vehicle_type_id in (1,2,3,4,5)",
    "rule4": "vehicle_make_id is not null and vehicle_make_id in (1,2,3,4,5,6,7)",
    "rule5": "payment_method_id is not null and payment_method_id in (1,2,3,4)",
    "rule6": "ride_status_id is not null and ride_status_id in (1,2)",
    "rule7": "pickup_city_id is not null and pickup_city_id between 1 and 10",
    "rule8": "dropoff_city_id is not null and dropoff_city_id between 1 and 10",
    "rule9": "cancellation_reason_id is not null and cancellation_reason_id in (1,2,3,4)",

    "rule10": "pickup_location_id is not null",
    "rule11": "dropoff_location_id is not null",

    "rule12": "pickup_address is not null",
    "rule13": "pickup_latitude is not null and pickup_latitude between -90 and 90",
    "rule14": "pickup_longitude is not null and pickup_longitude between -180 and 180",

    "rule15": "dropoff_address is not null",
    "rule16": "dropoff_latitude is not null and dropoff_latitude between -90 and 90",
    "rule17": "dropoff_longitude is not null and dropoff_longitude between -180 and 180",

    "rule18": "distance_miles is not null and distance_miles >= 0",
    "rule19": "duration_minutes is not null and duration_minutes >= 0",
    "rule21": "pickup_timestamp is not null",
    "rule22": "dropoff_timestamp is not null",

    "rule23": "base_fare is not null and base_fare >= 0",
    "rule24": "distance_fare is not null and distance_fare >= 0",
    "rule25": "time_fare is not null and time_fare >= 0",
    "rule26": "surge_multiplier is not null and surge_multiplier >= 1",
    "rule27": "subtotal is not null and subtotal >= 0",
    "rule28": "tip_amount is not null and tip_amount >= 0",
    "rule29": "total_fare is not null and total_fare >= 0",

    "rule30": "event_timestamp is not null",

    "rule31": "passenger_id is not null",
    "rule32": "passenger_name is not null",
    "rule33": "passenger_email is not null",
    "rule34": "passenger_updated_at is not null",

    "rule35": "driver_id is not null",
    "rule36": "driver_name is not null",
    "rule37": "driver_rating is not null and driver_rating between 0 and 5",
    "rule38": "driver_updated_at is not null",

    "rule39": "vehicle_id is not null",
    "rule40": "vehicle_make_id is not null",
    "rule41": "vehicle_model is not null",
    "rule42": "license_plate is not null",
    "rule43": "vehicle_updated_at is not null"
}


@dp.expect_all_or_fail(rules_silver)
@dp.table(
    name="ridesstream.silver.rides_silver"
)
def rides_silver():

    df = spark.readStream.table(
        "ridesstream.bronze.rides_bronze"
    )

    schema = StructType([

        StructField("ride_id", StringType()),
        StructField("confirmation_number", StringType()),

        StructField(
            "passenger",
            StructType([
                StructField("passenger_id", StringType()),
                StructField("passenger_name", StringType()),
                StructField("passenger_email", StringType()),
                StructField("passenger_phone", StringType()),
                StructField("updated_at", StringType()),
                StructField("operation", StringType())
            ])
        ),

        StructField(
            "driver",
            StructType([
                StructField("driver_id", StringType()),
                StructField("driver_name", StringType()),
                StructField("driver_rating", DoubleType()),
                StructField("driver_phone", StringType()),
                StructField("driver_license", StringType()),
                StructField("updated_at", StringType()),
                StructField("operation", StringType())
            ])
        ),

        StructField(
            "vehicle",
            StructType([
                StructField("vehicle_id", StringType()),
                StructField("vehicle_make_id", IntegerType()),
                StructField("vehicle_make", StringType()),
                StructField("vehicle_model", StringType()),
                StructField("vehicle_color", StringType()),
                StructField("license_plate", StringType()),
                StructField("updated_at", StringType()),
                StructField("operation", StringType())
            ])
        ),

        StructField("vehicle_type_id", IntegerType()),
        StructField("payment_method_id", IntegerType()),
        StructField("ride_status_id", IntegerType()),

        StructField("pickup_city_id", IntegerType()),
        StructField("dropoff_city_id", IntegerType()),
        StructField("cancellation_reason_id", IntegerType()),

        StructField("pickup_location_id", StringType()),
        StructField("dropoff_location_id", StringType()),

        StructField("pickup_address", StringType()),
        StructField("pickup_latitude", DoubleType()),
        StructField("pickup_longitude", DoubleType()),

        StructField("dropoff_address", StringType()),
        StructField("dropoff_latitude", DoubleType()),
        StructField("dropoff_longitude", DoubleType()),

        StructField("distance_miles", DoubleType()),
        StructField("duration_minutes", IntegerType()),
        StructField("pickup_timestamp", StringType()),
        StructField("dropoff_timestamp", StringType()),

        StructField("base_fare", DoubleType()),
        StructField("distance_fare", DoubleType()),
        StructField("time_fare", DoubleType()),
        StructField("surge_multiplier", DoubleType()),
        StructField("subtotal", DoubleType()),
        StructField("tip_amount", DoubleType()),
        StructField("total_fare", DoubleType()),

        StructField("rating", IntegerType()),

        StructField("event_timestamp", StringType())
    ])

    df_parsed = (
        df
        .withColumn(
            "data",
            from_json(
                col("value").cast("string"),
                schema
            )
        )
    )

    df_silver = df_parsed.select(

        "data.ride_id",
        "data.confirmation_number",
        "data.passenger.passenger_id",
        "data.passenger.passenger_name",
        "data.passenger.passenger_email",
        "data.passenger.passenger_phone",
        col("data.passenger.updated_at")
            .alias("passenger_updated_at"),

        "data.driver.driver_id",
        "data.driver.driver_name",
        "data.driver.driver_rating",
        "data.driver.driver_phone",
        "data.driver.driver_license",
        col("data.driver.updated_at")
            .alias("driver_updated_at"),
        "data.vehicle.vehicle_id",
        "data.vehicle.vehicle_make_id",
        "data.vehicle.vehicle_make",
        "data.vehicle.vehicle_model",
        "data.vehicle.vehicle_color",
        "data.vehicle.license_plate",
        col("data.vehicle.updated_at")
            .alias("vehicle_updated_at"),

       
        "data.vehicle_type_id",
        "data.payment_method_id",
        "data.ride_status_id",
        "data.pickup_city_id",
        "data.dropoff_city_id",
        "data.cancellation_reason_id",

 
        "data.pickup_location_id",
        "data.dropoff_location_id",

        "data.pickup_address",
        "data.pickup_latitude",
        "data.pickup_longitude",

        "data.dropoff_address",
        "data.dropoff_latitude",
        "data.dropoff_longitude",
        "data.distance_miles",
        "data.duration_minutes",
        "data.pickup_timestamp",
        "data.dropoff_timestamp",
        "data.base_fare",
        "data.distance_fare",
        "data.time_fare",
        "data.surge_multiplier",
        "data.subtotal",
        "data.tip_amount",
        "data.total_fare",
        coalesce(
            col("data.rating"),
            lit(5)
        ).alias("rating"),
        "data.event_timestamp"
    )

    df_silver = df_silver.withColumn(
        "event_timestamp",
        to_timestamp(col("event_timestamp")))
    
    df_silver = df_silver.withWatermark("event_timestamp", "10 minutes")
    df_silver = df_silver.dropDuplicates(subset=['ride_id'])

    return df_silver