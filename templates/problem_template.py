"""
================================================================================
PROBLEM TEMPLATE — PROFESSIONAL DSA DOCUMENTATION STANDARD
================================================================================

METADATA
--------
Problem Name    : [Full problem title exactly as on platform]
Platform        : [LeetCode / GFG / Codeforces / HackerRank]
Problem Link    : [URL]
Difficulty      : [Easy / Medium / Hard]
Topic           : [Array / Tree / Graph / DP / etc.]
Pattern         : [Sliding Window / Two Pointers / BFS / DP / etc.]
Date Solved     : [YYYY-MM-DD]
Time Taken      : [e.g., 25 minutes]
Attempts        : [1 / 2 / 3 — be honest, this builds self-awareness]
Revisit         : [Yes / No — Yes if you struggled or used hints]
Status          : [Solved / Partially Solved / Need Review]

TAGS            : #array #hashmap #two-sum #frequency-count

================================================================================
PROBLEM STATEMENT
================================================================================

[Copy the FULL problem statement here. Never skip this.

WHY: When you revise 3 months later, you should NOT need to open the browser.
The file must be self-contained. This is professional documentation practice.]

Example:
    Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you
    may not use the same element twice.

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.

Examples:
    Input : nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9

    Input : nums = [3, 2, 4], target = 6
    Output: [1, 2]

================================================================================
PATTERN RECOGNITION — HOW DID I IDENTIFY THE PATTERN?
================================================================================

[This is the MOST IMPORTANT section for growth. Write your thought process.

Strong engineers don't just solve problems — they know WHY a pattern applies.
This section trains your brain to recognize patterns in future problems.]

Signal Words in This Problem:
    - "two numbers that add up" → pair search → Two Pointers or HashMap
    - "return indices" → we need index tracking, not just values
    - No mention of "sorted" → Two Pointers won't work easily → HashMap

Why HashMap is the right pattern here:
    - We need complement lookup: for each num, we need (target - num)
    - HashMap gives O(1) lookup
    - We need index tracking → store {value: index}

Pattern Template That Applies:
    for each element x:
        if (target - x) exists in seen_map:
            return [seen_map[target - x], current_index]
        seen_map[x] = current_index

================================================================================
APPROACH 1 — BRUTE FORCE
================================================================================

[ALWAYS start with brute force. This shows clear thinking in interviews.
Never skip this section. Even if trivial, document it.]

Intuition:
    Check every pair (i, j) where i != j and see if nums[i] + nums[j] == target.

Algorithm (Step by Step):
    1. Loop i from 0 to n-1
    2. Loop j from i+1 to n-1
    3. If nums[i] + nums[j] == target → return [i, j]
    4. If no pair found → return [] (though problem guarantees one exists)

Time Complexity  : O(n²) — two nested loops, each up to n
Space Complexity : O(1) — no extra space used

Why This is Inefficient:
    For n = 10,000 → 10,000 × 10,000 = 100 million operations.
    This would TLE (Time Limit Exceeded) on most platforms.
"""


def two_sum_brute(nums: list[int], target: int) -> list[int]:
    """
    Brute Force: Check all pairs.
    Time: O(n²) | Space: O(1)
    """
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []  # Problem guarantees a solution exists, this is defensive


"""
================================================================================
APPROACH 2 — BETTER / OPTIMIZED
================================================================================

Intuition (The Insight That Unlocks Optimization):
    Instead of searching for a complement by looping again,
    can we STORE what we've already seen and look it up in O(1)?

    Answer: YES. HashMap (Python dict) gives O(1) average lookup.

    Key Insight:
        For every number x, we need (target - x).
        If (target - x) was seen BEFORE x in the array → we found our pair.
        So we build the map AS we iterate — single pass.

    This is a classic "complement lookup" pattern.

Algorithm (Step by Step):
    1. Create an empty dict: seen = {}
    2. Enumerate through nums: for i, num in enumerate(nums)
    3. Compute complement = target - num
    4. If complement is in seen → return [seen[complement], i]
    5. Else → store seen[num] = i
    6. Continue

    Why store BEFORE the complement check? → We don't. We check FIRST,
    then store. This prevents using the same index twice.

Time Complexity  : O(n) — single pass through array
Space Complexity : O(n) — dict can store up to n elements

Tradeoff:
    We traded O(n) space to gain O(n) time improvement (from O(n²) to O(n)).
    This is almost always the right call unless space is explicitly constrained.
"""


