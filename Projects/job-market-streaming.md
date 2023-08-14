---
tags: tech/data_engineering/projects
aliases:
publish: true
sr-due: 2022-11-06
sr-interval: 24
sr-ease: 261
---

# Architecture micro-services
```
job-market-streaming
|-- api-ingest
| |- crawler
| |- Dockerfile
| |_ requirements.txt
|-- kafka
|-- jupyter-pyspark
|__ docker-compose.yaml
```
# Roadmap
##### Project setup
- [x] Comprendre [[Platform blueprint]]
- [x] Miro : reproduire roadmap de job_market à partir de document streaming
- [x] Rédiger [README](https://github.com/team-data-science/WeeklyMeetup/tree/main/Project-Documentation) 

##### Connect & Buffer 
- [x] Réviser Docker
- [x] Setup [[Kafka]] and Zookeeper containers with [[Docker]]
- [x] Setup ingestion-topic
- [x] Setup local consumer to test topic receives messages
- [x] Produce kafka string in Python script
- [x] Add Scrapy ingest-API 
- [x] Create Kafka pipeline
- [x] Test pushing messages to Kafka container
- [x] Add all spiders (chromium needed)  
- [x] Build api_ingest image
- [x] Test running container
- [x] Modify docker-compose
- [x] Publish messages to kafka

##### Analytics

Same as done with Python in [[job-market-batch]] but with [[Spark]].

- Learn [[Spark fundamentals]] fundamentals  
- Analytics goals  
	- Consume data  
		- Retrieve raw data (kafka message) into a (spark) dataframe  
		- Limit length of data for testing  
		- Print dataframe  
	- Data processing  
		- Convert types  
		- Add `created_at` column  
		- Replace missing/wrong values in `remote` column  
		- Process `title` column  
			- Remove genders  
			- Remove special characters  
		- Create `language` column  
		- Remove jobs not in english or french  
		- Process `text` column  
			- Remove new lines at beginning  
			- Remove \\xa0  
			- Remove excess new lines in the body  
		- Add `technos` column  

##### Storage

##### Visualization

##### Make data-driven decisions
- Find most interesting jobs  
