---
tags: tech
aliases: [Apache Parquet]
publish: true
sr-due: 2022-10-08
sr-interval: 2
sr-ease: 247
---

File format designed for efficient data storage and retrieval

1. Columnar
![[Pasted image 20220831154006.png]]
2. Open-source
Compatible with most [[Hadoop]] processing frameworks.

3. Self-describing
Metadata contains schema + structure

![[Pasted image 20220831155843.png]]

Not text / non human readable
2x faster to unload
6x less storage in S3 compared to text format

https://www.upsolver.com/blog/apache-parquet-why-use