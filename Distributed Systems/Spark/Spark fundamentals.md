---
tags: tech
aliases:
publish: true
sr-due: 2022-11-17
sr-interval: 27
sr-ease: 240
---

> Spark works on memory of the nodes -> best if data stays distributed on these nodes (actions) and bad if the data is sent to the driver (disk) where there is risk of overpowering

## What Spark is good for ?
- Batch processing of huge datasets due to horizontal scaling
- Stream processing
- Integrates strongly with Hadoop (good for running on premise)

Typical input types
- CSV
- JSON
- Parquet
- Hadoop
- ODBC connections (database)
- REST calls
- S3, Cloud storage..
- Kafka, Kinesis..

Spark leverages the **memory** which is bigger than hard drives. 
Every transformation works with data on memory -> stupid fast.

## How it works
![[Pasted image 20220624125538.png]]

#### Components
- **Executor** : on each node, runs the tasks
- **Driver** : schedules the tasks for the executor
- **Spark Context** : main entrypoint
- **Cluster Manager** : manages ressources, manage executor on each node, CPU, how many tasks can be executed on the node

#### Cluster (manager) types
- **Standalone** : has its own cluster manager that comes with Spark
- **Hadoop YARN** : YARN is yet another ressource negotiator, can replace Spark's manager
- **Kubernetes** : manager for deploying containerized applications
- Apache Mesos

#### (Driver) deployment
- **Client deployment** : driver lives inside the client, quits with the client
- **Cluster deployment** : driver lives inside the YARN manager (Spark Application Master), independant from the application
[How it works in details](https://learndataengineering.com/courses/1296953/lectures/29753113)

#### Where to run Spark
On premise
	- Standalone 
	- Hadoop

Cloud (easier to setup)
	- AWS EMR / Glue
	- Google Cloud Dataproc
	- Azure HDInsight

## Spark coding basics

### Resilient Distributed Datasets
- Immutable
- Good for unstructured data
- Parallelized
- Work like arrays
- Low level (no optimization)
- RDD <-> DataFrame
- `map()`
- `reduce()`
- `foreachpartition()`

### DataFrames
- Immutable
- Good for structured data
- New DataFrames created through transformation

### Transformations & Actions

>**Transformations** create a new DataFrame
>- Lazy execution : not happening immediately
>- Schema is defined eagerly : happens immediately
> 
>**Actions** triggers the transformation
>- Creates outputs
>- Executed eagerly
>
 **Query** : transformation + action

#### Transformations
- Executed on the executors in parallel
- Do not return data back to the driver (data stays distributed)
- Schema of the new DataFrame can be changed (data stays distributed)

Typical transformations
- `select`
- `where`
- `join`
- `orderBy`

#### Actions
Execute the processing.

Actions that writes DataFrame to a storage on the executors (**good**)
	- `write` 
		- writes a part on disk for each node
		- writes on local disk / S3 / HDFS...

Actions that send back data to the driver (**bad** because Spark works on memory -> risk of overpowering)
	- `count`
	- `first`
	- `take(n)` (best for counting)
	- `show`
	- `collect`

## Hands On
### Course data & Environment
- [Jupyter Docker Container](https://hub.docker.com/r/jupyter/pyspark-notebook) : 
	- to run Spark in local mode and code dynamically
	- Jupyter Notebook Python, Spark, Mesos Stack from https://github.com/jupyter/docker-stacks
- Dataset : [content of the data engineering cookbook](https://github.com/team-data-science/learning-apache-spark/tree/main/data)

### Notebooks
[JSON Transformations](file:///Users/donor/Docker/learning-apache-spark/sources/01_JSON_Transformations.ipynb)
[CSV Schemas](file:///Users/donor/Docker/learning-apache-spark/sources/02_CSV_Schemas.ipynb)


