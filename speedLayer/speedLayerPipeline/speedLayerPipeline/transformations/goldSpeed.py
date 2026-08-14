from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

@dp.view
def passenger_view():
    df = spark.readStream.table("ridesstream.silver.rides_silver")
    df =df.select("passenger_id","passenger_name","passenger_email","passenger_phone",to_timestamp("event_timestamp").alias("passenger_updated_at"))
    df = df.withColumn("passenger_sk",sha2(col("passenger_id"),256))
    return df

dp.create_streaming_table("ridesstream.gold.dim_passenger")
dp.create_auto_cdc_flow(
    target="ridesstream.gold.dim_passenger",
    source="passenger_view",
    keys=["passenger_id"],
    sequence_by=col("passenger_updated_at"),
    stored_as_scd_type=2
)


@dp.view
def driver_view():
    df = spark.readStream.table("ridesstream.silver.rides_silver")
    df = df.select("driver_id","driver_name","driver_rating","driver_phone","driver_license",to_timestamp("event_timestamp").alias("driver_updated_at"))
    df = df.withColumn("driver_sk",sha2(col("driver_id"),256))
    return df

dp.create_streaming_table("ridesstream.gold.dim_driver")
dp.create_auto_cdc_flow(
    target="ridesstream.gold.dim_driver",
    source="driver_view",
    keys=["driver_id"],
    sequence_by=col("driver_updated_at"),
    stored_as_scd_type=2
)



@dp.view
def vehicle_view():
    df = spark.readStream.table("ridesstream.silver.rides_silver")
    df = df.select("vehicle_id","vehicle_make","vehicle_model","vehicle_color","license_plate",to_timestamp("event_timestamp").alias("vehicle_updated_at"))
    df = df.withColumn("vehicle_sk",sha2(col("vehicle_id"),256))
    return df

dp.create_streaming_table("ridesstream.gold.dim_vehicle")
dp.create_auto_cdc_flow(
    target="ridesstream.gold.dim_vehicle",
    source="vehicle_view",
    keys=["vehicle_id"],
    sequence_by=col("vehicle_updated_at"),
    stored_as_scd_type=2
)