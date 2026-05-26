# Interview-Focused Engineering Insights

---

## What Interviewers ACTUALLY Evaluate (Not What You Think)

> Most candidates prepare to SOLVE problems.
> Strong candidates prepare to THINK out loud.
> These are fundamentally different skills.

---

## The 5 Dimensions Interviewers Score You On

### 1. Problem Decomposition (25%)
```
What they look for:
  → Do you read the problem carefully before coding?
  → Do you identify constraints and edge cases first?
  → Do you clarify ambiguous requirements?

What weak candidates do:
  → Jump to code immediately
  → Assume input is always valid
  → Never ask clarifying questions

What strong candidates do:
  → Repeat the problem back in their own words
  → Ask: "Can the array contain duplicates? Can values be negative?"
  → Draw examples on paper/whiteboard before coding
  → State the pattern they recognize: "This looks like a sliding window problem"
```

### 2. Communication (25%)
```
What they look for:
  → Do you think out loud or sit in silence?
  → Can you explain WHY, not just WHAT?
  → Do you narrate your optimization journey?

What weak candidates do:
  → Code silently for 20 minutes then show result
  → Say "I'll use dynamic programming" without explaining why
  → Get stuck and go completely silent

What strong candidates do:
  → "I'm going to start with a brute force to understand the problem..."
  → "The bottleneck here is the inner loop. Can I eliminate it with a HashMap?"
  → "I see two approaches. Let me explain the tradeoff..."
  → When stuck: "I know I need to reduce this inner loop. Let me think about
     what data structure gives O(1) lookup..."
```

### 3. Coding Quality (20%)
```
What they look for:
  → Clean variable names (not i,j,k for everything)
  → Proper function structure
  → No dead code
  → Handles edge cases

What weak candidates do:
  → Variable names: a, b, x, temp
  → Everything in one giant function
  → No edge case handling

What strong candidates do:
  → def find_longest_substring(s: str, k: int) -> int:
  → Helper functions for complex logic
  → Comment non-obvious decisions (not obvious ones)
  → Test edge cases before declaring done
```

### 4. Problem-Solving Approach (20%)
```
What they look for:
  → Can you go from brute force to optimal systematically?
  → Do you know multiple approaches?
  → Do you know when to stop optimizing?

What weak candidates do:
  → Try to jump to optimal immediately (and often get it wrong)
  → Only know one approach
  → Over-optimize simple problems

What strong candidates do:
  → "Brute force is O(n²). Let me think about how to reduce that."
  → "I see two approaches: sorting + binary search (O(n log n)) or
     a HashMap approach (O(n) time, O(n) space). Given n can be 10^6,
     both are acceptable. I'll go with HashMap since it's slightly simpler."
```

### 5. Verification (10%)
```
What they look for:
  → Do you test your solution?
  → Do you dry-run on the example?
  → Do you check edge cases?

What weak candidates do:
  → Submit immediately after writing code
  → Never trace through manually

What strong candidates do:
  → "Let me trace through the example: [walks through step by step]"
  → "Edge cases: empty array, single element, all same values, negative numbers..."
  → "I should also check: what if k > len(s)?"
```

---

## What Recruiters Notice in Your GitHub Profile

### Green Contribution Graph
```
WHY IT MATTERS:
  Consistency > intensity. 10 commits/week for 6 months > 300 commits in one week.
  Recruiters check: Are you consistently practicing?

HOW TO BUILD IT:
  Commit EVERY day you code, even if it's just:
    - Adding one problem
    - Fixing a comment
    - Updating the README progress table
    - Adding a note to your pattern cheatsheet

MISTAKE: Committing everything in one burst and then disappearing.
```

### Commit Message Quality
```
WHAT RECRUITERS SEE:
  The commit history tells the story of your engineering discipline.

POOR COMMITS (red flag):
  "update"
  "fix"
  "add stuff"
  "wip"
  "asdfgh"

GOOD COMMITS (green flag):
  "[array] add: two-sum hashmap approach O(n) time O(n) space"
  "[dp] add: 0-1 knapsack bottom-up tabulation with space optimization"
  "[tree] fix: inorder traversal - handle null root edge case"
  "[pattern] add: sliding window template + 3 solved problems"
  "[revision] weekly: review session week-4, updated weak areas list"

RULE: Your commit message should make sense to a stranger 6 months from now.
```

### README Quality
```
WHAT RECRUITERS SEE:
  A professional README = you care about documentation = you think like an engineer.

Must have:
  - Clear repository purpose
  - Progress tracking table (shows you're systematic)
  - Pattern index (shows conceptual understanding, not just grinding)
  - Consistent structure

MISTAKE: Empty README or "This is my DSA practice repo. Work in progress."
That's the repo of someone who doesn't think about the reader.
```

