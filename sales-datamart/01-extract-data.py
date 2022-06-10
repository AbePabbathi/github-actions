# Databricks notebook source
# MAGIC %fs
# MAGIC ls /databricks-datasets/asa/airlines/2007.csv

# COMMAND ----------

df = spark.read.option("header","true").option("inferSchema","true").csv("/databricks-datasets/asa/airlines/2007.csv")
df.count()
