#!/bin/bash

docker run -it --rm \
--name spark_streaming \
-v ~/Users/donor/PycharmProjects/Spark/spark_streaming:/home/jovyan/work \
-p 8888:8888 jupyter/pyspark-notebook