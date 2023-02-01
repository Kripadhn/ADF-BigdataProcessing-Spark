from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("DataMigration").getOrCreate()

# Load the source data
df = spark.read.parquet("<path-to-source-data>")

# Clean the data
df = df.dropDuplicates()
df = df.fillna(0, subset=["column1", "column2", "column3"])
df = df.filter(df["column4"] > 0)

# Write the cleaned data to the target data sink
df.write.parquet("<path-to-target-data>", mode="overwrite")

# Here is an example of PySpark code that cleans the data and loads it into Azure Data Lake Storage:
# This is a basic example of how ADF and Apache Spark can be used to migrate and clean data.
# The code can be further extended to perform more complex operations such as data quality checks and data enrichment.