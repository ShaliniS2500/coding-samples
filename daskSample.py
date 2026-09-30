import dask.dataframe as dd

df = dd.read_parquet("s3://data/uber/")

# How much did NYC pay Uber?
df.base_passenger_fare.sum().compute()

# And how much did drivers make?
df.driver_pay.sum().compute()