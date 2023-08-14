---
tags: tech/databases
aliases:
publish: true
sr-due: 2022-10-12
sr-interval: 4
sr-ease: 209
---
|                     | [[Relational databases]]                                                                                                                               | [[NoSQL databases]]                                                                                                                                                                                                                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Optimal workloads   | Conçues pour OLTP, bonnes pour OLAP.                                                                                                                   | Conçues pour applications faible [[latence]] et [[Semi-structured data]]                                                                                                                                                                                                                                                                |
| [[Data modeling]]   | [[Normal forms]]  of the data in tables. Schéma définit strictement tables, colonnes, index, relations etc. Enforces [[Referential Integrity]]        | Many data models (key-value, document, graph...) optimised for performance and [[Scalability]].                                                                                                                                                                                                                                         |
| [[ACID]] properties | Yes                                                                                                                                                    | NoSQL databases often make tradeoffs by relaxing some of the ACID properties of relational databases for a more flexible data model that can scale horizontally. This makes NoSQL databases an excellent choice for high throughput, low-latency use cases that need to scale horizontally beyond the limitations of a single instance. |
| Performances        | Performances depend generally on disk subsystem. Query optimisation of [[Indexes]] and data distribution is necessary to achieve peak performance. | Performances depend generally on the cluster size, network latency and application.                                                                                                                                                                                                                                                     |
| [[Scalability]]     | Vertical scaling or horizontal scaling by adding replicas for read only workload.                                                                      | Scale easily due to [[Distributed systems\|distributed architecture]].                                                                                                                                                                                                                                                                                           |
| API                 | [[SQL Fundamentals]]                                                                                                                                                | Clés de partition permettent de rechercher key-value pairs, colonnes, documents semi-structurés...                                                                                                                                                                                                                                      |

**Comparaison des terminologies**
| SQL                    | [[MongoDB]]           | DynamoDB               | [[Cassandra]]         | Couchbase   |
| ---------------------- | ----------------- | ---------------------- | ----------------- | ----------- |
| Table                  | Collection        | Table                  | Table             | Data Bucket |
| Row                    | Document          | Element                | Row               | Document    |
| Column                 | Field             | Attribute              | Column            | Field       |
| Primary Key            | ObjectId          | Primary Key            | Primary Key       | Document ID |
| Index                  | Index             | Secondary Index        | Index             | Index       |
| View                   | View              | Global secondary index | Materialized view | View        |
| Nested table or object | Embedded document | Map                    | Map               | Map         |
| Array                  | Array             | List                   | List              | List        |

****
https://aws.amazon.com/nosql/?nc1=h_ls
