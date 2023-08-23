### clickhouse: postgres table -> parquet
```
./clickhouse local -q "SELECT id, url, title, company, location, type, industry, remote, text FROM   
	postgresql(  
	'localhost:5432',  
	'job_market',  
	'raw_jobs',  
	'user',  
	'pwd'  
)  
INTO OUTFILE 'raw_jobs.parquet'"
```

### snowflake: create file format
```
CREATE or REPLACE FILE FORMAT raw_jobs_format
TYPE = parquet
USE_LOGICAL_TYPE = TRUE;
```

### snowflake: create internal named stage
```
CREATE OR REPLACE STAGE raw_jobs_stage
COPY_OPTIONS = (on_error='skip_file')
FILE_FORMAT = (FORMAT_NAME = raw_jobs_format);
```

### snowsql: upload local file to stage
```
PUT file:///Users/donor/raw_jobs.csv @raw_jobs_stage;
```

### snowflake: copy to table
```
COPY INTO raw_jobs
FROM @raw_jobs_stage
file_format = (type = parquet)
MATCH_BY_COLUMN_NAME=CASE_INSENSITIVE;
```
