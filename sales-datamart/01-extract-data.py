# Databricks notebook source
# MAGIC %fs
# MAGIC ls /databricks-datasets/asa/airlines/2007.csv

# COMMAND ----------

df = spark.read.option("header","true").option("inferSchema","true").csv("/databricks-datasets/asa/airlines/2007.csv")
df.count()

# COMMAND ----------

# create temp view
df.createOrReplaceTempView("flights_tmp")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- sample query
# MAGIC select count(*) from flights_tmp
