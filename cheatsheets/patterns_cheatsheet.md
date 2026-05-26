# 🎯 Pattern Recognition Master Cheatsheet

> **Core Principle:** You don't solve problems. You recognize patterns and apply frameworks.
> Every DSA problem is an instance of a known pattern. Your job is identification, not invention.

---

## How to Read Any Problem (Universal 5-Step Framework)

```
Step 1 — READ the constraints carefully
    → Array size (n)? → Tells you what O() is acceptable
    → Values range?   → Tells you if hashing is safe
    → Sorted input?   → Tells you if binary search / two pointers apply

Step 2 — IDENTIFY key phrases (see table below)
Step 3 — MAP to a pattern
Step 4 — RECALL the template
Step 5 — CODE the template, adapt, test edge cases
```

**Acceptable Complexity by Input Size:**

| n               | Max Acceptable Complexity |
|-----------------|--------------------------|
| n ≤ 10          | O(n!) — Backtracking OK  |
| n ≤ 20          | O(2^n) — Bitmask DP OK   |
| n ≤ 500         | O(n²) — Nested loops OK  |
| n ≤ 10,000      | O(n log n) — Sorting OK  |
| n ≤ 10^6        | O(n) — Linear mandatory  |
| n ≤ 10^8        | O(log n) — Binary Search |

---

## Pattern 1: Sliding Window

### Recognition Signals
```
✅ "Contiguous subarray" or "contiguous substring"
✅ "Maximum/minimum sum of subarray of size k"
✅ "Longest substring with at most k distinct characters"
✅ "Minimum window substring"
✅ Input is an array or string
✅ You need to examine a PORTION of the data, not pairs/triples
```

### Red Flags (Sliding Window WON'T work)
```
❌ Non-contiguous elements (use DP/backtracking)
❌ Problem asks for pairs at any distance (use two pointers/hashmap)
❌ 2D input (use different technique)
```

### Two Types

**Type 1 — Fixed Window (size k given)**
```python
def fixed_window(arr, k):
    # Build initial window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide: add right, remove left
    for i in range(k, len(arr)):
        window_sum += arr[i]        # Add new right element
        window_sum -= arr[i - k]    # Remove old left element
        max_sum = max(max_sum, window_sum)

    return max_sum
# Time: O(n) | Space: O(1)
```

**Type 2 — Variable Window (find window meeting a condition)**
```python
def variable_window(arr, condition):
    left = 0
    result = 0
    window_state = {}  # Track what's in window (freq, sum, etc.)

    for right in range(len(arr)):
        # EXPAND: Add arr[right] to window
        window_state[arr[right]] = window_state.get(arr[right], 0) + 1

        # SHRINK: While window violates condition, move left
        while violates_condition(window_state):
            window_state[arr[left]] -= 1
            if window_state[arr[left]] == 0:
                del window_state[arr[left]]
            left += 1

        # UPDATE result: window is valid at this point
        result = max(result, right - left + 1)

    return result
# Time: O(n) | Space: O(k) where k = distinct elements
```

### Common Mistakes
```
❌ Forgetting to initialize the first window before sliding
❌ Off-by-one: window size is right - left + 1, not right - left
❌ Not handling the shrink condition carefully (infinite loop risk)
❌ Using fixed window template for variable window problems
```

### Problem Progression
```
Easy   → Maximum Sum Subarray of Size K
Easy   → Smallest Subarray with Sum >= S
Medium → Longest Substring with K Distinct Chars
Medium → Fruits Into Baskets
Medium → No-Repeat Substring (LC 3)
Hard   → Minimum Window Substring (LC 76)
Hard   → Substring with all characters of a pattern
```

---

## Pattern 2: Two Pointers

### Recognition Signals
```
✅ SORTED array or can be sorted (KEY requirement)
✅ "Find a pair that..." with some condition
✅ "Three sum", "Four sum", "closest pair"
✅ Palindrome check
✅ Remove duplicates in-place
✅ "Container with most water" (maximize area between bars)
✅ Two arrays to merge/compare
```

