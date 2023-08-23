### Traditional teams

- Data Analysts : knows what to build, closer to business
	- Reports
	- Dashboards
	- SQL, Excel
- Data Engineer : knows how to build the infrastructure
	- Python, SQL
	- ETL
	- Orchestration

### ETL to ELT

ELT in (cloud-based) data warehouses has transformed the work of data teams with:
- scalable compute
- scalable storage
- reduction of transfer time
### Analytics Engineer

Owns the transformation of raw data up to the BI layer.

Changes the data team's focus:
- Analytics engineers focus on the transformation of raw data into transformed data that is ready for analysis. This new role on the data team changes the responsibilities of data engineers and data analysts.
- Data engineers can focus on larger data architecture and the EL in ELT.
- Data analysts can focus on insight and dashboard work using the transformed data.
- Note: At a small company, a data team of one may own all three of these roles and responsibilities. As your team grows, the lines between these roles will remain blurry.

https://www.getdbt.com/what-is-analytics-engineering/

"the person who curates an organization’s data and acts as a resource who wants to make use of it" 
"the analytics engineer is a steward of organizational knowledge, not a researcher answering a specific question"

### Main functionalities

dbt connects directly to the data platform to model the data.

DAG

dbt build
dbt run
dbt test
dbt docs generate

Lineage graph of models

Deployment environment with jobs

YAML files used to
- know a directory is a dbt project 
- generic tests
