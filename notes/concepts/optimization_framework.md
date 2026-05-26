# Optimization Thinking Framework
## From Brute Force → Better → Optimal

> This is the single most important mental framework for cracking interviews.
> Interviewers don't want the optimal solution in 2 minutes.
> They want to SEE your thinking process. This document trains that process.

---

## The 5-Question Optimization Protocol

When you have a brute force solution, ask these 5 questions in order:

```
Question 1: WHAT IS SLOW?
  → Find the bottleneck. Which line/loop is O(n²) or O(n³)?
  → Example: "The inner loop searches for an element linearly."

Question 2: WHY IS IT SLOW?
  → What computation is repeated or wasteful?
  → Example: "I'm scanning the same subarray multiple times."

Question 3: CAN I PRECOMPUTE?
  → Can I compute something upfront to make queries O(1)?
  → Example: Prefix sums, sorted order, frequency maps

Question 4: CAN I AVOID REDUNDANT WORK?
  → Is there a data structure that tracks state incrementally?
  → Example: Sliding window avoids recomputing sum from scratch each time

Question 5: WHAT'S THE TRADEOFF?
  → Every optimization trades something (usually space for time)
  → State the tradeoff explicitly: "I'm using O(n) extra space to get O(n) time"
```

---

## The Optimization Ladder (Visual Mental Model)

```
PROBLEM: Maximum sum subarray of size k

LEVEL 1 — Brute Force
  for every starting position i (n positions):
    sum up k elements from i to i+k
  Time: O(n*k) | Space: O(1)

  BOTTLENECK: Recomputing sum from scratch for each window

LEVEL 2 — Observe the Pattern
  Window [i, i+k-1] → [i+1, i+k]
  Difference: remove arr[i], add arr[i+k]
  We don't need to re-sum! Just adjust.

LEVEL 3 — Sliding Window
  Build initial window sum: O(k)
  Slide: for each step, sum += arr[right] - arr[left]
  Time: O(n) | Space: O(1)

REDUCTION: O(n*k) → O(n)
HOW: Eliminated recomputation by maintaining running state
```

---

## Common Optimization Moves (Memorize These)

### Move 1: Linear Scan → HashMap Lookup
```
WHEN: You have an inner loop that searches for an element
WHAT: Store elements in a dict as you scan
EFFECT: O(n²) → O(n)

Before:
  for i in range(n):
    for j in range(i+1, n):     ← O(n) inner search
      if arr[j] == target - arr[i]:
        return [i, j]

After:
  seen = {}
  for i, num in enumerate(arr):
    if target - num in seen:    ← O(1) dict lookup
      return [seen[target-num], i]
    seen[num] = i
```

### Move 2: Recomputation → Prefix Sum (Precomputation)
```
WHEN: You answer range queries (sum, min, max) multiple times
WHAT: Build a prefix array once, answer each query in O(1)
EFFECT: O(n) per query → O(1) per query

Before:
  def range_sum(arr, l, r):
    return sum(arr[l:r+1])        ← O(n) per call

After:
  prefix = build_prefix(arr)      ← O(n) once
  def range_sum(l, r):
    return prefix[r+1] - prefix[l] ← O(1) per call
```

### Move 3: Repeated Subproblems → Memoization/DP
```
WHEN: Recursive solution recalculates the same state multiple times
WHAT: Cache results in a dict (top-down) or array (bottom-up)
EFFECT: O(2^n) → O(n²) or O(n)

Before (Fibonacci):
  def fib(n):
    return fib(n-1) + fib(n-2)   ← Exponential: O(2^n)

After (Memoization):
  memo = {}
  def fib(n):
    if n in memo: return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]              ← O(n) with O(n) space

After (Bottom-up DP, O(1) space):
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
  return a
```

### Move 4: Full Search → Binary Search
```
WHEN: Input is sorted, or you're searching for a minimum/maximum
WHAT: Eliminate half the search space each iteration
EFFECT: O(n) → O(log n)

Before:
  for i in range(len(arr)):
    if arr[i] == target:
      return i                  ← O(n)

After (sorted array):
  left, right = 0, len(arr)-1
  while left <= right:
    mid = (left+right)//2
    if arr[mid] == target: return mid
    elif arr[mid] < target: left = mid+1
    else: right = mid-1       ← O(log n)
```

### Move 5: Nested Loops → Two Pointers
```
WHEN: Sorted array, need pairs/triplets with a constraint
WHAT: Use two pointers from ends, move based on comparison
EFFECT: O(n²) → O(n)

Before:
  for i in range(n):
    for j in range(i+1, n):     ← O(n²)
      if arr[i] + arr[j] == target:
        return [i, j]

After (sorted array):
  left, right = 0, n-1
  while left < right:           ← O(n)
    s = arr[left] + arr[right]
    if s == target: return [left, right]
    elif s < target: left += 1
    else: right -= 1
```

