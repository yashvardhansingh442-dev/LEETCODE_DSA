
# 23. Merge k Sorted Lists

## Problem
You are given an array of `k` linked-lists `lists`, each linked-list sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

**Example 1:**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Example 2:**
```
Input: lists = []
Output: []
```

**Example 3:**
```
Input: lists = [[]]
Output: []
```

## Constraints
- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order.
- Sum of `lists[i].length` will not exceed `10^4`.

---

## Pattern
This is the natural extension of **LC 21 (Merge Two Sorted Lists)** to `k` lists. Brute-force pairwise merging works but the ordering of merges matters a lot for complexity — this is the classic setup for either a **min-heap** or **divide and conquer**.


Let me know when you want the code (and which approach) — heap, divide & conquer, or both.
