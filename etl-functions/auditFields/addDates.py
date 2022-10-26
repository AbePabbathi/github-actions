from pyspark.sql.functions import lit
from datetime import datetime
# add load date func
def addLoadDate(df):
    df = df.withColumn("_loadDate",lit(datetime.now()))
    return df