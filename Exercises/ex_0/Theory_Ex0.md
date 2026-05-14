# Ex 0 - 4. Theory Questions

####   a) Why enterprises are moving from on-premises to cloud IT infrastructure?

- Lägre kostnader: Slipper köpa och underhålla egen hårdvara
- Skalbarhet: Kan enkelt öka/minska resurser efter behov
- Flexibilitet: Snabb åtkomst från var som helst
- Automatiska uppdateringar: Leverantören sköter säkerhet och underhåll
- Pay-as-you-go: Betalar bara för det du använder

#### Källor: 
[Azure Microsoft](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-cloud-migration)

[AWS Cloud Migration](https://aws.amazon.com/migration-and-modernization/)


####   b) What are different layers in medallion architecture in Databricks?

- Bronze (rådata): Data kopieras in exakt som den är från källan
- Silver (rensat): Data städas, valideras och struktureras
- Gold (aggregerat): Färdig business-data för rapporter och analytics

![Medallion Architecture](https://docs.databricks.com/aws/en/assets/images/medallion-architecture-15e2d57ad70d28b1701dda4f7271d862.png)

#### Källor:
[Databricks officiella dokumentation](https://docs.databricks.com/en/lakehouse/medallion.html)

####   c) Are big data and cloud the same concept? Explain your thoughts in details.

**Nej, olika koncept:**
- Big Data = Stora mängder data (volym, hastighet, variation) som kräver speciella verktyg för att analysera
- Cloud = Leveransmodell där IT-resurser tillhandahålls via internet
- Relation: Cloud är ett verktyg för att hantera big data, men big data kan också hanteras on-premises. Cloud gör big data mer tillgängligt för företag tack vare elastisk skalning.

#### Källor:
[IBM Big Data vs Cloud](https://www.ibm.com/topics/big-data)

[Oracle Cloud Computing](https://www.oracle.com/cloud/what-is-cloud-computing/)

####   d) Are unity catalog and catalog the same thing in Databricks?

**Inte exakt samma:**
- Unity Catalog: Databricks moderna governance-lösning för hela organisationen (centraliserad säkerhet, metadata management)
- Catalog: En "behållare" för databaser och tabeller (kan finnas både i Unity Catalog och äldre Hive metastore)

#### Källor: 
[Databricks Unity Catalog dokumentation](https://docs.databricks.com/en/data-governance/unity-catalog/index.html)

[Unity Catalog Best Practices](https://docs.databricks.com/en/data-governance/unity-catalog/best-practices.html)

####   e) In Databricks free edition account, where are your data stored?

- I Databricks-managed cloud storage (AWS S3 eller Azure Blob Storage beroende på region). Du har begränsad kontroll - data lagras i Databricks infrastruktur, inte ditt eget storage-konto.
- OBS: Community Edition är för lärande, inte produktion!

####Källor:
[Databricks Community Edition FAQ](https://docs.databricks.com/en/getting-started/community-edition.html)

[Databricks Free Trial dokumentation](https://www.databricks.com/product/faq/community-edition)

####   f) When is it preferred to use SQL vs PySpark for SDP?

**Använd SQL:**
- Enkla queries och aggregeringar
- Teamet är bekväma med SQL
- Standard datawarehouse-operationer
- Snabbare för ad-hoc analys

**Använd PySpark när:**
- Komplex data transformation
- Behöver Python-bibliotek (ML, custom logic)
- Programmatisk kontroll och loops
- Integrering med Python-workflows

#### Källor:
[Databricks SQL documentation](https://docs.databricks.com/en/sql/index.html)

[PySpark vs SQL comparison](https://docs.databricks.com/en/languages/index.html)




