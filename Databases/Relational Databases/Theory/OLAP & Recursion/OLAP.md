---
tags: tech/databases, stanford
aliases:
---

# Introduction

## [[OLTP vs OLAP]]

Overall, database activity can be divided into two broad classes. One of them, the traditional one, is known as OLTP, or online transaction processing. The other one, the subject of this video, came about more recently, and it's known as OLAP, or online analytical processing. 
### OLTP
Online transaction processing is typically characterized by short transactions, both queries and updates. Things like updating an account balance in a bank database or logging a page view in a web application. Queries in OLTP databases are generally fairly simple. Find an account balance or find the GPA of a student. They typically touch small portions of the data. And updates in this environment can be frequent. We might be making airline seat reservations or updating an online shopping cart. 
### OLAP
OLAP is pretty much the opposite in all respects. In OLAP, we have long transactions, often complex analysis of the data or data mining type operations. The queries as I said, can be complex and especially they often touch large portions of the data rather than small portions as in OLTP. And updates in the OLAP environment tend to be infrequent, in fact, sometimes in the OLAP environment there are no updates to the data at all. 
Now, these two are extremes and really there is a spectrum between those two extremes. We might have a sort of, moderate amount of update and queries that touch a moderate portion of the data. But the fact is that database systems traditionally were designed for the first extreme. And then special techniques were developed for the other extreme. So the systems are tuned for the two extremes. And depending on ones work load one might choose to use different options in a database system. 

## [[Data Warehouses]]

There's a concept called data warehousing. It's really a software architecture. The idea is that often in enterprises or other operation, there are lots of operational sources. So you can think of a point of sale, for example, might have many, many OLTP database pieces related to an enterprise, and data warehousing is the process of bringing the data from all of those distributed OLTP sources into a single, gigantic warehouse where the point then is to do analyses of the data, and that would fall under the OLAP camp. 

## Decision support system

Also known as DSS. This isn't really an exact term. It's generally used to talk about infrastructure for again large scale data analyses. So, if you think of a data warehouse, where we're bringing in a lot of data from operational sources, and that warehouse is tuned for OLAP queries that would be thought of as a decision support system. And, of course, this system is designed to support decisions that are made, again, based on data analysis. 

## Star schema

Frequently applications that are doing OLAP are designed based around a star schema, so it's a certain type of relational schema. 
### Fact table
In a star schema, there's usually one fact table. That will be a typically very large table, it will be updated frequently. Often it's actually append only, so there are only inserts into the fact table. 
### Dimensions tables
And then there are maybe many dimension tables. Those are updated infrequently and don't tend to be as large. So examples of a fact table might be sales transactions in a sales database or in a university database, maybe students enrolling in courses or in a web application logging the page views. 
In all of these cases we can see that the fact table can be very large and can be append only, so inserts only. Examples of dimension tables might be in a sales database store's items and customers in a college enrollment database. Maybe students and courses in a web application. Maybe web pages users and advertisers. So, you can see, that these are generally smaller tables, they're more stable, they're not updated as frequently. You can sort of think of dimension tables as things in the real world and then fact tables as logging things that happened. It's not always divided this way but, it's not a bad approximation. 
Now, you might be wondering why is it called a star schema and it's called that because we have the fact table sort of, centrally referencing dimension tables around it. We have our central fact table, the sales table. And we can see that the sales table contains these three columns I've abbreviated them in the picture: the Store ID, Item ID, and the Customer ID. So if you look at this squinting, you will see that it is kind of a star schema with the central fact table pointing to the dimension tables around it, and that's where the name comes from. 
### Dimension attributes
These three are what are known as dimension attributes. So those are the attributes that are foreign keys into the dimension tables. 
### Dependent attributes
Then the remaining attributes in this case the quantity and the price are called dependent attributes. So they're I guess dependent on the values for the dimension attributes and typically, queries will tend to aggregate on the dependent attributes. 

## OLAP queries

So, now that we known what a star schema looks like, let's look at the type of queries that are generally issued over this schema, and they're called OLAP queries. 
### Join
Typically a query over a star schema will first join some or all of the relations. And when you're joining the sale as the fact table with the dimension tables, you can almost think of it as expanding the facts in the sales table to include more information about the sales. Since we have the foreign keys we'll be adding, for example, to the information about a sale. More about the store. The city and state of the store. For a sale item will be adding the category brand and so on. So that's the join process and the query will join as much as it needs in order to do the rest of it's work. 
### Filter
It might then filter the data. For example we might decide that in our query we only care about stores in California or customers in California, we're only interested in shirts and so on. So they can filter on the dimension attributes after joining, or could filter on the price or quantity as well. 
### Group by and aggregate
After filtering there's often a group by and an aggregation. So we might decide that we're interested in figuring out our total sales divided by customer or by item or by state or all of those. And then the aggregation might sum up the sales or it might determine the average price that's sold. 

## Performance issues

So if you think about executing queries of this type, they can be quite complex and they can touch large portions of the database.
### Special indexing techniques
Running this type of query on a gigantic database over a standard database system can be very slow, but over the past decade or so, special indexing techniques have been introduced and special query processing techniques specifically to handle this type of query on star schemas on large databases. And again, by large, just think about the number of sales, for example, in a large retail chain, or a number of web views, or even shopping cart additions in a large online vendor. So, in all of those applications, people are interested in doing OLAP queries and they tend to use a system that supports these special techniques.
### Materialized views
Another component of getting good performance in these systems is the use of materialized views. You might remember that materialized views are useful when we have a workload that consists of lots of queries and not so many updates. And that's exactly the type of workload we have in OLAP. Furthermore, we have many queries that take roughly the same structure so materialized views are useful in that setting as well. 

