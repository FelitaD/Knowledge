---
tags:
- tech
aliases: [programmation parallèle, parallel computation]
publish: true
sr-due: 2022-10-07
sr-interval: 2
sr-ease: 230
---

Parallel computing is the basis of modern data processing tools.

It is necessary due to memory limitations and processing power.
It works by splititng up tasks into smaller subtasks and distribute them over several computers.

![[Pasted image 20221004234207.png]]

|     | Pros                    | Cons                      |
| --- | ----------------------- | ------------------------- |
|     | Extra processing power  | Moving data incurs a cost |
|     | Reduced memory fooprint | Communication time                          |

Parallel computing, although incredibly efficient and powerful, is not a magic tool solving all the data engineering processing challenges, and can actually be overkill. It incurs a cost in that data has to be moved to the processor. Also, the time taken to move data can sometimes outweigh the time saved by doing computations in parallel. The two scenarios where this tends to occur are when transporting data is slow (imagine if the sales assitants folding t shirts worked in different buildings), or when the computation is trivial.

## Parallel computation frameworks


See [[Distributed systems]].

- Apache [[Hadoop]]
- [[Spark]] : tries to keep as much computation in memory. It relies on RDDs (list of tuples). We can transform data with map or filter.
- [[PySpark]] : Python interface, dataframe abstraction.

```python
<class 'pyspark.sql.dataframe.DataFrame'> 

df.printSchema() df.groupBy('Year').mean('Age') df.groupBy('Year').mean('Age').show()

# Running Spark files
spark-submit \ 
	--master local[4] \
		/home/repl/spark-script.py
```