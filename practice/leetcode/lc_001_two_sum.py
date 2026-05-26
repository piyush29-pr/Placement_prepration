"""
================================================================================
METADATA
================================================================================
Problem Name    : Two Sum
Platform        : LeetCode
Problem Link    : https://leetcode.com/problems/two-sum/
Difficulty      : Easy
Topic           : Array, Hash Map
Pattern         : Complement Lookup (HashMap)
Date Solved     : 2024-01-15
Time Taken      : 12 minutes
Attempts        : 1
Revisit         : No
Status          : Solved

TAGS            : #array #hashmap #two-sum #complement-lookup

================================================================================
PROBLEM STATEMENT
================================================================================

Given an array of integers `nums` and an integer `target`, return indices of
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice. You can return the answer in any order.

Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.

Examples:
    Input : nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]              (nums[0] + nums[1] = 2 + 7 = 9)

    Input : nums = [3, 2, 4], target = 6
    Output: [1, 2]              (nums[1] + nums[2] = 2 + 4 = 6)

    Input : nums = [3, 3], target = 6
    Output: [0, 1]              (nums[0] + nums[1] = 3 + 3 = 6)

================================================================================
PATTERN RECOGNITION
================================================================================

Signal Words Identified:
    → "two numbers" + "add up to target" → we need a PAIR with a sum property
    → "return indices" → must track index, not just value
    → No mention of "sorted" → Two Pointers won't apply cleanly
    → n up to 10^4 → O(n) or O(n log n) needed (O(n²) would give 10^8 ops → TLE)

Mental Map:
    "Find two elements that sum to X" → Complement Lookup
    For every element x, I need to find (target - x) in the array.
    If I store every element's INDEX in a dict, lookup becomes O(1).

Pattern Template Applied:
    for each (index, value) in array:
        complement = target - value
        if complement already seen → return [index_of_complement, current_index]
        else → record {value: index} in hashmap

Why not sort + two pointers?
    → We need to return INDICES. Sorting would destroy original indices.
    → We'd need to store original indices before sorting, complicating the code.
    → HashMap is simpler and achieves O(n).

================================================================================
APPROACH 1 — BRUTE FORCE
================================================================================

Intuition:
    Check every pair of indices (i, j) where i < j.
    If nums[i] + nums[j] == target, return [i, j].

Algorithm:
    1. Outer loop: i from 0 to n-2
    2. Inner loop: j from i+1 to n-1
    3. If nums[i] + nums[j] == target → return [i, j]

Time Complexity  : O(n²) — n*(n-1)/2 pairs checked
Space Complexity : O(1)  — no extra space

Verdict: TLE for n = 10^4. But valid for understanding and small inputs.
"""
from typing import Optional


def two_sum_brute(nums: list[int], target: int) -> list[int]:
    """
    Brute Force: Check every pair.
    Time: O(n²) | Space: O(1)
    """
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):           # j starts at i+1 to avoid same element
            if nums[i] + nums[j] == target:
                return [i, j]

    return []   # Defensive; problem guarantees a solution


"""
================================================================================
APPROACH 2 — OPTIMAL (HashMap / Complement Lookup)
================================================================================

Optimization Insight:
    The inner loop in brute force is a LINEAR SEARCH for (target - nums[i]).
    Linear search is slow because we throw away information each iteration.

    Fix: Store what we've seen in a dict → lookup becomes O(1).

    Key decision: Check BEFORE storing.
    Why? If we stored first and then checked, when target = 6 and arr[i] = 3,
    we'd find our own index (stored it just before), violating "same element twice".

Algorithm:
    1. Initialize empty dict: seen = {}
    2. For each (i, num) in enumerate(nums):
       a. complement = target - num
       b. If complement in seen → return [seen[complement], i]
       c. Else → seen[num] = i
    3. Return [] (defensive, never reached per constraints)

Time Complexity  : O(n) — single pass
Space Complexity : O(n) — dict stores up to n (value, index) pairs

Tradeoff:
    O(n) extra space → O(n²) to O(n) time improvement
    This is almost always the correct tradeoff.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Optimal: HashMap complement lookup.
    Time: O(n) | Space: O(n)

    Args:
        nums   : List of integers (2 <= len <= 10^4)
        target : Target sum

    Returns:
        [i, j] where nums[i] + nums[j] == target, i != j

    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    seen = {}  # Maps value → index of first occurrence

    for i, num in enumerate(nums):
        complement = target - num

        # Check BEFORE storing (prevents reusing same index)
        if complement in seen:
            return [seen[complement], i]

        seen[num] = i   # Record this element for future lookups

    return []  # Guaranteed to never reach here per constraints


"""
================================================================================
DRY RUN — Manual Trace
================================================================================

