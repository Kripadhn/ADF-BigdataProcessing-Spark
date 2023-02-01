Set up Azure Data Factory (ADF):

Create an Azure Data Factory instance in the Azure portal.
Create an input data source for real-time data streams (e.g., Azure Event Hubs or IoT Hubs).
Create an output data sink (e.g., Azure Synapse Analytics or Azure SQL Database).
Ingest data into Event Hubs or IoT Hubs:

Ingest real-time data streams into Azure Event Hubs or IoT Hubs using a device or a custom solution.
Create a Streaming Pipeline:

Create a pipeline in ADF that contains a Streaming data flow activity.
Configure the Streaming data flow activity to process the real-time data streams from Event Hubs or IoT Hubs.
The Streaming data flow can perform operations such as filtering, transforming, aggregating, and enriching the data.
Store the results:

Store the results of the Streaming data flow in the output data sink.
The results can be stored in a format such as Parquet or Avro.