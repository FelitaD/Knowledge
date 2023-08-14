---
tags: tech
aliases:
publish: true
sr-due: 2022-10-24
sr-interval: 11
sr-ease: 250
---

Connecting or ingesting is getting data from the source and making it available to later stages.

Data source -*send*-> API -*push*-> temporary storage <-*simple and fast access*- other stages

A good practice is that the temporary storage follows a [[pub-sub]] pattern :

Data source -*send*-> API -*publish*-> [[message queues]] <-*consume*- analytics

Use of [[messaging queue]] systems like Apache Kafka, RabbitMQ or AWS Kinesis, also [[caches]] for specialised applications like Redis.
