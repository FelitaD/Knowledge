[[Arrays]]
[[Linked lists]]
[[Stacks]]
[[Queues]]
[[Hash tables]]
[[Binary Trees]]
[[Heaps]]
[[B-trees]]

- **Time complexities**

BigO Cheatsheet: https://www.bigocheatsheet.com/
![[Pasted image 20230616211112.png]]

****
- **Reading from sequential memory addresses is faster**
When processor asks contents from a certain memory address on the RAM, the memory controller also gives nearby memory addresses. 

*RAM, Cache, Memory Controller and Processor*
![[Pasted image 20230620192511.png|200]]

- **Most integers are fixed-width: they take up a constant O(1) space (eg. 64 bits) in the RAM**
[[Binary Numbers]]

****
- **How data structures are used**

- Storing data
Data structures are used for efficient data persistence such as specifying the collection of attributes and corresponding structures used to store records in a database management system.

- Managing resources and services 
Core operating system (OS) resources and services are enabled through the use of data structures such as linked lists for memory allocation, file directory management and file structure trees, as well as process scheduling queues.

- Data exchange
Data structures define the organization of information shared between applications, such as TCP/IP packets.

- Ordering and sorting
Data structures such as [[Binary Trees]] -also known as an ordered or sorted binary tree -provide efficient methods of sorting objects, such as character strings used as tags. With data structures such as priority queues, programmers can manage items organized according to a specific priority.

- Indexing
Even more sophisticated data structures such as[[ B-trees]] are used to index objects, such as those stored in a database.

- Searching
[[Indexes]] created using binary search trees, [[B-trees]] or [[Hash tables]] speed the ability to find a specific sought-after item.

- Scalability
Big data applications use data structures for allocating and managing data storage across distributed storage locations, ensuring scalability and performance. Certain big data programming environments -such as Apache [[Spark]] -provide data structures that mirror the underlying structure of database records to simplify querying. 




