CREATE OR REFRESH STREAMING TABLE supply_chain_live.gold.fct_orderlines
  COMMENT "Fact table - gold layer" AS
-- mark the code and run
-- rename the columns as in the dimentional db-diagram
SELECT
  order_item_id,
  order_id,
  customer_id,
  product_card_id AS product_id,
  date_format(order_date, 'yyyyMMddHHmm')::BIGINT AS order_datetime_id,
  -- 2017-06-17T04:41:00.000+0000 -> 201706170441
  order_item_product_price AS order_item_price,
  order_item_quantity AS quantiy,
  order_item_discount_rate AS discount_rate,
  ROUND(order_item_price * quantiy * (1 - discount_rate), 2) AS total_amount


FROM
  STREAM supply_chain_live.silver.supply_chain_obt