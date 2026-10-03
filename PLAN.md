# The Plan: 20-Day Python Coding Fluency ("Python Gym Before LeetCode")

**Goal:** open a blank editor, read an English requirement, and build working Python without freezing.
**Not the goal:** watching explanations and saying "I understand." Understanding counts for nothing here. Only code you write yourself counts.

---

## 1. The core skill we train every single day

```
ENGLISH REQUIREMENT
  -> understand it
  -> inputs?  -> output?
  -> small steps (manual walk-through)
  -> pseudocode
  -> Python
  -> run / test
  -> debug
```

Decomposition checklist (asked on every problem until it is automatic):
1. What information do I receive? (inputs)
2. What must I produce? (output)
3. What would I do by hand?
4. Do I need: variables / if-elif / loop / list / dict / set / function?
5. What are 3 test cases, including one edge case?

## 2. How a session works

| Step | What happens |
|------|--------------|
| Flash drill | Random syntax questions, answered from memory (no lookup). |
| Micro block | 20-40 one-operation exercises. |
| Small programs | 5-10 programs mixing a few concepts. |
| Blank-file challenge | "START WITH A COMPLETELY EMPTY FILE." Requirement only. |
| Larger problem | 1-3 real requirements, no concept labels. |
| Daily report | Scores, 3 automatic skills, 3 struggles, mistakes to review. |

**Where the work lives:** you write code in `dayNN/` files in this repo. You paste or tell me when it's done. I run it, test it, and review it. Everything is committed and pushed to GitHub after every change.

## 3. The difficulty ladder (per concept)

1. **Micro**: one operation ("append 5 to a list")
2. **Combination**: 2-3 operations ("collect numbers, print the largest")
3. **Small program**: several concepts ("shopping cart total")
4. **Real requirement**: English only, you choose the tools ("parking garage: $5 first hour, $3 after, cap $20")
5. **Interview**: unfamiliar requirement, no hints, full process

## 4. Rules I follow as your coach

- **No answers up front.** You write first. Always.
- **Stuck ladder:** 
  - Hint 1 is conceptual. 
  - Hint 2 is syntax. 
  - Hint 3 is a code skeleton. 
  - Only then the solution. 
- **Rewrite rule:** if I show a solution, it doesn't count. "Close it. Rewrite from memory." Then you get a variation.
- **Don't rescue early.** If you say "I don't know," I ask: what do we receive? what do we return? what would you do manually?
- **Fail -> repeat the concept. Succeed -> change the context** (grades, salaries, distances, temperatures, scores, sensor readings...) so syntax becomes context-independent.
- **No memorizing programs.** I change names, numbers, edge cases, and order every time.
- **Error log** (`ERROR_LOG.md`): every mistake is categorized and reviewed at the start of the next day.
- **Volume adapts:** struggling -> easier but more reps. Cruising -> harder.

## 5. The 20 days

| Days | Theme | What you'll be able to do |
|------|-------|---------------------------|
| 1-3 | Basic code construction | variables, input/output, arithmetic, comparisons, if/elif/else, functions, return. Age check, ticket pricing, grades, password validation, delivery fee. |
| 4-6 | Conditions + real-world logic | English rules -> conditionals. Pizza, coffee, parking, Uber, hotel, tax, shipping, insurance, and a dozen more. |
| 7-9 | Loops + repetition | print/sum/max/count/average/search/filter/build lists, then carts, votes, transactions, sensors. |
| 10-11 | Lists / array thinking | `nums[i]`, `[-1]`, `len`, `append`, `pop`, `remove`, `sort`, `sorted`; the three loop styles; find/filter/transform/dedupe/reverse/second-largest. |
| 12-13 | Dicts + sets | `freq[x] = freq.get(x, 0) + 1`, `in`, `set()`, `add`; word counts, inventory, duplicates, grouping, lookups. |
| 14 | Functions | split programs into `calculate_tax`, `calculate_discount`, `validate_input`... |
| 15 | Nested logic + program building | ATM, shopping cart, restaurant, grade system. |
| 16 | Debugging | broken programs, no bug named: syntax, type, index, logic, infinite loop, off-by-one, mutation. |
| 17 | English -> code | requirements only; YOU write pseudocode first. |
| 18 | Mini projects | 5-10 programs, 5-20 min each, no solutions up front. |
| 19 | Random interview drills | no topic labels; you pick the tools. |
| 20 | Fluency exam | 6 timed rounds, 60 sec up to a full interview-style problem (explain, I/O, steps, pseudocode, code, test, debug, complexity). |

**After Day 20 only:** Coding fluency -> Easy LeetCode -> Medium LeetCode -> interview problems. By then your brain is on "which pattern?" and not "how do I write a for loop?"

## 6. Mastery levels (goal: Level 7 on every topic)

1. Recognize 2. Explain 3. Write with a hint 4. Write independently 5. Use in an unfamiliar problem 6. Debug it 7. Use under time pressure

A topic is **mastered at Level 7, never from understanding an explanation.**

## 7. Daily report (end of every session)

Scores /100: Python Fluency, Translation (English -> code), Debugging, Independent Coding, Speed.
Plus: 3 things you now write automatically, 3 you still struggle with, mistakes to review tomorrow, concepts needing repetition.

## 8. Repo layout and GitHub workflow

```
PLAN.md        this file
PROGRESS.md    daily scores + mastery tracking
ERROR_LOG.md   mistake database
day01/ ... day20/   exercises and your solutions
```

Every change (new exercises, your solutions, log updates, reports) is committed and pushed to `origin/main`.