### Template 1 — Opposite Ends (sorted, find pair)
```python
def two_pointers_opposite(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]          # Found
        elif current_sum < target:
            left += 1                     # Need larger value
        else:
            right -= 1                    # Need smaller value

    return []
# Time: O(n) | Space: O(1)
# WHY it works: Sorted array means moving left ptr increases sum,
# moving right ptr decreases sum. We cover all possibilities.
```

### Template 2 — Same Direction (fast/slow or remove duplicates)
```python
def remove_duplicates(arr):
    # 'slow' marks where next unique element goes
    # 'fast' scans ahead to find unique elements
    slow = 1

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow - 1]:  # Found a new unique element
            arr[slow] = arr[fast]
            slow += 1

    return slow  # Length of deduplicated array
# Time: O(n) | Space: O(1) — in-place
```

### Common Mistakes
```
❌ Applying to UNSORTED array (always sort first or confirm it's sorted)
❌ Not handling duplicates (in 3Sum, skip duplicates after finding a valid triplet)
❌ Loop condition: use left < right, NOT left <= right (avoids using same element)
❌ Moving BOTH pointers when you should only move one
```

### Problem Progression
```
Easy   → Two Sum II (sorted input)
Easy   → Valid Palindrome
Easy   → Squaring a Sorted Array
Medium → Three Sum (LC 15)
Medium → Three Sum Closest
Medium → Container with Most Water (LC 11)
Hard   → Four Sum
Hard   → Trapping Rain Water (LC 42)
```

---

## Pattern 3: Binary Search

### Recognition Signals
```
✅ Sorted array / matrix
✅ "Find minimum/maximum value that satisfies a condition"
✅ "Search in rotated sorted array"
✅ "Find first/last occurrence"
✅ O(log n) time complexity required
✅ Can you define: if mid satisfies condition, search left? or right?
```

### Core Template (Memorize This Exactly)
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:             # <= because we check single elements
        mid = left + (right - left) // 2  # Avoids integer overflow (habit from C++)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1           # Target is in RIGHT half
        else:
            right = mid - 1          # Target is in LEFT half

    return -1  # Not found
# Time: O(log n) | Space: O(1)
```

### Advanced: Binary Search on Answer
```python
# Pattern: "Find minimum X such that condition(X) is True"
# Used when: you can CHECK a condition but can't directly compute answer

def binary_search_on_answer(lo, hi, condition_fn):
    """
    Find the minimum value in [lo, hi] satisfying condition_fn.
    condition_fn must be monotone: False...False...True...True
    """
    result = -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if condition_fn(mid):
            result = mid        # mid works, but maybe something smaller works
            hi = mid - 1        # Search left for smaller valid answer
        else:
            lo = mid + 1        # mid doesn't work, need larger

    return result

# Example: "Minimum days to make m bouquets"
# condition(days) = "can we make m bouquets in 'days' days?"
# Answer: smallest days where condition = True
```

### Common Mistakes
```
❌ Using mid = (left + right) // 2 — causes integer overflow in other languages
   Always use: mid = left + (right - left) // 2

❌ Infinite loop: When to use left < right vs left <= right
   Use left <= right for standard search (terminates when left > right)
   Use left < right when left == right means you've found the answer

❌ Not handling the case where target doesn't exist

❌ Confusing which half to search (write out: if arr[mid] < target, target is RIGHT)

❌ Off-by-one in left = mid+1 vs left = mid (can cause infinite loop)
```

### Problem Progression
```
Easy   → Binary Search (LC 704)
Easy   → Find First and Last Position (LC 34)
Medium → Search in Rotated Sorted Array (LC 33)
Medium → Find Minimum in Rotated Sorted Array (LC 153)
Medium → Koko Eating Bananas (LC 875) — Binary Search on Answer
Hard   → Median of Two Sorted Arrays (LC 4)
Hard   → Minimum Capacity to Ship Packages (LC 1011)
```

---

## Pattern 4: Prefix Sum

### Recognition Signals
```
✅ "Sum of elements between index i and j" (range sum query)
✅ "Subarray sum equals K"
✅ "Number of subarrays with sum divisible by K"
✅ Multiple queries on same array
✅ 2D: "sum of rectangle" (2D prefix sum)
```

### Template
```python
def build_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)  # prefix[i] = sum of arr[0..i-1]

    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    return prefix

