A graph database focuses on the relationship between data elements. Each element is stored as a node (such as a person in a social media graph). The connections between elements are called links or relationships. In a graph database, connections are first-class elements of the database, stored directly. In relational databases, links are implied, using data to express the relationships.

A graph database is optimized to capture and search the connections between data elements, overcoming the overhead associated with JOINing multiple tables in SQL.

Very few real-world business systems can survive solely on graph queries. As a result graph databases are usually run alongside other more traditional databases.

Use cases include fraud detection, social networks, and knowledge graphs.

Graph-Based databases **store entities and the relationships** between these entities. The entity is stored as a node, and the relationships as edges. This makes it easy to visualize the relationships between the nodes. Each node and each edge has a unique identifier.

This type of database is multi-relational. It is mainly used for social networks, logistics or spatial data. Popular examples include Neo4J, Infinite Graph, OrientDB and FlockDB.