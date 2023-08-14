
If inherit from a data pipeline that has no tests.

### 1. End-to-end tests

First ensure end-to-end testing so that can add new features and verify the end result stays the same.
In practice, take sample data and compare output with an expected output.

### 2. Data quality testing

Difference with end-to-end test is that it runs each time the pipeline runs.
It adds tasks to the pipeline itself like loading in a staging table and task to check constraints.
[[dbt]] and [[great expectations]] have functionality to make these checks easily.
Can add quality testing right after each transformation to catch errors earlier.

### 3. Monitoring and alerting

*Monitoring*
Add checks of data size in the pipeline. Send logs to service like [[datadog]], [[newrelic]] or a database with [[looker]] / [[Metabase]] to alert when unexpected changes in data size (eg. count of rows before and after transformation).
*Alerting*
Catch out-of-memory errors, file not found, etc. Set up notification of pipeline breakage via slack or email from datadog or newrelic.

### 4. Unit and contract testing

Functions that interact with external systems such as API call to microservice or vendor.

****
*Resources*

https://www.startdataengineering.com/post/how-to-add-tests-to-your-data-pipeline/
https://medium.com/slalom-build/the-challenge-of-testing-data-pipelines-4450744a84f1