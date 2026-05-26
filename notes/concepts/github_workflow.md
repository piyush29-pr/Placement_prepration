# GitHub Best Practices for DSA Repository

---

## Git Workflow: The Professional Standard

### Initial Repository Setup

```bash
# 1. Create repo on GitHub (initialize with README)
# 2. Clone locally
git clone https://github.com/YOUR_USERNAME/dsa-mastery.git
cd dsa-mastery

# 3. Set up the folder structure
mkdir -p data_structures/{arrays,linked_lists,stacks,queues,trees,graphs,heaps,tries,hash_maps}
mkdir -p algorithms/{sorting,searching,recursion,backtracking,greedy,dynamic_programming}
mkdir -p patterns/{sliding_window,two_pointers,binary_search,prefix_sum,tree_bfs,tree_dfs,top_k_elements,dynamic_programming,backtracking,graphs}
mkdir -p notes/{concepts,complexity,interview_tips,mistakes,pattern_guides}
mkdir -p templates revision/{daily,weekly,monthly} practice/{leetcode,codeforces} contests cheatsheets

# 4. Add .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
.env
.venv/
venv/
*.egg-info/
.DS_Store
.idea/
.vscode/
*.pyc
EOF

# 5. Initial commit
git add .
git commit -m "init: repository structure with all topic folders"
git push origin main
```

---

## Commit Strategy

### The Golden Rule
```
One logical change = one commit.
Never commit broken code.
Never mix multiple topics in one commit.
```

### Commit Message Format (Follow This Exactly)
```
[scope] action: short description

[scope]   = topic area: array, tree, dp, graph, pattern, revision, etc.
action    = add, fix, update, refactor, remove
description = what changed and why (present tense, max 72 chars)

Examples of GOOD commits:
  [array] add: maximum product subarray - bottom-up DP approach
  [tree] add: lowest common ancestor - iterative DFS approach
  [dp] add: coin change problem - BFS + top-down memoization
  [pattern] add: sliding window template with variable window notes
  [revision] update: week-3 review - marked LCS as weak area
  [note] add: binary search on answer pattern explanation
  [fix] tree: null root edge case in inorder traversal
  [readme] update: progress table - 45 problems solved

Examples of BAD commits (never do these):
  "update"
  "add problem"
  "fix bug"
  "wip"
  "done"
  "asdfgh"
```

### Daily Commit Workflow
```bash
# After solving a problem:
git status                          # See what changed
git add patterns/sliding_window/longest_substring_k_distinct.py
git commit -m "[sliding-window] add: longest substring k distinct chars - O(n) variable window"
git push origin main

# After updating revision notes:
git add revision/daily/2024-01-15.md
git commit -m "[revision] add: daily session log 2024-01-15 - 3 sliding window problems"
git push origin main

# After updating README:
git add README.md
git commit -m "[readme] update: progress table - sliding window 8/20 complete"
git push origin main
```

---

## Branch Strategy

For a solo learning repo, keep it simple. But learn the professional way:

```bash
# Main branch = always clean, always working
main

# Feature branches = for adding new topics
git checkout -b feature/add-graph-section
# ... work on it ...
git add .
git commit -m "[graph] add: BFS template + number of islands solution"
git checkout main
git merge feature/add-graph-section
git branch -d feature/add-graph-section
git push origin main

# Why branch even for solo?
# 1. Trains the professional habit
# 2. Keeps main always clean
# 3. You can experiment in a branch without breaking main
# 4. Recruiters see your workflow in git log
```

---

## File Naming Convention

```
Rule: Names must be self-documenting. No need to open the file to know its content.

Format: [problem_name]_[approach_if_multiple].py

Examples:
  two_sum.py
  two_sum_brute.py              ← if storing brute force separately
  longest_substring_k_distinct.py
  maximum_sum_subarray_k.py
  binary_search_rotated_array.py
  merge_intervals.py
  word_break_memo.py            ← memoization approach
  word_break_dp.py              ← bottom-up DP approach
  kth_largest_heap.py

Platform-based (in practice/leetcode/):
  lc_001_two_sum.py             ← LeetCode problem 1
  lc_053_max_subarray.py        ← LeetCode problem 53
  lc_076_min_window_substring.py

This naming makes the folder self-indexing.
```

---

## Repository Hygiene (Non-Negotiables)

### Keep These Clean At All Times
```
1. No empty files
   Every file must have content. Delete placeholder files.

2. No duplicate solutions without documentation
   If you have two approaches, document BOTH in the same file with clear sections.

3. No commented-out junk code
   If you want to preserve an approach, document it properly. Don't comment out blocks.

4. No print("test") left in code
   Use proper test functions (see template).

5. Update README.md every week
   A stale README signals an abandoned repo.
```

---

## GitHub Actions (Automation — Add Later)

### Auto-validate Python files on push
Create `.github/workflows/validate.yml`:

```yaml
name: Validate Python Files

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install pyflakes

      - name: Check Python syntax
        run: |
          find . -name "*.py" -not -path "./.git/*" | xargs python -m pyflakes
          echo "All Python files validated ✓"

      - name: Run tests
        run: |
          find . -name "*.py" -not -path "./.git/*" | xargs -I {} python {} || true
          echo "Test run complete"
```

### When to add GitHub Actions:
```
Beginner  → Skip automation, focus on content
Intermediate → Add syntax validation (above)
Advanced  → Add auto-generated progress stats, LeetCode sync
```

---

## README Badges (Add Once You Have Content)

```markdown
<!-- Add these to the top of your README.md -->

![Problems Solved](https://img.shields.io/badge/Problems_Solved-45-blue)
![Python](https://img.shields.io/badge/Language-Python_3.11-yellow)
![Patterns](https://img.shields.io/badge/Patterns_Covered-8-green)
![Last Updated](https://img.shields.io/badge/Last_Updated-January_2024-orange)

<!-- LeetCode profile badge (get from LeetCode profile settings) -->
[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-orange)](https://leetcode.com/YOUR_USERNAME)
```

---

## What a Recruiter Sees When Visiting Your GitHub

```
Timeline of a recruiter's 90-second repo evaluation:

0:00 — Land on repo page
       → Is the README professional? Do I understand the purpose immediately?
       → Checks: Last commit date (is it recent?)

0:15 — Scroll README
       → Is there a progress tracker? Shows systematic approach.
       → Is there a roadmap? Shows planning ability.
       → Are there code examples? Shows technical depth.

0:30 — Click on a folder (e.g., patterns/)
       → Are files named clearly?
       → Does the folder structure make sense?

0:45 — Open one Python file
       → First 10 lines: Is the metadata/header professional?
       → Does it have complexity analysis?
       → Is the code clean and readable?

1:00 — Check commit history
       → Consistent? (daily/weekly commits > monthly bursts)
       → Meaningful messages?

1:30 — Decision: "This candidate is serious" or "Standard repo, nothing special"

YOUR GOAL: Make it obvious by 0:30 that this repo is different.
```

---

*Lives in: notes/concepts/github_workflow.md*
*Read before setting up repo. Reference when confused about git workflow.*
