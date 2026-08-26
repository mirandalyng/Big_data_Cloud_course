# Spark declarity pipeline to get the data into our bronze layer

from pyspark import pipelines as dp

# Base dir with the data folders
BASE_DIR = "/Volumes/supply_chain_demo/default/raw"

# Provide a schema to the data

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

