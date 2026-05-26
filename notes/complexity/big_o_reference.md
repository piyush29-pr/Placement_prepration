# Big O Complexity Reference

> **Rule of Thumb:** If n = 10^8, you need O(n) or better. If n = 500, O(n²) is fine.

---

## Time Complexity Ladder (Slowest to Fastest)

```
O(n!)          → Factorial     → Brute force permutations (n ≤ 10)
O(2^n)         → Exponential   → All subsets, brute-force DP (n ≤ 20)
O(n^3)         → Cubic         → 3D DP, matrix chain (n ≤ 300)
O(n^2)         → Quadratic     → Nested loops, bubble sort (n ≤ 5000)
O(n log n)     → Linearithmic  → Merge sort, heap sort (n ≤ 10^6)
O(n)           → Linear        → Single pass (n ≤ 10^8)
O(√n)          → Square root   → Prime checking
O(log n)       → Logarithmic   → Binary search (any n)
O(1)           → Constant      → Hash lookup, arithmetic
```

---

## Data Structure Operations

| Structure         | Access | Search | Insert | Delete | Notes                         |
|-------------------|--------|--------|--------|--------|-------------------------------|
| Array             | O(1)   | O(n)   | O(n)   | O(n)   | Insert/delete shifts elements |
| Dynamic Array     | O(1)   | O(n)   | O(1)*  | O(n)   | *Amortized. Python list.      |
| Linked List       | O(n)   | O(n)   | O(1)   | O(1)   | O(1) if at known node         |
| Stack             | O(n)   | O(n)   | O(1)   | O(1)   | LIFO                          |
| Queue             | O(n)   | O(n)   | O(1)   | O(1)   | FIFO, use deque in Python     |
| Hash Map          | -      | O(1)*  | O(1)*  | O(1)*  | *Average, O(n) worst (rare)   |
| Hash Set          | -      | O(1)*  | O(1)*  | O(1)*  | Same as HashMap               |
| Binary Search Tree| O(n)*  | O(n)*  | O(n)*  | O(n)*  | *Balanced: O(log n)           |
| Balanced BST      | O(log n)| O(log n)| O(log n)| O(log n)| Python: sortedcontainers  |
| Min/Max Heap      | O(n)   | O(n)   | O(log n)| O(log n)| heapq in Python             |
| Trie              | O(m)   | O(m)   | O(m)   | O(m)   | m = length of string          |

---

## Sorting Algorithms Cheatsheet

| Algorithm      | Best       | Average    | Worst      | Space  | Stable? |
|----------------|------------|------------|------------|--------|---------|
| Bubble Sort    | O(n)       | O(n²)      | O(n²)      | O(1)   | Yes     |
| Selection Sort | O(n²)      | O(n²)      | O(n²)      | O(1)   | No      |
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)   | Yes     |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)   | Yes     |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(log n)| No     |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) | O(1)   | No      |
| Counting Sort  | O(n+k)     | O(n+k)     | O(n+k)     | O(k)   | Yes     |
| Radix Sort     | O(nk)      | O(nk)      | O(nk)      | O(n+k) | Yes     |
| Tim Sort       | O(n)       | O(n log n) | O(n log n) | O(n)   | Yes     |

> **Python's sort()** uses Timsort → O(n log n) worst case, O(n) for nearly sorted

---

## Python-Specific Complexity (Memorize These)

```python
# LIST
len(lst)              → O(1)
lst[i]                → O(1)   # Index access
lst.append(x)         → O(1)   # Amortized
lst.pop()             → O(1)   # Remove last
lst.pop(0)            → O(n)   # Remove first (NEVER do this in loops, use deque)
lst.insert(i, x)      → O(n)   # Shifts elements
x in lst              → O(n)   # Linear scan (use set for O(1))
lst.sort()            → O(n log n)
sorted(lst)           → O(n log n)

# DICT (HashMap)
d[key]                → O(1) avg
d[key] = val          → O(1) avg
key in d              → O(1) avg
del d[key]            → O(1) avg

# SET
x in s                → O(1) avg
s.add(x)              → O(1) avg
s.remove(x)           → O(1) avg

# STRING (IMPORTANT: strings are IMMUTABLE)
s[i]                  → O(1)
s + t                 → O(len(s) + len(t))  # Creates NEW string
"".join(lst)          → O(total length)     # Efficient string building

# DEQUE (from collections)
deque.append(x)       → O(1)
deque.appendleft(x)   → O(1)
deque.pop()           → O(1)
deque.popleft()       → O(1)   # Use this instead of list.pop(0)

# HEAPQ
heapq.heappush        → O(log n)
heapq.heappop         → O(log n)
heapq.heapify         → O(n)
heap[0]               → O(1)   # Peek minimum
```

---

## Space Complexity Rules

```
O(1)    → Fixed variables, no extra structures
O(log n) → Recursive call stack of depth log n (binary search recursion)
O(n)    → Array, HashMap, Set proportional to input
O(n²)   → 2D DP table, adjacency matrix for graph
O(n * m) → 2D DP on two sequences of length n and m
```

---

## Optimization Reduction Patterns (Interview Gold)

```
O(n²) → O(n log n)   : Use sorting + binary search instead of nested loops
O(n²) → O(n)         : Use HashMap for O(1) lookups instead of inner loop
O(2^n) → O(n²) or O(n): Use DP to eliminate repeated subproblems
O(n) space → O(1)    : Use two variables instead of array (Fibonacci pattern)
O(n) space → O(√n)   : Mathematical reduction (rare, but exists)
```

---

*Reference for: data_structures/ | algorithms/ | patterns/ | Use during code review*
