from ctypes.macholib import framework

import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 2000)

df  = pd.read_parquet(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\day25_pandas\userdata1.parquet")

print(df)

print(df.columns)


Pandas
extract ( readcsv, readjson, readexcel,read database)
transformation
load

pytest
small framework

pyspark(Datbaricks)
pyspark
github


1. read csv1
2. read db