def two_sum_optimal(nums: list[int], target: int) -> list[int]:
    """
    Optimal: HashMap for O(1) complement lookup.
    Time: O(n) | Space: O(n)

    Args:
        nums   : List of integers
        target : Target sum to find

    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
    """
    seen = {}  # Maps value → index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        # Store AFTER checking to avoid using same element twice
        seen[num] = i

    return []  # Defensive return; problem guarantees solution exists


"""
================================================================================
DRY RUN — TRACE THROUGH MANUALLY
================================================================================

[Always do a manual trace. This is what you do on a whiteboard in interviews.
Writing it here builds the habit of mental simulation.]

Input: nums = [2, 7, 11, 15], target = 9

Step 1: i=0, num=2
    complement = 9 - 2 = 7
    Is 7 in seen? seen={} → NO
    Store: seen = {2: 0}

Step 2: i=1, num=7
    complement = 9 - 7 = 2
    Is 2 in seen? seen={2:0} → YES → return [seen[2], 1] = [0, 1] ✓

Output: [0, 1] ← Correct!

---

Edge Case Dry Run: nums = [3, 3], target = 6

Step 1: i=0, num=3
    complement = 6 - 3 = 3
    Is 3 in seen? seen={} → NO
    Store: seen = {3: 0}

Step 2: i=1, num=3
    complement = 6 - 3 = 3
    Is 3 in seen? seen={3:0} → YES → return [0, 1] ✓

Why does this work? Because we CHECK before we STORE.
If we stored first, seen[3] would be overwritten to index 1, losing index 0.

================================================================================
EDGE CASES
================================================================================

[List EVERY edge case you thought of. This shows thoroughness in interviews.]

1. Negative numbers     : nums = [-3, 4, 1], target = 1 → [-3+4=1] → [0,1] ✓
2. Duplicate values     : nums = [3, 3], target = 6 → [0, 1] ✓
3. Large numbers        : Works because Python handles arbitrary integers
4. Target is 0          : nums = [-1, 1], target = 0 → [0, 1] ✓
5. Array of size 2      : Minimum valid input, still works ✓

================================================================================
COMPLEXITY ANALYSIS — FINAL
================================================================================

                | Time      | Space     |
----------------|-----------|-----------|
Brute Force     | O(n²)     | O(1)      |
Optimal (Hash)  | O(n)      | O(n)      |

Space-Time Tradeoff:
    We gave up O(n) extra space to reduce time from O(n²) → O(n).
    This is called "using auxiliary space to speed up lookups."

When NOT to optimize space here:
    If n is guaranteed very small (n < 100), brute force is readable and fine.
    Optimization is about constraints, not ego.

================================================================================
WHAT I LEARNED
================================================================================

[The learning log. Write honestly. This is gold during revision.]

1. The "complement lookup" pattern applies to ANY problem where you need
   to find a PAIR with a certain property. Memorize this mental model.

2. Always check THEN store in HashMap to avoid using same element twice.
   This mistake is common in interviews.

3. "Return indices" is the signal to track indices in the HashMap,
   not just the values.

4. Python's dict (HashMap) is O(1) average for get/set — internalize this.

5. This same pattern appears in: 3Sum, 4Sum, subarray sum = k, pairs with difference k.

================================================================================
RELATED PROBLEMS (Build the Connection Map)
================================================================================

- Two Sum II (sorted array) → Two Pointers instead of HashMap
- Three Sum → Two Pointers + outer loop
- Four Sum → Two Pointers + two outer loops
- Subarray Sum Equals K → Prefix Sum + HashMap (same complement idea)
- Pairs with Difference K → HashMap variant

================================================================================
"""


# ---- TESTS ----
# Always write tests. Professionals test their code.

def run_tests():
    """Test suite for Two Sum."""

    test_cases = [
        # (nums, target, expected_output)
        ([2, 7, 11, 15], 9,  [0, 1]),
        ([3, 2, 4],      6,  [1, 2]),
        ([3, 3],         6,  [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0],   0,  [0, 3]),
    ]

    print("Running Two Sum Tests...")
    print("-" * 40)

    all_passed = True
    for i, (nums, target, expected) in enumerate(test_cases):
        result = two_sum_optimal(nums, target)
        status = "PASS ✓" if result == expected else f"FAIL ✗ (got {result})"
        print(f"Test {i+1}: {status}")
        if result != expected:
            all_passed = False

    print("-" * 40)
    print("All tests passed ✓" if all_passed else "Some tests failed ✗")


if __name__ == "__main__":
    run_tests()
