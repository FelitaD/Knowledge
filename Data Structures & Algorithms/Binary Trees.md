Trees are [[Graphs]] that can not have cycles and all nodes must be connected.

Everything in the left subtree is smaller than the current node, everything in the right subtree is larger.
- smallest value located at the end of leftmost subtree 
- largest value located at the end of rightmost subtree

- Order lists efficiently
- Much faster at searching than arrays and linked lists
- Much faster at inserting and deleting than arrays
- Used to implement more advanced data structures:
	- dynamic sets 
	- lookup tables 
	- priority queues

## Implementation

```python
class TreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left_child = left
		self.right_child = right

class BinarySearchTree:
	def __init__(self):
		self.root = None
```

## Complexities & Operations

All operations:
- worst case: O(n)
- average case: O(log n)

#### Searching
```python
 def search(self, search_value):
     current_node = self.root
     while current_node:
       if search_value == current_node.data:
         return True
       elif search_value < current_node.data:
         current_node = current_node.left_child
       else:
         current_node = current_node.right_child
	return False
```

#### Inserting
```python
 def insert(self, data):
	new_node = TreeNode(data)
	if self.root == None:
		self.root = new_node
		return 
	else:
		current_node = self.root     
		while True:
			if data < current_node.data:
				if current_node.left_child == None:
					current_node.left_child = new_node
					return
				else:
					current_node = current_node.left_child
			elif data > current_node.data:
				if current_node.right_child == None:
					current_node.right_child = new_node
					return
				else:
					current_node = current_node.right_child
```

#### Deleting

Replace node to delete with node that has a greater value but the least great.

