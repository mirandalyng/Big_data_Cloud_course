| Terminology | Explanation |
| :--- | :--- |
| **On-premises IT infrastructure** | Egen fysisk IT-infrastruktur (hårdvara, servrar, nätverk) som ägs, driftas och underhålls lokalt i företagets egna lokaler eller datacenter. |
| **Cloud IT infrastructure** | IT-infrastruktur (servrar, lagring, databaser) som hyrs som en tjänst över internet från en molnleverantör (t.ex. AWS, Azure, Google Cloud). |
| **3 Vs of big data** | De tre grundpelarna som definierar Big Data: **Volume** (enorm datamängd), **Velocity** (hög hastighet i datatillväxt/strömning) och **Variety** (blandade dataformat; strukturerad, semistrukturerad och ostrukturerad data). |
| **Scalability** | Skalbarhet; systemets förmåga och kapacitet att hantera en ökande mängd arbete eller data genom att lägga till resurser (antingen vertikalt genom starkare maskiner eller horisontellt genom fler maskiner). |
| **Availability** | Tillgänglighet; den procentuella tid som ett system eller en tjänst är i drift, fungerar korrekt och är nåbar för användarna (ofta mätt i "antal nior", t.ex. 99.9%). |
| **Lakeflow Connect** | En funktion inom Databricks Lakeflow som automatiserar och förenklar datainläsning (ingestion) från externa källor och SaaS-applikationer direkt in i data-lakehouset. |
| **Lakeflow Spark Declarative Pipeline** | Ett deklarativt ramverk i Databricks (bygger på Delta Live Tables) där man beskriver *vad* datatransformationerna ska göra snarare än *hur* stegen ska köras, vilket automatiserar orkestrering och kvalitetskontroll. |
| **Unity Catalog** | Databricks centraliserade styrnings- och säkerhetsverktyg (governance) som hanterar åtkomstkontroll, datasekretess, spårbarhet (lineage) och auditering över hela plattformen. |
| **Data Lakehouse** | En modern dataarkitektur som kombinerar de bästa egenskaperna från ett *Data Lake* (billig lagring av all rådata) med ett *Data Warehouse* (struktur, ACID-transaktioner och hög SQL-prestanda). |
| **Delta Table** | Standardformatet för tabeller i ett Data Lakehouse (bygger på Delta Lake). Lagrar data i Parquet-filer men lägger till en transaktionslogg för ACID-transaktioner och versionshantering (Time Travel). |
| **Lakeflow Jobs** | Databricks inbyggda verktyg för schemaläggning och orkestrering (tidigare Databricks Workflows), som används för att köra och övervaka produktionstasker som notebooks och SQL-frågor. |
| **Spark** (Apache Spark) | En extremt snabb, distribuerad beräkningsmotor med öppen källkod som används för att bearbeta och analysera enorma mängder data parallellt över kluster. |
| **PySpark** | Det officiella Python-biblioteket för Apache Spark, vilket gör det möjligt för Python-utvecklare att skriva Spark-kod med Python-syntax. |
| **Data Intelligence Platform** | En vidareutveckling av lakehouset som integrerar generativ AI och LLMs direkt i dataplattformen för att automatisera datastyrning och möjliggöra analys med naturligt språk. |