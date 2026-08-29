# Search Insert Position

**Difficulty:** Easy

## Problem

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

## Examples

**Example 1:**
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**
```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3:**
```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains distinct values sorted in ascending order.
- `-10^4 <= target <= 10^4`

## Approach Ideas

- **Binary Search:** Since the array is sorted and `O(log n)` is required, standard binary search is the way to go.
  - Maintain `low = 0` and `high = n - 1`.
  - While `low <= high`, compute `mid`. If `nums[mid] == target`, return `mid`. If `nums[mid] < target`, move `low = mid + 1`, else `high = mid - 1`.
  - When the loop ends without finding the target, `low` is the correct insertion index (the first position where `nums[low] >= target`).

## Complexity

| Approach      | Time      | Space |
|---------------|-----------|-------|
| Binary Search | O(log n)  | O(1)  |