def range_sum(prefix, left, right):
    # Sum of arr[left..right] inclusive
    return prefix[right + 1] - prefix[left]
# Preprocessing: O(n) | Query: O(1) | Space: O(n)
```

### Advanced: Subarray Sum Equals K
```python
def subarray_sum_equals_k(nums, k):
    """
    Count subarrays with sum == k.
    Key Insight: sum(i,j) = prefix[j] - prefix[i-1]
    So if prefix[j] - k == some previous prefix → found a subarray
    """
    count = 0
    prefix_sum = 0
    seen = {0: 1}  # prefix_sum → frequency; {0:1} handles subarrays from index 0

    for num in nums:
        prefix_sum += num

        # If (prefix_sum - k) was seen before, those are valid subarrays
        if (prefix_sum - k) in seen:
            count += seen[prefix_sum - k]

        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count
# Time: O(n) | Space: O(n)
```

### Common Mistakes
```
❌ Forgetting {0: 1} in the HashMap initialization
   This handles subarrays starting at index 0

❌ 1-indexed vs 0-indexed confusion in prefix array

❌ range_sum formula: it's prefix[right+1] - prefix[left], not prefix[right] - prefix[left-1]
```

---

## Pattern 5: Fast & Slow Pointers (Floyd's Algorithm)

### Recognition Signals
```
✅ Linked list cycle detection
✅ "Find the start of a cycle"
✅ "Find middle of a linked list"
✅ "Happy number" (number theory cycle detection)
✅ "Palindrome linked list"
```

### Template — Cycle Detection
```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps

        if slow == fast:          # They met → cycle exists
            return True

    return False  # fast reached None → no cycle
# Time: O(n) | Space: O(1)

def find_cycle_start(head):
    slow = fast = head

    # Phase 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Phase 2: Find start (mathematical proof: reset one pointer to head)
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # This is the cycle start
```

### Template — Middle of Linked List
```python
def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # slow is at the middle
# When list has even length → returns second of two middle nodes
```

---

## Pattern 6: Tree BFS (Level Order)

### Recognition Signals
```
✅ "Level order traversal"
✅ "Zigzag traversal"
✅ "Level averages"
✅ "Minimum depth of tree"
✅ "Connect level order siblings"
✅ "Shortest path" in unweighted graph/tree
```

### Template
```python
from collections import deque

def bfs_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)   # CRITICAL: snapshot size at start of level
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
# Time: O(n) | Space: O(n) — queue holds at most one full level
```

### Common Mistakes
```
❌ Not snapshotting level_size = len(queue) before the inner loop
   Without this, you can't separate levels (queue grows as you process)

❌ Using a list instead of deque → queue.pop(0) is O(n), deque.popleft() is O(1)

❌ Not checking if node.left/right exist before appending
```

---

## Pattern 7: Tree DFS

### Recognition Signals
```
✅ "Path from root to leaf"
✅ "Maximum/minimum path sum"
✅ "All paths", "count paths"
✅ "Validate BST"
✅ "Diameter of tree"
✅ Inorder / Preorder / Postorder traversal
```

### Template — Recursive DFS
```python
def dfs(node, path, result):
    if not node:
        return

    path.append(node.val)  # PRE-ORDER: process before children

    if not node.left and not node.right:  # Leaf node
        result.append(list(path))         # Found a root-to-leaf path

    dfs(node.left, path, result)
    dfs(node.right, path, result)

    path.pop()  # BACKTRACK: remove current node before returning up
```

### Template — Iterative DFS (Stack)
```python
def dfs_iterative(root):
    if not root:
        return []

    result = []
    stack = [(root, [root.val])]  # (node, path_so_far)

    while stack:
        node, path = stack.pop()

        if not node.left and not node.right:
            result.append(path)

        if node.right:
            stack.append((node.right, path + [node.right.val]))
        if node.left:
            stack.append((node.left, path + [node.left.val]))

    return result
