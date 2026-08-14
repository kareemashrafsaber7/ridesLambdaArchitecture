# Databricks notebook source
df_cancel = spark.table("ridesstream.batchgold.dim_cancellation_reason")

synapse_url = "jdbc:sqlserver://rideslambdasyn.sql.azuresynapse.net:1433;database=ridesLambdaDW"

df_cancel.write \
    .format("sqlserver") \
    .option("host", "rideslambdasyn.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "ridesLambdaDW") \
    .option("dbtable", "gold.dim_cancellation_reason") \
    .option("user", "kareem") \
    .option("password", "") \
    .mode("append") \
    .save()

# COMMAND ----------

df_city = spark.table("ridesstream.batchgold.dim_city")

synapse_url = "jdbc:sqlserver://rideslambdasyn.sql.azuresynapse.net:1433;database=ridesLambdaDW"

df_city.write \
    .format("sqlserver") \
    .option("host", "rideslambdasyn.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "ridesLambdaDW") \
    .option("dbtable", "gold.dim_city") \
    .option("user", "kareem") \
    .option("password", " ") \
    .mode("append") \
    .save()

# COMMAND ----------

df_driver = spark.table("ridesstream.batchgold.dim_driver")

synapse_url = "jdbc:sqlserver://rideslambdasyn.sql.azuresynapse.net:1433;database=ridesLambdaDW"

df_driver.write \
    .format("sqlserver") \
    .option("host", "rideslambdasyn.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "ridesLambdaDW") \
    .option("dbtable", "gold.dim_driver") \
    .option("user", "kareem") \
    .option("password", " ") \
    .mode("append") \
    .save()

# COMMAND ----------

df_passenger = spark.table("ridesstream.batchgold.dim_passenger")

synapse_url = "jdbc:sqlserver://rideslambdasyn.sql.azuresynapse.net:1433;database=ridesLambdaDW"

df_passenger.write \
    .format("sqlserver") \
    .option("host", "rideslambdasyn.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "ridesLambdaDW") \
    .option("dbtable", "gold.dim_passenger") \
    .option("user", "kareem") \
    .option("password", " ") \
    .mode("append") \
    .save()

# COMMAND ----------

df_payment_method = spark.table("ridesstream.batchgold.dim_payment_methods")

synapse_url = "jdbc:sqlserver://rideslambdasyn.sql.azuresynapse.net:1433;database=ridesLambdaDW"

df_payment_method.write \
    .format("sqlserver") \
    .option("host", "rideslambdasyn.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "ridesLambdaDW") \
    .option("dbtable", "gold.dim_payment_methods") \
    .option("user", "kareem") \
    .option("password", " ") \
    .mode("append") \
    .save()

# COMMAND ----------

df_ride_status = spark.table("ridesstream.batchgold.dim_ride_status")

synapse_url = "jdbc:sqlserver://rideslambdasyn.sql.azuresynapse.net:1433;database=ridesLambdaDW"

df_ride_status.write \
    .format("sqlserver") \
    .option("host", "rideslambdasyn.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "ridesLambdaDW") \
    .option("dbtable", "gold.dim_ride_status") \
    .option("user", "kareem") \
    .option("password", " ") \
    .mode("append") \
    .save()

# COMMAND ----------

df_vehicle = spark.table("ridesstream.batchgold.dim_vehicle")

synapse_url = "jdbc:sqlserver://rideslambdasyn.sql.azuresynapse.net:1433;database=ridesLambdaDW"

df_vehicle.write \
    .format("sqlserver") \
    .option("host", "rideslambdasyn.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "ridesLambdaDW") \
    .option("dbtable", "gold.dim_vehicle") \
    .option("user", "kareem") \
    .option("password", " ") \
    .mode("append") \
    .save()

# COMMAND ----------

df_make = spark.table("ridesstream.batchgold.dim_vehicle_make")

synapse_url = "jdbc:sqlserver://rideslambdasyn.sql.azuresynapse.net:1433;database=ridesLambdaDW"

df_make.write \
    .format("sqlserver") \
    .option("host", "rideslambdasyn.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "ridesLambdaDW") \
    .option("dbtable", "gold.dim_vehicle_make") \
    .option("user", "kareem") \
    .option("password", " ") \
    .mode("append") \
    .save()

# COMMAND ----------

df_fact = spark.table("ridesstream.batchgold.fact_rides_batch")

synapse_url = "jdbc:sqlserver://rideslambdasyn.sql.azuresynapse.net:1433;database=ridesLambdaDW"

df_fact.write \
    .format("sqlserver") \
    .option("host", "rideslambdasyn.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "ridesLambdaDW") \
    .option("dbtable", "gold.fact_rides_batch") \
    .option("user", "kareem") \
    .option("password", " ") \
    .mode("append") \
    .save()