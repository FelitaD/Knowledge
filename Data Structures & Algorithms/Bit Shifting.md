Moves each digit left or right.

- **Left Shifts**
Multiples a number by 2.
```
0010  # 2
0010 << 1 -> 0100  # 4
0010 << 2 -> 1000  # 8
```

- **Logical Right Shifts** (not in Python)
Divides a number by 2 (modulo) if it's positive.
```
1011 >> 3  →  0001
0101 >> 1  →  0010  # 5 becomes 2
```

- **Arithmetic Right Shifts**
Also copies the most significant bit.
If a number is encoded in 2s complement, it preserves the sign.
```
1011 >> 1  →  1101 
1011 >> 3  →  1111  
0011 >> 1  →  0001 
0011 >> 2  →  0000
```