```

---

## Pattern 8: Dynamic Programming

### Recognition Signals
```
✅ "Maximum/minimum" result
✅ "Number of ways to..."
✅ "Can we achieve..."
✅ Overlapping subproblems (same computation repeated)
✅ Optimal substructure (optimal solution uses optimal sub-solutions)
✅ Keywords: "partition", "subsequence", "subset", "count paths"
```

### The DP Thinking Framework (Always Follow This)
```
Step 1 — DEFINE: What does dp[i] or dp[i][j] MEAN?
          Write it in plain English before coding.

Step 2 — RECURRENCE: How does dp[i] relate to smaller subproblems?
          dp[i] = f(dp[i-1], dp[i-2], ..., input[i])

Step 3 — BASE CASE: What is dp[0]? dp[1]? (Prevent index errors)

Step 4 — DIRECTION: Fill left-to-right? right-to-left? top-to-bottom?

Step 5 — ANSWER: Is it dp[n]? max(dp)? dp[n][m]?
```

### Template — 0/1 Knapsack
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[i][w] = max value using first i items with weight limit w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Option 1: Don't take item i
            dp[i][w] = dp[i-1][w]

            # Option 2: Take item i (if it fits)
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i-1][w - weights[i-1]] + values[i-1])

    return dp[n][capacity]
# Time: O(n * capacity) | Space: O(n * capacity) → can optimize to O(capacity)
```

### Template — Fibonacci-Style (1D DP)
```python
def climbing_stairs(n):
    # dp[i] = number of ways to reach step i
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # From step below or two steps below

    return dp[n]
# Can be space-optimized to O(1) using two variables
```

### DP Sub-Patterns (Each is Its Own Pattern)
```
1. Fibonacci Numbers         → dp[i] = dp[i-1] + dp[i-2]
2. 0/1 Knapsack              → Include/exclude each item
3. Unbounded Knapsack        → Item can be reused
4. Longest Common Subsequence → 2D DP on two sequences
5. Palindromic Subsequence   → DP on reversed string
6. DP on Trees               → DFS + memoization
7. DP on Intervals           → dp[i][j] = optimal for range [i,j]
8. Counting DP               → Count combinations/arrangements
9. Bitmask DP                → State = subset of elements (n ≤ 20)
10. Digit DP                 → Count numbers satisfying condition in range
```

---

## Pattern 9: Backtracking

### Recognition Signals
```
✅ "Generate ALL..." (all subsets, permutations, combinations)
✅ "Find any one valid solution" (Sudoku, N-Queens)
✅ "Count the number of solutions"
✅ Constraint satisfaction problems
✅ When you need to "undo" a choice and try another
```

### Universal Backtracking Template
```python
def backtrack(state, choices, result):
    # BASE CASE: Is current state a complete solution?
    if is_complete(state):
        result.append(list(state))  # Add a COPY, not reference
        return

    for choice in choices:
        if is_valid(state, choice):     # Pruning: skip invalid choices
            state.append(choice)        # CHOOSE
            backtrack(state, next_choices(choices, choice), result)
            state.pop()                 # UNCHOOSE (backtrack)
```

### Example: Subsets
```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(list(current))  # Every state is a valid subset

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)   # Move start forward (no reuse)
            current.pop()               # Undo choice

    backtrack(0, [])
    return result
```

### Common Mistakes
```
❌ Appending state directly: result.append(state) → always append list(state)
   Because state is mutable; you'd add a reference, not a copy.

❌ Forgetting to pop after recursive call → state accumulates garbage

❌ Not pruning early → exponential time when constraint checking could stop early

❌ Confusing permutations (order matters, use visited[]) vs combinations (order doesn't)
```

---

## Pattern 10: Heap / Top-K Elements

### Recognition Signals
```
✅ "K largest", "K smallest", "K most frequent"
✅ "K closest points to origin"
✅ "Median of a data stream"
✅ "Merge K sorted lists"
✅ "Find the Kth largest element"
```