### Code Quality in Files
```
What separates your repo from 10,000 other "DSA repos":

1. COMMENTS ON WHY, NOT WHAT
   Bad:  # Loop through array
   Good: # We check BEFORE storing to prevent using the same index twice

2. COMPLEXITY ANALYSIS IN EVERY FILE
   # Time: O(n) | Space: O(1)
   This shows you understand what you wrote.

3. MULTIPLE APPROACHES IN ONE FILE
   Brute force → Optimal shows progression of thought.

4. DRY RUN SECTION
   Tracing through an example manually in comments.
   This is exactly what happens on a whiteboard.
```

---

## What Separates Average Candidates from Strong Ones

### In Coding Interviews

```
Average Candidate:
  → Knows the solution
  → Codes it up
  → It works
  → Done

Strong Candidate:
  → Identifies the pattern (and says WHY it applies)
  → States brute force with complexity
  → Identifies the bottleneck
  → Explains the optimization insight
  → Codes the optimal solution
  → Dry-runs it on the example
  → Checks edge cases
  → States final complexity
  → Mentions possible follow-up optimizations

The difference: Strong candidates treat the interview as a TECHNICAL DISCUSSION,
not a test. They invite the interviewer into their thinking.
```

### In DSA Repositories

```
Average Repo:
  → 200 files named solution.py
  → No comments
  → No structure
  → No documentation
  → Green squares everywhere (daily grind without depth)

Strong Repo:
  → 80 problems, each with full documentation
  → Pattern-based organization
  → Brute force → optimal progression
  → Complexity analysis
  → Learning notes
  → Daily logs showing a systematic approach
  → Shows DEPTH over breadth
```

---

## The FAANG Preparation Mindset

### What FAANG Looks For (Beyond Algorithms)

```
1. SCALABILITY THINKING
   Don't just solve for n = 10. Think about n = 10^9.
   "This O(n²) solution would TLE for large inputs. The O(n) HashMap
   approach scales to any input size."

2. EDGE CASE AWARENESS
   Empty input, single element, duplicates, negatives, overflow.
   Mention these proactively. Don't wait to be asked.

3. CODE CLARITY
   Google's codebase has millions of lines written by hundreds of engineers.
   They need code that others can read and maintain.
   Write code that's clear, not clever.

4. COMMUNICATION OF UNCERTAINTY
   "I'm not 100% sure about the complexity here. Let me think..."
   Better than silence or false confidence.

5. ADAPTABILITY
   When the interviewer gives a hint, take it gracefully.
   "Oh, that's a great point. If I use a min-heap here instead..."
   Shows you can learn quickly — critical for engineering teams.
```

### Realistic Preparation Numbers

```
For Tier 1 companies (FAANG/equivalent):
  - Minimum: 200+ problems (40 Easy, 120 Medium, 40 Hard)
  - All 14 major patterns practiced with 10+ problems each
  - Can solve a medium in 20–25 minutes under pressure
  - Can explain ANY solution verbally without code

For Tier 2 companies (Mid-size tech):
  - Minimum: 100–150 problems
  - Core patterns practiced
  - Can solve easy in 10 min, medium in 30 min

For Service-based companies:
  - 50–75 problems
  - Basic patterns: arrays, strings, sorting, basic DP
  - GFG Top 50 list is standard

FOR ALL: Quality > Quantity. Understanding 75 problems deeply beats
grinding 300 problems without internalization.
```

---

## The One Thing Most Candidates Miss

```
VERBAL EXPLANATION is a separate skill from CODING.

You can solve a problem perfectly in private and fail to explain it in an interview.

PRACTICE: After solving any problem, close the editor.
Look at a wall. Explain the solution out loud in 2 minutes.
Include: pattern, brute force, optimization insight, complexity.

If you can't explain it out loud, you don't know it well enough.
This is how interviewers expose shallow understanding.
```

---

## Common Interview Mistakes (Avoid These)

```
❌ Jumping to code without clarifying requirements
   Fix: Spend 2-3 min understanding the problem first

❌ Optimizing too early before a working solution exists
   Fix: Working brute force > broken optimal

❌ Saying "I know this, it's [pattern name]" without explaining why
   Fix: "This looks like X because [signal words] and [constraint]"

❌ Panicking when stuck and going silent
   Fix: "I'm not seeing the optimization immediately. Let me think about
   what data structure could help here..."

❌ Not testing edge cases
   Fix: Always ask "What about empty input? What about one element?"

❌ Complicated variable names or overly clever one-liners
   Fix: Write code for the reader, not for yourself

❌ Saying "my solution is optimal" without proving it
   Fix: State the complexity and WHY it can't be improved further

❌ Changing approach completely when interviewer gives a hint
   Fix: Build on your existing solution, don't start over
```

---

*This file lives in: notes/interview_tips/README.md*
*Review this the evening before every interview and every week*
