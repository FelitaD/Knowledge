
Good for storing networks, geography, social relationships.

Trees are a type of graphs.
- directed
- undirected
- weighted

Most graph algorithms are at least `O(nlogn)`.

How to store this graph ?
![[Pasted image 20230622153749.png|200]]

- Edge list
```python
graph = [[0, 1], [1, 2], [1, 3], [2, 3]]
```
- Adjacency list
```python
graph = [
	[1],
	[0, 2, 3],
	[1, 3],
	[1, 2],
]

# or
graph = {     
	0: [1],     
	1: [0, 2, 3],     
	2: [1, 3],     
	3: [1, 2], 
	}
```
- Adjacency matrix
```python
graph = [     
	[0, 1, 0, 0],     
	[1, 0, 1, 1],     
	[0, 1, 0, 1],     
	[0, 1, 1, 0], 
	]
```