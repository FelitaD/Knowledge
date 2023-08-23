
Frequently applications that are doing online analytical processing are designed based around a star schema.

It's a certain type of relational schema.
In a star schema, there's usually one fact table. That will be a typically very large table, it will be updated frequently. Often it's actually append only, so there are only inserts into the fact table.
And then there are maybe many dimension tables.
Those are updated infrequently and don't tend to be as large.
