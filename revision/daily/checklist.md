# Daily DSA Workflow System

---

## ☀️ Daily Checklist (Every Coding Session)

### Before You Start (5 minutes)
```
[ ] Pick today's FOCUS topic (one pattern or one data structure)
[ ] Open yesterday's problem — can you recall the approach without looking?
[ ] Review your mistake log — did yesterday's mistake show up before?
[ ] Set a timer (Pomodoro: 25 min solve, 5 min break)
```

### Solving a Problem (25–40 minutes per problem)
```
[ ] Read the FULL problem statement (don't rush)
[ ] Write down the constraints — what is n? what are value ranges?
[ ] Identify key signal words → map to a pattern
[ ] Write BRUTE FORCE first (even if slow) — say it out loud
[ ] Analyze brute force: WHERE is it slow? repeated computation? unnecessary work?
[ ] Think of optimization: can HashMap speed up lookup? can sorting help?
[ ] Write the optimal solution
[ ] Dry-run on the given example BY HAND (write it out)
[ ] Dry-run on ONE edge case (empty input, single element, all same, negative nums)
[ ] Test your code
[ ] Write complexity analysis: Time O(?), Space O(?)
[ ] Document using the problem template
```

### After Solving (10 minutes)
```
[ ] Look at top-voted solutions on the platform — is there a cleaner approach?
[ ] If you used a hint or took > 30 min: add to revision/daily/[date]_revisit.md
[ ] Update the README.md progress table (increment solved count)
[ ] Git commit with a meaningful message (see convention in README)
[ ] Write ONE sentence: "Today I learned: ___"
```

### End of Session
```
[ ] Log today's problems in the session log (see format below)
[ ] Rate your understanding: 1 (confused) → 5 (can teach it)
[ ] Flag topics rated 1–2 for weekly revision
```

---

## 📋 Session Log Format

Create a file: `revision/daily/YYYY-MM-DD.md`

```markdown
# Session Log — YYYY-MM-DD

## Focus Today
Pattern: [e.g., Sliding Window]
Topic: [e.g., Variable Window]

## Problems Solved

| # | Problem | Platform | Difficulty | Time Taken | Pattern | Understanding |
|---|---------|----------|------------|------------|---------|---------------|
| 1 | Two Sum | LeetCode | Easy | 12 min | HashMap | 5/5 |
| 2 | Longest Substring K Distinct | LeetCode | Medium | 35 min | Sliding Window | 3/5 |
| 3 | Min Window Substring | LeetCode | Hard | 55 min (hint used) | Sliding Window | 2/5 |

## Key Insights Today
- [Insight 1: e.g., "Variable sliding window shrinks from left when invalid"]
- [Insight 2]

## Mistakes Made
- [Mistake: e.g., "Forgot to check window size before accessing arr[left-k]"]

## Add to Revision (Problems rated < 3/5)
- [ ] Min Window Substring — revisit in 2 days

## Tomorrow's Focus
Pattern: [next pattern to study]
```

---

## 📅 Weekly Checklist (Sunday Evening, 30 minutes)

```
[ ] Count total problems solved this week (target: 10–15)
[ ] Review ALL daily logs from this week
[ ] List patterns practiced this week
[ ] List patterns NOT practiced this week
[ ] Attempt all problems marked for revisit from the week
[ ] Pick your 2 WEAKEST topics → schedule for next week
[ ] Update the main README.md progress dashboard
[ ] Do one TIMED mock problem (45 minutes, no hints, no looking up)
[ ] Commit: "[revision] weekly-review week-N"
```

### Weekly Review Template: `revision/weekly/week_N.md`

