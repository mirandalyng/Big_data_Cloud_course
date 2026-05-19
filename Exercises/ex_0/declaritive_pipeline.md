# Medalltion Bronze Layer with Spark Decleration Pipelines 

(Ex 00 - task )

## How to step-by-step 

**create a folder structure (e.g. Bronze_layer --> explorations, transformations, utils)**

## 1. Create ETL pipeline 
**1. Go to "Jobs & Pipelines"**

**2. Create a new pipeline**

**3. Rename it**

**4. Settings -> choose root path (e.g. bronze folder)**

**5. Settings -> source code path (e.g. transformations folder) --> SAVE**

**6. Inside the workspace you can see the new pipeline created --> delete it (because it's pointed somewhere else)** 

**7. You can see on the root-folder that it is connected to the pipeline** 

**8. Click on that "open in pipeline editor"

**9. The root folder is the pipeline and all of the pipeline source code  folder are inside of the transformation folder** 

## 2. SQL catalog setup  

**1. Create a Query inside of the explorations folder --> rename to initial_setup"
**2.SQL**

To show catalogs: 

    `SHOW CATALOGS;`

Create catalog:

    `CREATE CATALOG IF NOT EXISTS (catalog_name)`

Use catalog to be able to create schemas inside of it:

    `USE CATALOG (catalog_name);`

create schcemas: 

    `
    CREATE SCHEMA IF NOT EXISTS bronze;
    CREATE SCHEMA IF NOT EXISTS silver; 
    CREATE SCHEMA IF NOT EXISTS gold;
    `

Create a volume for storing raw data (this will go into volume inside of default)

    `CREATE VOLUME IF NOT EXISTS raw;`


##3. Upload Files to Volume

**1. Go into Catalog, update to see the volume you created**
**2. Inside the cataloge you can see the schemas**
**3. Inside the default you can see the raw**
**4. Go inside the _raw_ folder --> files --> create directory (data, logs, metadata)
    - one for each csv file 
**5. Go inside each folder and upload the data


##4. Quick EDA Check
**1. create and EDA-notebook**
**2. Do some quick EDA to see paths etc.**

Check the volume paths:

    `VOLUME_PATH = "/Volumes/supply_chain_demo/default/raw"
    spark.sql(f"LIST '{VOLUME_PATH}'").display()`

    `spark.sql(f"LIST '{VOLUME_PATH}/data'").display()`

Show schemas: 
    `
    SHOW SCHEMAS IN supply_chain_demo;
    `

##5. PySpark Streaming Table
**1. Create foldes (bronze-silver-gold inside of the transformation)
**2. create and file inside the bronze folder (e.g. raw_supply_chain.py)**
**3. Write the script**

    # Spark declarity pipeline to get the data into our bronze layer

from pyspark import pipelines as dp

**4. Base dir with the data folders**
BASE_DIR = "/Volumes/supply_chain_demo/default/raw"

**5. Provide a schema to the data**

    `
    schema = (
        spark.read.format("csv")
        .options(header=True, inferSchema=True)
        .load(f"{BASE_DIR}/data/DataCoSupplyChainDataset.csv")
        .schema
    )

    # This will create a streaming table 
    # Supply-cataloge --> bronze schema --> raw supply chain (table)

    @dp.table(name="supply_chain_demo.bronze.raw_supply_chain", comment ="Raw supply chain data for DataCo", table_properties={
        "delta.columnMapping.mode": "name", 
        "delta.minReaderVersion": "2", 
        "delta.minWriterVersion": "5"
    })

    def raw_supply_chain(): 
        return (
            spark.readStream.format("csv").options(header=True, encoding="UTF-8").schema(schema).load(f"{BASE_DIR}/data")
        )
    `
**6. Run the pipeline**

**7. Go to the Catalog --> bronze --> see the new raw supply chain --> sample data --> connect**



## 6. SQL Streaming Tables

**1.Create another file in the bronze layer folder for the sequal (SQL) --> supply_chain_logs.sql**

**2. Ingest the log files**

    `
    CREATE OR REFRESH STREAMING TABLE airbnb.bronze.raw_access_logs
    COMMENT "Raw access logs" AS 
    SELECT 
    * FROM 
    STREAM read_files("/Volumes/airnb/default/raw/logs", format => "csv", header => true, inferSchema => true )
    `



