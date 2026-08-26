## What is medallian architecture? 

**A way to organize data in data lakehouse**
    - Databricks is a data lakehouse (contains the data lake and warehouse)
    - A way to organize the data 

**When data are continuously redined throughout a data pipeline, data with improving quality are stored in different data layers**

    - Bronze 
    - Silver 
    - Gold 

When we go futher in the layers the data is more and more refined data 

### Benefits of medallion architecture 
 
- Preserce historucal archive of source data and make reproccisng easy 
- Enadble step-by-step transformation 
- Data lineage for debugging 
    - see where the data has flowed for one table to another or one view to another
    - you can go back and debugg it easy 
- Enhance performance by scaling layers separatly

- Simple model - easy to understand and implement
- Flexibility - can always recreate Silver/Gold from Bronze
- Speed - incremental ETL, ACID transactions
- Traceability - complete history and time travel
- Cost-effective - can combine data across entire enterprise for advanced analytics


### Data Layers 


![Data Layers](https://www.databricks.com/sites/default/files/inline-images/building-data-pipelines-with-delta-lake-120823.png)

#### 1. Bronze layer: 

**Data sources:** csv API, databases etc --> *Data ingestion* --> **Bronze:** raw data format

- EL part (Extract & Load)
- Exact copy from source systems, as-is
- No transformations at all
- Includes metadata (when loaded, from where, process ID, etc.)
- Purpose: Historical archive, traceability, ability to recreate everything without going back to source

#### 2. Silver layer: 

**Data transformation** --> **Silver:** cleaned and restructured 

- Data from different sources is matched and merged
- Duplicates removed, formats standardized
- Creates an "Enterprise view" - unified picture of core business entities (customers, products, transactions)
- Minimal transformation - only "just-enough" cleansing (ELT instead of ETL)
- Normalized data models (3NF or Data Vault)
- Purpose: Fast data delivery for ad-hoc analysis, self-service for analysts and data scientists

#### 3. Gold layer: 

**Project-specific complex transformation** --> **Gold:** comsumption-ready  

- Project-specific databases optimized for consumption
- Denormalized (fewer joins = faster reads)
- Ready-made reports and dashboards
- Star schemas (Kimball) or Data Marts (Inmon)
- Examples: Customer analytics, sales reports, product recommendations, KPI dashboards

#### Notes: 
- You don't need to use all the layers (maybe silver is enough)
- You can adapt it to your need 
- Add or remove layers 






