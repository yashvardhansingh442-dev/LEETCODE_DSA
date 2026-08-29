# Trapping Rain Water

**Difficulty:** Hard

## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

## Examples

**Example 1:**
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2:**
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Approach Ideas

- **Brute Force:** For each bar, find the max height to its left and to its right, then the water trapped above it is `min(leftMax, rightMax) - height[i]` (if positive). O(n²) time.
- **Dynamic Programming (Prefix/Suffix Max):** Precompute `leftMax[i]` and `rightMax[i]` arrays in O(n) time, then sum `min(leftMax[i], rightMax[i]) - height[i]` across all indices. O(n) time, O(n) space.
- **Two Pointers (Optimal):** Use `left` and `right` pointers starting at the ends, tracking `leftMax` and `rightMax` on the fly. Move the pointer on the side with the smaller max inward, accumulating trapped water as you go. O(n) time, O(1) space.
- **Monotonic Stack:** Maintain a decreasing stack of indices. When a taller bar is found, pop and compute the water trapped between the popped bar and the new taller bar using the width and bounded height. O(n) time, O(n) space.

## Complexity

| Approach              | Time  | Space |
|-----------------------|-------|-------|
| Brute Force           | O(n^2)| O(1)  |
| DP (Prefix/Suffix Max)| O(n)  | O(n)  |
| Two Pointers          | O(n)  | O(1)  |
| Monotonic Stack       | O(n)  | O(n)  |
