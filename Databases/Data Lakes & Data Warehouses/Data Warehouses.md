---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-18
sr-interval: 8
sr-ease: 190
---

Data Warehousing **integrates data and information collected from various sources into one comprehensive database**. For example, a data warehouse might combine customer information from an organization's point-of-sale systems, its mailing lists, website, and comment cards.

Data warehouses are a type of data management system generally used for analytical insight and connected to BI tools for visualization.
It can also act as an organisational layer for a [[Data Lakes|data lake]].

-   Tabular structure makes them easy to use (SQL & joins)
-   [Star](https://www.guru99.com/star-snowflake-data-warehousing.html), snowflake and galaxy schema
-   Dimensional modeling with dimensional and facts tables
-   Often no “transactions” and have [[ACID]] tradeoffs (need processing to make sure everything is in)
-   Not used for [[OLTP]]

-   The top cloud data warehouses at a glance - Amazon Redshift, Microsoft Azure Synapse Analytics, Google BigQuery, and Snowflake Cloud Data Platform.

So you can think of a point of sale, for example, might have many, many OLTP database pieces related to an enterprise, and data warehousing is the process of bringing the data from all of those distributed OLTP sources into a single, gigantic warehouse where the point then is to do analyses of the data, and that would fall under the OLAP camp.

DSS
This isn't really an exact term. It's generally used to talk about infrastructure for again large scale data analyses.
So, if you think of a data warehouse, where we're bringing in a lot of data from operational sources, and that warehouse is tuned for OLAP queries that would be thought of as a decision support system.

Has a [[Star schema]]
