This kind of database **stores and retrieves data as a key-value pair**. However, the value is stored as a document in JSON or XML format. The value is thus understood by the database and can be found with a query.

This type of database therefore offers **increased flexibility**. It is mainly used for CMS systems, blogging platforms, or e-commerce applications. However, it is not suitable for complex transactions requiring multiple operations or queries on variable aggregate structures. The best known examples in this category are Amazon SimpleDB, CouchDB, **[MongoDB](https://datascientest.com/en/mongodb-all-about-the-document-oriented-nosql-database)**, Riak, and Lotus Notes.

A [document database](https://www.mongodb.com/document-databases) stores data in [JSON, BSON](https://www.mongodb.com/json-and-bson), or XML documents (not Word documents or Google Docs, of course). In a document database, documents can be nested. Particular elements can be indexed for faster querying.

Documents can be stored and retrieved in a form that is much closer to the data objects used in applications, which means less translation is required to use the data in an application. SQL data must often be assembled and disassembled when moving back and forth between applications and storage.

Document databases are popular with developers because they have the flexibility to rework their document structures as needed to suit their application, shaping their data structures as their application requirements change over time. This flexibility speeds development because, in effect, data becomes like code and is under the control of developers. In SQL databases, intervention by database administrators may be required to change the structure of a database.

The most widely adopted document databases are usually implemented with a scale-out architecture, providing a clear path to scalability of both data volumes and traffic.

Use cases include ecommerce platforms, trading platforms, and mobile app development across industries.