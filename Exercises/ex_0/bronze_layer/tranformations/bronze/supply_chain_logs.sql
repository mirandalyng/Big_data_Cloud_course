CREATE OR REFRESH STREAMING TABLE airbnb.bronze.raw_access_logs
  COMMENT "Raw access logs" AS
SELECT
  *
FROM
  STREAM read_files(
    "/Volumes/airnb/default/raw/logs",
    format => "csv",
    header => TRUE,
    inferSchema => TRUE
  )

  