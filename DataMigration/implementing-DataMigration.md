Here is a step-by-step implementation of data migration using Azure Data Factory (ADF) and Apache Spark with Python code:

Set up Azure Data Factory (ADF):

Create an Azure Data Factory instance in the Azure portal.
Create an input data source for the source data (e.g., Azure Blob Storage or Azure SQL Database).
Create an output data sink for the target data (e.g., Azure Blob Storage or Azure Data Lake Storage).
Create a Migration Pipeline:

Create a pipeline in ADF that contains two activities: a Data Extraction activity and a Data Loading activity.
The Data Extraction activity reads the source data and writes it to the intermediate data sink (e.g., Azure Blob Storage).
The Data Loading activity reads the intermediate data and writes it to the target data sink.
Clean the Data:

Use Spark to clean the data in the intermediate data sink.
The data cleaning process can include operations such as data transformation, data enrichment, data cleansing, and data standardization.
Load the Clean Data:

Use Spark to read the cleaned data from the intermediate data sink and write it to the target data sink.