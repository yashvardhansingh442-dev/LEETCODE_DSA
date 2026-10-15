# Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium

## Problem

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

## Examples

**Example 1:**
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

**Example 2:**
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

**Example 3:**
```
Input: nums = [], target = 0
Output: [-1,-1]
```

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

## Approach

**Two Binary Searches ("Lower Bound" / "Upper Bound"):** Since the array is sorted and `O(log n)` is required, run binary search twice:

1. **Find the leftmost index:** Search for the first position where `nums[i] >= target`. If that position holds `target`, it's the start of the range.
2. **Find the rightmost index:** Search for the first position where `nums[i] > target`, then subtract 1. If that adjusted position holds `target`, it's the end of the range.

If either search reveals `target` isn't actually present at the found index (or the array is empty), return `[-1, -1]`.



## Complexity

| Approach                  | Time      | Space |
|-----------------------------|-----------|-------|
| Two Binary Searches         | O(log n)  | O(1)  |