## Data cubes

Now let me switch gears and introduce a different way of looking at the data in these OLAP applications with star schemas, and it's what's known as a data cube. Sometimes this is also called multidimensional OLAP and the basic idea is that when we have data with dimensions, we can think of those dimensions as forming the axis of a cube. It's kind of like an N dimensional spreadsheet. Now we can have any number of dimensions, but for the examples I'm gonna give, the best I can draw is up to three dimensions, and that's why people call it a cube. 
So we have our dimensions forming the axis of our cube. And then the cells of the cube, again, you can think of it sort of like cells of a spreadsheet. Are the fact data. Or the dependent data. And finally we have aggregated data on the sides, edges and corners of corner of the cube. Again similar to how you might aggregate columns in a spreadsheet.  
### Entries inside the cube
The idea is that every cell in the cube, so every combination of item, costumer, and store has a cell in the cube, so this would be sort of a free floating cell here. So now on the faces, edges, and corner of the cube are going to have aggregated data. And there does need to be with each data cube a predefined aggregate. So this will be the aggregate over all items for that particular store and customer. And we'd have similar values on the other faces of the cube. 
### Entries on the edges
Now let's talk about what's on the edge of the cube. So here we have, say for store 3, we'll have the aggregate value over all customers and items in this point for store 3. So that will be the total sales that we conducted at store S3. Over here on this edge we'd have the total for a specific costumer and over here for specific items. 
### Entries at the corner
And then finally, we have at the corner of the cube the full aggregation. So that's going to be in this case the sum of the quantity times price for every store, customer and item. 

## Fact table uniqueness

So as we saw in the cube, we have one cell in the cube for each combination of store ID, item ID, and customer ID. So if those three together form a key, then it's very straight forward. If the dimension attributes together don't form a key then we might be pre-aggregating already inside the data cube. So, we might decide to already have say the sum of quantity times price for each combination of store item and customer. 
Another possibility and it's done quite commonly is to add to the fact table the attribute date, or even the time. And that can be used to create a key. Typically, we won't have two transactions at exactly the same time. Now if we do have an attribute here called date, one might wonder is that a dimension attribute or a dependent attribute. Actually, it's pretty much a dimension attribute because we're gonna use it as another dimension in our data cube, but the difference being that we would not have an actual dimension table listing the dates. 

## Slicing and dicing

### Slice
So, the idea of a slicing query is a query that analyzes a slice of the cube and it does that by constraining one of the dimensions. For eg. let's only consider sales that are from the state of Washington.
### Dice
Constrain by another dimension. Subset of the slice. For eg. sales of items only in Washington and in the color red.

## Roll up and drill down

Now let's move on to a couple other concepts in the OLAP world called drill down and roll up. 
### Drill down
The idea of drill down, is that we may be examining summary data and then we want to get more information. Drill down into the details of that data. 
So, to drill down what we do is add a grouping attribute. So if we added, for example, category, when we add another grouping attribute, that gets us more data in the answer - more detail in our data. 
### Roll up
Rollup is exactly the opposite. Rollup says we're looking at data and we decide we have too much detail and we want to summarize. And summarize is simply a matter of removing a group by attributes. So if we took out state, then now we'll only see our data summarized by brand rather than broken out into state and brand. 

## SQL constructs

And lastly, I want to introduce some SQL constructs. These are constructs that have been added, fairly recently, to the SQL standard in order to perform OLAP queries. 
The constructs are called with cube and with roll up and they're added to the group by clause. 
- `WITH CUBE`
When we add `WITH CUBE` to a query with a `GROUP BY` what happens is that, basically, we're adding to the result of our query, the faces, edges, and corner of the cube. Using no values for the attributes that we're not constraining. 
- `WITH ROLLUP`
With Rollup is similar to With Cube, except it's smaller. It actually is a portion of the data cube, and that makes sense when we have dimensions that are inherently hierarchical. 

![[Pasted image 20230128161728.png|300]]




So, we can conclude there are two broad types of data base activity, online transaction processing. Short, simple transactions touching small portions of the data, lots of updating and OLAP, or online analytical processing, where we have complex queries, long transactions, might touch a large portion of the data and might not update the data at all. For online analytical processing OLAP we saw that star schemas are frequently used. We saw how to view the data as a data cube. Of course, that can be in any number of dimensions. We just use three for visualization. There are two new constructs in SQL: With Cube and With Rollup. And finally this type of query can be very stressful on a database system when we have very large databases. So special techniques have been introduced into systems to help perform these queries efficiently.

## Demo

We saw Star Schema and we saw plain SQL queries over that schema. We saw the concept of drilling down and rolling up; also slicing and dicing. We introduced a WITH CUBE extension to SQL, which is not yet implemented in MySQL, but we were able to write a query that's equivalent to WITH CUBE. We also saw putting a WITH CUBE query into a table and then querying that table directly and that can be much more efficient than running the equivalent query in SQL directly over the fact table. We also saw WITH ROLLUP, which is implemented. We didn't demonstrate putting the result of WITH ROLLUP in a table, but we could certainly do that too. **All of these features are useful primarily in applications that are performing analyses over very large data sets that exhibit this dimensional type structure, but this is actually quite a common structure in analysis applications** 

![[asset-v1_StanfordOnline+SOE.YDB-OLAP_RECURSION0001+2T2020+type@asset+block@OLAPIntro.pdf]]