While a relational database stores data in rows and reads data row by row, a column store is organized as a set of columns. This means that when you want to run analytics on a small number of columns, you can read those columns directly without consuming memory with the unwanted data. Columns are often of the same type and benefit from more efficient compression, making reads even faster. Columnar databases can quickly aggregate the value of a given column (adding up the total sales for the year, for example). Use cases include analytics.

Unfortunately, there is no free lunch, which means that while columnar databases are great for analytics, the way in which they write data makes it very difficult for them to be strongly consistent as writes of all the columns require multiple write events on disk. Relational databases don't suffer from this problem as row data is written contiguously to disk.

As their name indicates, they are **based on columns**. They are based on the **BigTable model** from Google. Each column is treated separately, and the values are stored contiguously.

This category of database offers **high performance** for aggregation queries like SUM, COUNT, AVG and MIN. This is because the data is already available and ready in a column. Examples are HBase, Cassandra or Hypertable.

