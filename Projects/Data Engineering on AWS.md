[course](https://learndataengineering.com/courses/1296952/lectures/29754554)
[code](https://github.com/team-data-science/aws-data-engineering)
[repo](https://github.com/FelitaD/aws_stream_pipeline) 
[README](file:///Users/donor/PycharmProjects/aws_stream_pipeline/README.MD) 
[diagram](file:///Users/donor/PycharmProjects/aws_stream_pipeline/diagrams/AWS_ecommerce_streaming.drawio)

## Dataset

Online Retail Dataset
- original https://archive.ics.uci.edu/ml/datasets/online+retail#
- kaggle https://www.kaggle.com/datasets/carrie1/ecommerce-data

### Defining the purpose

Main goal
- Process transactions
- Give customer access to purchase history
Secondary 
- Average sales
- Most valuable product
- ...

### SQL vs. NoSQL Storage Possibilities

*Relational solution*
Relational storage implies a schema with 3 entities : customer, invoice and items (stock).
Problem is that workload will be a lot of writes with millions of customers for a e-commerce and indexes need to be created all the time, etc.
*Non-relational solutions*
Wide column 

## Platform Design

![[Pasted image 20230303121301.png]]

### Selecting the Tools 

### Client

Simulate a streaming data source that sends e-commerce data as a JSON string.

![[Pasted image 20230303172501.png]]

### Connect

![[Pasted image 20230303172532.png]]

### Buffer

![[Pasted image 20230303172602.png]]

### Process

![[Pasted image 20230303172628.png]]

### Store

Multiple solutions
- S3
- DynamoDB NoSQL
	- Wide Column Store
	- Backend
	- Transactions
- Redshift Data Warehouse
	- Analytics Layer
	- Distributed Storage and Processing

### Visualize

- APIs
	- Access for Apps, UIs...
	- Execute queries and transactions
	- Simple, stateless
- Tableau
	- BI tool
	- Installed locally
	- Connects to Redshift

## Data Pipelines Overview

### Ingestion

A Python client simulates streaming by sending JSON from a CSV file through. 
![[Pasted image 20230303173054.png]]

![[Ingestion.png]]

Lambda functions are exposed through API Gateway
reduire temps d'execution du code reduit couts
![[Pasted image 20230306060106.png]]

### Stream to S3

Use case : putting data in data lake
S3 is very cheap and uses little memory
![[Pasted image 20230303194656.png]]

### Stream to DynamoDB

![[Pasted image 20230303195028.png]]

### Visualization API

![[Pasted image 20230303200312.png]]

### Visualization Redshift Data Warehouse Pipeline

![[Pasted image 20230303200650.png]]
![[Pasted image 20230307175516.png|200]]

### Batch Processing Pipeline

![[Pasted image 20230303201526.png]]

## AWS Basics

### Things to keep in mind

- Not all services are available under the free tier
- Stop containers and EC2 instances as soon as possible
- Kinesis streams and DynamoDB tables cost even if you are not running
- Limit DynamoDB read and write capacity as much as possible (this is where costs are)
- Lambda standard does 10k retries (limit that)
- Watch out for auto scaling
- Add all services to the same region (convenience)

### IAM Identity & Access Management

Roles and policies

### Logging

Cloudwatch

### AWS Python API Boto3

Boto3 AWS SDK to access all AWS resources : S3, DynamoDB, IAM, Glue...
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html


