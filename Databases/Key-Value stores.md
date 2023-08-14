The simplest type of NoSQL database is a [key-value store](https://www.mongodb.com/key-value-database). Every data element in the database is stored as a key value pair consisting of an attribute name (or "key") and a value. In a sense, a key-value store is like a relational database with only two columns: the key or attribute name (such as "state") and the value (such as "Alaska").

Use cases include shopping carts, user preferences, and user profiles.

In the case of key/value pair databases, the data is **stored as key/value pairs**. This allows the support of large volumes of data and heavy loads. The data is stored in a **“hash” array** in which each key is unique. The value can be a JSON, a BLOB object, a line of code or other.

This type of database is **the most basic**. It allows the developer to store data more easily without a schema. Examples include **Redis** or **Dynamo**. Moreover, Amazon Dynamo is the initial model of this category of database.