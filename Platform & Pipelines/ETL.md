---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-14
sr-interval: 1
sr-ease: 228
---

**ETL** is a process that extracts the data from different RDBMS source systems, then transforms the data (like applying calculations, concatenations, etc.) and finally loads the data into the Data Warehouse system. **ETL stands for Extract-Transform-Load** and it is a process of how data is loaded from the source system to the data warehouse. Data is extracted from an OLTP database, transformed to match the data warehouse schema and loaded into the data warehouse database.

## What Is ETL Architecture?

ETL architecture is a ‘master plan’ defining the ways in which your ETL processes will be implemented from beginning to end. This wires a portrayal of the methods in which the data will move from the source to the target areas, in addition to the transformation list that will be executed on this data.

ETL architecture revolves around the three fundamental steps:

-   **Extract**. The initial step is the extraction of data, during which the data is explicitly identified and is drawn out from several internal as well as external sources. Database tables, pipe, files, spreadsheets, relational and non-relational databases may include amongst some of these data sources.
-   **Transform**. The next step involves transformation. Once the data is extracted, it must be transformed into a suitable format and should be transported physically to the target data warehouse. This transformation of data may include cleansing, joining and sorting data.
-   **Load**. The final step is to load the transformed data into the target destination. This target destination may be a data warehouse or a database. Once the data is loaded to the data warehouse, it can be queried precisely and utilized for analytics and business intelligence.

## 12 Best Practices for ETL Architecture

### 1. Understand Your Organizational Requirements

- Usage and latency
If volume of extracted data from both ends is high, traditional RDBMS may be a bottleneck.
- Compatibility with other tools
- Management overhead
- ...

### 2. Audit Your Data Sources

- Assessing quality and relevance of data
- Key metrics
- Quantity

### 3. Determine Your Approach to Data Extraction

### 4. Identify changes

Provide notifications and/or show the changes that are made after an extraction occurs.

"It is critical to remember the data extraction frequency while using Full or Delta Extract for loads."
> Full load processing means that the entire amount of data is imported iteratively the first time a data source is loaded into the data studio. Delta processing, on the other hand, means loading the data incrementally, loading the source data at specific pre-established intervals.

### 5. Build Your Cleansing Machinery

- Use normalized data or convert it to [[3rd normal form]]

### 6. ETL Logs Are Important


### 7. Resolving Data Errors



### 8. Recovery Point



### 9. Build Code Modules


### 10. Staging Area


### 11. Error Alert Task


### 12. Enhancing ETL Solution


****
[ETL Best practices](https://blog.skyvia.com/etl-architecture-best-practices/)
