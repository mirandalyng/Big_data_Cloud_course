CREATE OR REFRESH MATERIALIZED VIEW supply_chain_live.gold.dim_product
  COMMENT "Dim products dedubplicated - gold layer" AS
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