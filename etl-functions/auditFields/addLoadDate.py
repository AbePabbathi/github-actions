# Databricks notebook source
from pyspark.sql.functions import lit
from datetime import datetime

def addLoadDate(df):
    df = df.withColumn("_loadDate",lit(datetime.now()))
    return df

# COMMAND ----------

# df = spark.createDataFrame(["10","11","13"], "string").toDF("age")
# display(df)

# COMMAND ----------

# newdf = addLoadDate(df)
# display(newdf)
