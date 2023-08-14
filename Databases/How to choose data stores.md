---
tags: 
- tech/databases
- interview
aliases:
publish: true
sr-due: 2022-10-14
sr-interval: 1
sr-ease: 210
---

```ad-summary
 -   Generate a (rough) relational database design of your data
	-   find out the problems in querying data / sending data in
	-   which pb want to relieve
-   Look into the documentation of each database
-   Find out schema design with your data for the database
-   How to write and query data
	-   does it fit with the write / read (sequential / random)
-   Compatible visualizations and processing frameworks
	-   probably just after the schema design
-   Google for use-cases on Slideshare or Medium
-   Set up a test instance  
```

First of all to understand this better look at the [[Schema Design Data Stores]] course where there are examples. 

Before you start selecting a datastore (databases) you have to think about your data. 
- How do I store the data and
- which is often even more important, how do I query it? 

This will help you define your access patterns. 

You need to get to your data efficiently which implies having the right database system and the right design 

After you have the access patterns I recommend you generate a relational database design (ER model). 

If you are not sure about ER model then look into the fundamentals course or the schema design. 

Find out where are the problems with using a relational database if you put your data in and use your access patterns. 

You want to make sure that you only use NoSQL if it’s really necessary. 

If you found out that relational databases are not the right solution then search for alternatives ( the next videos will show you the different options. You can also go into [db-engines.com](http://db-engines.com/), look at the different types and search for a database. For every candidate go through the documentation of the database. 

How does the schema design (data modeling) work in this store. 

Does that fit to your access patterns and, well, basically what you want to do? If yes I recommend you look into compatibilities with other tools. 

Your db will not be the only tool in your platform. 
- Does it fit to your visualizations (can they connect to your db) 
- does your processing framework work with the db (sometimes you can only do rudimentary things in case you use Spark instead of the Python client for instance) 

It’s also a good idea to search Medium, Slideshare or just Google for use-cases where people used that database If all that fits then create a database schema for that chosen database with your data. 
(Keep the access patterns for read and write in mind!) 

Once you have that and you are happy try it out in a dev environment.

****
source: Andreas Kretz