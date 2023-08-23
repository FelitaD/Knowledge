- Explain why testing is crucial for analytics.
- Explain the role of testing in analytics engineering.
- Configure and run generic tests in dbt.
- Write, configure, and run singular tests in dbt.

Improving data reliability
https://www.youtube.com/watch?v=M_cNspn2XsE&ab_channel=dbt

Run tests in development
Schedule tests in production

### Singular tests

### Generic tests

4 types:
- unique
- not_null
- accepted_values
- relationships

### Additional tests

Can be imported through packages or write custom generic tests

### Running the tests

`dbt run --select stg_job_postings`
`dbt test --select source:job_postings`

### dbt build

Allows tests to happen directly after a model runs in the DAG

Test everything upstream of a model:
`dbt build --select +model_name`