### Template — K Largest Elements
```python
import heapq

def k_largest(nums, k):
    # MIN-HEAP of size k maintains K largest elements seen so far
    # Python's heapq is a min-heap by default
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # Remove smallest → keep K largest

    return heap  # heap[0] is the Kth largest
# Time: O(n log k) | Space: O(k)
# WHY min-heap for K largest: We remove the smallest, keeping only the K largest
```

### Template — K Smallest Elements
```python
def k_smallest(nums, k):
    # MAX-HEAP of size k (negate values for max-heap in Python)
    heap = []

    for num in nums:
        heapq.heappush(heap, -num)    # Negate for max-heap simulation
        if len(heap) > k:
            heapq.heappop(heap)       # Remove largest (most negative)

    return [-x for x in heap]
```

### Python Heap Cheatsheet
```python
import heapq

# Min-heap operations
heap = []
heapq.heappush(heap, val)      # Push
min_val = heapq.heappop(heap)  # Pop minimum
min_val = heap[0]              # Peek minimum (no removal)

# Build heap from list: O(n)
heapq.heapify(nums)

# Heap with tuples (sorts by first element)
heapq.heappush(heap, (priority, item))

# Max-heap: negate values
heapq.heappush(heap, -val)
max_val = -heapq.heappop(heap)

# K smallest: O(n log k)
heapq.nsmallest(k, nums)

# K largest: O(n log k)
heapq.nlargest(k, nums)
```

---

## Pattern 11: Graph Traversal

### Recognition Signals
```
✅ "Number of islands", "number of connected components"
✅ "Shortest path" → BFS (unweighted), Dijkstra (weighted)
✅ "Course schedule" (dependency) → Topological Sort
✅ "Clone graph", "number of provinces"
✅ "Detect cycle in graph"
```

### BFS for Shortest Path
```python
from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, 0)])  # (node, distance)
    visited = {start}

    while queue:
        node, dist = queue.popleft()

        if node == end:
            return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1  # No path exists
```

### DFS for Connected Components / Islands
```python
def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Mark as visited (in-place)
        dfs(r+1, c); dfs(r-1, c)
        dfs(r, c+1); dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count
```

### Topological Sort (Kahn's Algorithm — BFS-based)
```python
from collections import deque

def topological_sort(n, prerequisites):
    graph = [[] for _ in range(n)]
    in_degree = [0] * n

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else []  # Empty = cycle exists
```

---

## Master Decision Tree

```
Problem received
│
├── Input is sorted or can be sorted?
│   ├── YES → Two Pointers or Binary Search
│   └── NO  → Continue
│
├── Find a subarray/substring?
│   ├── Contiguous + fixed size?  → Fixed Sliding Window
│   ├── Contiguous + variable?    → Variable Sliding Window
│   └── Non-contiguous?           → DP or Backtracking
│
├── Linked List problem?
│   ├── Cycle?          → Fast/Slow Pointers
│   ├── Reverse?        → Iterative with prev/curr/next
│   └── Middle/Kth?     → Fast/Slow Pointers
│
├── Tree problem?
│   ├── Level by level? → BFS (Queue)
│   └── Path/depth?     → DFS (Recursion or Stack)
│
├── Graph problem?
│   ├── Shortest path (unweighted)?  → BFS
│   ├── Shortest path (weighted)?    → Dijkstra (heapq)
│   ├── Connected components?        → DFS/BFS + visited
│   └── Dependencies/ordering?       → Topological Sort
│
├── Optimization (max/min) with overlapping subproblems?
│   └── Dynamic Programming
│       ├── 1D array input?   → 1D DP
│       ├── 2 sequences?      → 2D DP (LCS, Edit Distance)
│       └── Subsets?          → Knapsack variant
│
├── Generate ALL solutions?
│   └── Backtracking (with pruning)
│
├── K largest/smallest/frequent?
│   └── Heap (Priority Queue)
│
└── Range sum queries?
    └── Prefix Sum
```

---

*Last Updated: [DATE] | Maintained in: cheatsheets/ | Pattern count: 11 core patterns*
