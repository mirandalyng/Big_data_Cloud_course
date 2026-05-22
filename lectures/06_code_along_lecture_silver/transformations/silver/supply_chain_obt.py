from pyspark.sql.functions import to_timestamp, col, coalesce, lit, when, round as spark_round
from pyspark import pipelines as dp
from utils.utils import rename_columns_to_snake_case

@dp.table(name="supply_chain_live.silver.supply_chain_obt", 
          comment ="Cleaned supply chain data for DataCo", 
          table_properties={
            "delta.columnMapping.mode": "name", 
            "delta.minReaderVersion": "2", 
            "delta.minWriterVersion": "5"
    }
)

def cleaned_supply_chain():
    df = spark.sql("FROM STREAM supply_chain_live.bronze.raw_supply_chain")
    df = rename_columns_to_snake_case(df)


    return (
        df.withColumn(
            "shipping_date", to_timestamp("shipping_date_(dateorders)", "M/d/yyyy H:mm")
        )
        .withColumn(
            "order_zipcode", coalesce(col("order_zipcode").cast("string"), lit("unknown"))
        )
        .withColumn(
            "customer_zipcode",
            coalesce(col("customer_zipcode").cast("string"), lit("unknown")),
        )
        .withColumn(
        "customer_lname", coalesce(col("customer_lname"), lit("unknown"))
        )
        .withColumn(
            "customer_country",
            when(col("customer_country") == "EE. UU.", "United States").otherwise(
                col("customer_country")
            ),
        )
        .withColumn("order_date", to_timestamp("order_date_(dateorders)", "M/d/yyyy H:mm"))
        
        .withColumn(
        "order_item_product_price", spark_round(col("order_item_product_price"), 2))
        .withColumn("benefit_per_order", spark_round(col("benefit_per_order"), 2))
        .withColumn("sales_per_customer", spark_round(col("sales_per_customer"), 2))
        .withColumn(
        "order_item_total",
        spark_round(
            col("order_item_quantity") 
            * col("order_item_product_price") 
            * (1 - col("order_item_discount_rate")), 
            2))
        
    ).drop(
        "customer_email",
        "customer_password",
        "product_description",
        "shipping_date_(dateorders)",
        "order_date_(dateorders)",
    )