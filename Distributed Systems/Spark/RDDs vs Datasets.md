---
tags:
- tech
aliases:
publish: true
sr-due: 2022-10-14
sr-interval: 6
sr-ease: 190
---

Before Spark 2.0, the main programming interface of Spark was the Resilient Distributed Dataset (**RDD**).  After Spark 2.0, RDDs are replaced by **Dataset**, which is strongly-typed like an RDD, but with richer optimizations under the hood. 

The RDD interface is still supported, and you can get a more detailed reference at the [RDD programming guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html). However, we highly recommend you to switch to use Dataset, which has better performance than RDD.

Spark’s primary abstraction is a distributed collection of items called a [[Dataset]]. Datasets can be created from Hadoop InputFormats (such as HDFS files) or by transforming other Datasets. Due to Python’s dynamic nature, we don’t need the Dataset to be strongly [[Typed language|typed]]. 

> As a result, all Datasets in Python are Dataset[Row], and we call it `DataFrame` to be consistent with the data frame concept in Pandas and R.