Input: nums = [2, 7, 11, 15], target = 9

i=0, num=2:
    complement = 9 - 2 = 7
    Is 7 in seen? seen={} → NO
    Store: seen = {2: 0}

i=1, num=7:
    complement = 9 - 7 = 2
    Is 2 in seen? seen={2:0} → YES
    Return [seen[2], 1] = [0, 1] ✓

---

Edge Case: nums = [3, 3], target = 6

i=0, num=3:
    complement = 6 - 3 = 3
    Is 3 in seen? seen={} → NO
    Store: seen = {3: 0}

i=1, num=3:
    complement = 6 - 3 = 3
    Is 3 in seen? seen={3:0} → YES
    Return [0, 1] ✓

Why this works: We CHECK before storing.
If we stored first: seen = {3:1} (index 1), then check → found index 1 (same element!) ✗

================================================================================
EDGE CASES CONSIDERED
================================================================================

1. Duplicate values (e.g., [3,3], target=6) → Handled: check before store
2. Negative numbers (e.g., [-1, -2, -3, -4, -5], target=-8) → Works: -3 + -5 = -8
3. Zero values (e.g., [0, 4, 3, 0], target=0) → Works: 0 + 0 = 0 at indices [0,3]
4. Large target (close to 10^9 * 2) → No overflow in Python (arbitrary precision)
5. Minimum array size n=2 → Works correctly

================================================================================
COMPLEXITY SUMMARY
================================================================================

               | Time    | Space   |
---------------|---------|---------|
Brute Force    | O(n²)   | O(1)    |
Optimal (Hash) | O(n)    | O(n)    |

Space-Time tradeoff: O(n) space → O(n²) to O(n) time improvement.
This is the "auxiliary space for faster lookup" pattern.

================================================================================
WHAT I LEARNED
================================================================================

1. "Complement lookup" is a fundamental pattern:
   For any problem asking for a PAIR summing to X:
   → Loop through, check if (X - current) was seen before → O(n)

2. Always check BEFORE storing in HashMap when:
   → The problem says "may not use same element twice"
   → This prevents returning [index, index] as answer

3. "Return indices" is the key signal for HashMap over Two Pointers.
   Two Pointers would require sorting → destroys original indices.

4. Python dict get/set is O(1) average. Internalize this.
   When you see inner loop doing a search → think dict.

5. This SAME insight (complement lookup) appears in:
   → Three Sum (extend with outer loop + two pointers)
   → Subarray Sum Equals K (prefix sum + same complement idea)
   → Pairs with difference K

================================================================================
RELATED PROBLEMS (Ordered by Difficulty)
================================================================================

1. Two Sum II - Input Array Is Sorted (LC 167)    → Two Pointers (sorted, no index issue)
2. Two Sum III - Data Structure Design (LC 170)    → HashMap with add/find operations
3. Three Sum (LC 15)                               → Sort + Two Pointers (extend this pattern)
4. Four Sum (LC 18)                                → Sort + Two outer loops + Two Pointers
5. Subarray Sum Equals K (LC 560)                 → Prefix Sum + Complement Lookup (same HashMap idea)
6. Pairs with Difference K                         → HashMap variant
7. Count Pairs with Given Sum                      → Same HashMap pattern

================================================================================
"""


# ============================================================
# TESTS
# ============================================================

def run_tests():
    """
    Comprehensive test suite for Two Sum.
    Tests both brute force and optimal solution.
    """
    test_cases = [
        # (nums, target, expected)
        ([2, 7, 11, 15],        9,   [0, 1]),
        ([3, 2, 4],             6,   [1, 2]),
        ([3, 3],                6,   [0, 1]),
        ([-1, -2, -3, -4, -5], -8,   [2, 4]),
        ([0, 4, 3, 0],          0,   [0, 3]),
        ([1, 2, 3, 4, 5],       9,   [3, 4]),
    ]

    print("=" * 50)
    print("Testing Two Sum")
    print("=" * 50)

    for i, (nums, target, expected) in enumerate(test_cases):
        result_brute   = two_sum_brute(nums, target)
        result_optimal = two_sum(nums, target)

        brute_ok   = result_brute == expected
        optimal_ok = result_optimal == expected

        status = "PASS ✓" if brute_ok and optimal_ok else "FAIL ✗"
        print(f"Test {i+1}: {status} | nums={nums}, target={target}")

        if not brute_ok:
            print(f"  Brute:   expected {expected}, got {result_brute}")
        if not optimal_ok:
            print(f"  Optimal: expected {expected}, got {result_optimal}")

    print("=" * 50)


if __name__ == "__main__":
    run_tests()
