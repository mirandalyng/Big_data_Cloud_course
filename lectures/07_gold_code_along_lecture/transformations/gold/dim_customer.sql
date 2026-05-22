CREATE OR REFRESH MATERIALIZED VIEW supply_chain_live.gold.dim_customer
  COMMENT "Dim customer dedubplicated - gold layer" AS
SELECT
  product_card_id AS product_id,
  MAX_BY(product_name, order_date) AS product_name,
  ROUND(MAX_BY(product_price, order_date), 2) AS product_price


FROM
  supply_chain_live.silver.supply_chain_obt


GROUP BY
  product_id
ORDER BY
  product_id;

  -- customer_id integer [primary key]
  -- first_name string
  -- last_name string 
  -- country string
  -- state string 
  -- city string 
  -- street string 
  -- zipcode integer
  -- segment string 