```markdown
# Weekly Review — Week N (YYYY-MM-DD to YYYY-MM-DD)

## Stats
- Problems solved: X
- Easy: X | Medium: X | Hard: X
- Patterns covered: [list]
- Patterns missed: [list]

## Strongest Areas This Week
- [Topic] — solved X problems, average understanding 4.5/5

## Weakest Areas This Week
- [Topic] — needs more practice (rated 2/5 twice)

## Problems to Revisit Next Week
- [ ] Problem A (struggled with the shrink condition in sliding window)
- [ ] Problem B (forgot the base case in DP)

## Timed Mock Result
Problem: [name] | Time: X min | Solved? Yes/No | Pattern identified: Yes/No

## Next Week Focus
1. Primary: [Pattern/Topic]
2. Secondary: [Pattern/Topic]
3. Revisit: [2–3 problems from weak list]
```

---

## 🗓️ Monthly Revision Strategy

### End of Month (2 hours)

```
[ ] Solve problems from EACH pattern you've covered (1 problem per pattern, cold)
[ ] No hints, timed (30 minutes each)
[ ] Rate yourself honestly
[ ] Patterns scored < 3/5 → revise notes + solve 3 more problems next week
[ ] Update README.md progress dashboard
[ ] Review your "What I Learned" sections from all daily logs
[ ] Write monthly summary in revision/monthly/month_N.md
```

### Monthly Template: `revision/monthly/month_N.md`

```markdown
# Monthly Review — Month N (Month YYYY)

## Overall Stats
- Total problems solved: X
- LeetCode Easy: X | Medium: X | Hard: X
- Patterns mastered (≥ 4/5): [list]
- Patterns in progress (2–3/5): [list]
- Patterns not started: [list]

## Pattern Mastery Self-Assessment

| Pattern         | Comfort | Problems Solved | Notes                  |
|-----------------|---------|-----------------|------------------------|
| Sliding Window  | 4/5     | 12              | Variable window OK     |
| Two Pointers    | 5/5     | 10              | Solid                  |
| Binary Search   | 3/5     | 8               | On-answer variant weak |
| Tree BFS        | 4/5     | 9               | Level-order solid      |
| DP              | 2/5     | 6               | Need more practice     |

## Interview Readiness
- Can I solve an easy problem in < 15 min? Yes / No
- Can I solve a medium problem in < 30 min? Yes / No
- Can I explain my solution verbally? Yes / No
- Do I know time/space complexity of my solutions? Yes / No

## Next Month Plan
[Outline what to focus on based on above assessment]
```

---

## 🔁 Spaced Repetition Schedule

```
After solving a problem:
  → Revisit after 2 days  (if rating < 4/5)
  → Revisit after 1 week  (if rating 4/5)
  → Revisit after 1 month (if rating 5/5)

This is how memory consolidation works.
The goal is NOT to solve 1000 problems.
The goal is to truly know 150 problems and recognize 15 patterns.
```

---

## ⚡ Problem Difficulty Progression (Per Pattern)

```
Day 1: Solve 2 Easy problems in the pattern
Day 2: Solve 1 Easy (revisit) + 1 Medium
Day 3: Solve 2 Medium problems
Day 4: Attempt 1 Hard (without pressure, just exposure)
Day 5: Revisit 1 Medium you struggled with + 1 new Medium
Day 6: Cold solve: pick any from the pattern without notes
Day 7: Rest or light revision
```

---

## 🧠 Mental Model Warm-Up (First 5 Minutes of Any Session)

Ask yourself these before opening a problem:

```
1. What are the 3 sliding window signals?
   → "contiguous", fixed/variable size, substring/subarray

2. When do I use a min-heap vs max-heap for K-elements problems?
   → K largest: use min-heap (keep K largest by removing smallest)
   → K smallest: use max-heap (keep K smallest by removing largest)

3. What's the binary search template from memory?
   → left, right = 0, n-1 | while left <= right | mid = left+(right-left)//2

4. What is the backtracking template structure?
   → choose → recurse → unchoose

5. What is dp[i][j] for LCS?
   → Length of LCS of text1[:i] and text2[:j]
```

---

*This file lives in: revision/daily/checklist.md | Review every morning*
