# Pattern: Sliding Window

## What is Sliding Window?

Sliding Window is a technique where you maintain a **"window"** (a contiguous subarray or substring) and slide it across the input, updating the window's state incrementally rather than recomputing from scratch.

**Core Idea:**
Instead of re-examining every element for every window position (O(n²)),
maintain a running state that adjusts as the window expands or shrinks (O(n)).

---

## Recognition Signals (Memorize These)

```
MUST have ALL of these:
  ✅ Input is an array or string (sequential structure)
  ✅ You need to examine a contiguous portion (subarray/substring)
  ✅ You're looking for maximum, minimum, count, or validity

PLUS one of:
  ✅ "Fixed size k" → Fixed Sliding Window
  ✅ "Longest/shortest with condition" → Variable Sliding Window
  ✅ "All subarrays of..." → Sliding Window
```

---

## Problem Progression (Solve in This Order)

| # | Problem | Difficulty | Link | Window Type | Status |
|---|---------|------------|------|-------------|--------|
| 1 | Maximum Sum Subarray of Size K | Easy | - | Fixed | [ ] |
| 2 | Smallest Subarray with Sum >= S | Easy | - | Variable | [ ] |
| 3 | Longest Substring with K Distinct Chars | Medium | LC 340 | Variable | [ ] |
| 4 | Fruits Into Baskets | Medium | LC 904 | Variable | [ ] |
| 5 | No-Repeat Substring | Medium | LC 3 | Variable | [ ] |
| 6 | Longest Substring with Same Letters After Replacement | Medium | LC 424 | Variable | [ ] |
| 7 | Longest Subarray with Ones After Replacement | Medium | LC 1004 | Variable | [ ] |
| 8 | Permutation in a String | Medium | LC 567 | Fixed | [ ] |
| 9 | String Anagrams | Medium | LC 438 | Fixed | [ ] |
| 10 | Smallest Window containing Substring | Hard | LC 76 | Variable | [ ] |

---

## Templates

### Fixed Window
```python
def fixed_window(arr: list, k: int):
    window_sum = sum(arr[:k])
    result = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        result = max(result, window_sum)

    return result
```

### Variable Window
```python
def variable_window(arr: list, condition):
    left = 0
    window = {}
    result = 0

    for right in range(len(arr)):
        # Expand: add arr[right]
        window[arr[right]] = window.get(arr[right], 0) + 1

        # Shrink: while condition violated
        while not is_valid(window):
            window[arr[left]] -= 1
            if window[arr[left]] == 0:
                del window[arr[left]]
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result
```

---

## Common Mistakes

```
❌ Using list.pop(0) instead of deque.popleft() in O(1)
❌ Not deleting zero-frequency keys from dict (wrong distinct count)
❌ Off-by-one: window size = right - left + 1
❌ Mixing fixed and variable window templates
❌ Updating result outside the valid window check
```

---

*Folder: patterns/sliding_window/ | Start date: [DATE]*
