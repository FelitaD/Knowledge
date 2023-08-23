- Explain what models are in a dbt project.
- Build your first dbt model.
- Explain how to apply modularity to analytics with dbt.
- Modularize your project with the ref function.
- Review a brief history of modeling paradigms.
- Identify common naming conventions for tables.
- Reorganize your project with subfolders.

Models shape raw data to finally transformed
Models are SQL select statements
Each model has a one-to-one relationship with a table/ view in the data warehouse (most of the time)

to build a selected model:
`dbt run --select model_name`

to create a view or a table:
`{{ config ( materialized="table" )}}`

### Modularity

Build the product piece by piece
#### CTE

In a formal sense, a Common Table Expression (CTE), is a temporary result set that can be used in a SQL query. You can use CTEs to break up complex queries into simpler blocks of code that can connect and build on each other. In a less formal, more human-sense, you can think of a CTE as a separate, smaller query within the larger query you’re building up. Creating a CTE is essentially like making a temporary [view](https://docs.getdbt.com/terms/view) that you can access throughout the rest of the query you are writing.
There are two-types of CTEs: recursive and non-recursive.

#### ref function

Pull from another model

stg_customers.sql
```sql
with customers as ( 
	select id as customer_id, first_name, last_name 
	from raw.jaffle_shop.customers 
) 
select * from customers
```

```sql
with customers as ( select * from {{ ref('stg_customers')}} ),
```

### Data Modeling

Traditional modeling techniques (normalized modeling):
- Star Schema
- Kimball
- Data Vault 

Denormalized modeling:
- ad hoc analytics
- agile analytics

### Sources

#### Naming conventions

Sources:
- raw loaded data

Staged:
- light touched transformation (renaming column...)
- clean and standardized
- one to one with source tables

Intermediate:
- built on staging models

Fact:
- things are occurring or have already accured (clicks, events, votes...)

Dimension:
- things that exist (people, place, user, company, products...)

![[Pasted image 20230822135028.png]]