### Move 6: O(n) Space → O(1) Space (Space Optimization)
```
WHEN: DP table where each row only depends on previous row
WHAT: Use two 1D arrays or two variables instead of full 2D table
EFFECT: O(n²) space → O(n) space

Before (2D DP for Fibonacci-like):
  dp = [0] * (n+1)
  dp[0] = 0; dp[1] = 1
  for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]  ← O(n) space

After:
  prev2, prev1 = 0, 1
  for _ in range(2, n+1):
    prev2, prev1 = prev1, prev1+prev2  ← O(1) space
```

---

## Real Example: Full Optimization Walkthrough

**Problem:** Find the length of the longest substring with at most k distinct characters.

```python
# ============================================================
# LEVEL 1 — BRUTE FORCE
# ============================================================
# Intuition: Try every possible substring, check if it has <= k distinct chars
# Time: O(n²) or O(n³) | Space: O(k)

def longest_k_distinct_brute(s, k):
    n = len(s)
    max_len = 0

    for i in range(n):           # Start of substring
        for j in range(i, n):   # End of substring
            # Check distinct chars in s[i..j]
            if len(set(s[i:j+1])) <= k:
                max_len = max(max_len, j - i + 1)

    return max_len
# Bottleneck: set(s[i:j+1]) recomputes from scratch for every (i,j) pair

# ============================================================
# OPTIMIZATION THINKING
# ============================================================
# Q1: What is slow?
#     Inner loop + set computation = O(n²) or O(n³) total
#
# Q2: Why is it slow?
#     We throw away information. When we go from s[i..j] to s[i..j+1],
#     we recompute the entire set. We already KNOW s[i..j]'s characters.
#
# Q3: Can I maintain state incrementally?
#     YES! Maintain a frequency map as I expand the window.
#     When freq map has > k distinct keys, shrink from left.
#
# Q4: What data structure tracks this?
#     dict: char → frequency in current window
#
# Q5: Tradeoff?
#     O(k) extra space for the freq map. Worth it for O(n) time gain.

# ============================================================
# LEVEL 2 — OPTIMAL: SLIDING WINDOW
# ============================================================
# Time: O(n) | Space: O(k)

def longest_k_distinct_optimal(s, k):
    freq = {}       # char → count in current window
    left = 0
    max_len = 0

    for right in range(len(s)):
        # EXPAND: add s[right] to window
        freq[s[right]] = freq.get(s[right], 0) + 1

        # SHRINK: while we violate the constraint (> k distinct chars)
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]   # Remove key entirely (important!)
            left += 1

        # Window is valid: update result
        max_len = max(max_len, right - left + 1)

    return max_len

# Reduction: O(n²) → O(n) by maintaining window state incrementally
# The key insight: each character is added and removed at most once → O(n)
```

---

## When NOT to Optimize

```
1. If n is small (n < 100), brute force is fine and MORE readable.
   Don't optimize for the sake of it.

2. If the interviewer hasn't asked for optimization yet.
   State the brute force, get agreement, THEN optimize.
   This shows methodical thinking.

3. If optimization makes code significantly harder to understand.
   Code clarity is a real engineering value.
   State the tradeoff: "I can optimize to O(n log n) but the code becomes complex.
   For production, I'd keep O(n²) unless n is large."

4. If you're not sure the optimization is correct.
   A working brute force > a broken optimal solution.

INTERVIEW RULE: A clear brute force that you can explain fully
is worth more than a half-coded optimal solution.
```

---

## Complexity Reduction Decision Tree

```
You have a brute force. It's O(n²). What to do?

Is there a nested loop where the inner loop SEARCHES for something?
├── YES → Can you precompute what it searches for?
│          ├── YES → Use a HashMap → O(n)
│          └── NO  → Is input sorted? Use Two Pointers → O(n)
│
Is there REPEATED subproblem computation (recursion)?
├── YES → Use memoization (top-down DP) or tabulation (bottom-up DP)
│
Are you processing a subarray/window multiple times?
├── YES → Use Sliding Window → O(n)
│
Are you searching for a value in a sorted range?
├── YES → Binary Search → O(log n)
│
Are you considering all subsets?
├── YES → Can you use DP to avoid exponential blowup?
│          ├── YES → DP → O(n²) or O(n * target)
│          └── NO  → Backtracking with pruning
```

---

## Senior Engineer Mindset: Thinking Out Loud

**The interview process your thoughts should follow:**

```
"Let me start with the naive approach to make sure I understand the problem.

For each [element], I [check all other elements]. That gives me O(n²).

Looking at this more carefully, the bottleneck is [inner loop searches for X].

Can I precompute X? Yes — if I build a [data structure] as I scan, 
I can look up X in O(1). That reduces the inner loop to O(1), 
giving O(n) total.

The tradeoff is O(n) extra space for the [data structure].

Let me code this up and trace through the example to verify..."
```

This internal monologue, spoken out loud, is what FAANG interviewers evaluate.
Not the code. The THINKING.

---

*This file lives in: notes/concepts/optimization_framework.md*
