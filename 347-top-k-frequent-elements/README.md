<h2><a href="https://leetcode.com/problems/top-k-frequent-elements/">347. Top K Frequent Elements</a></h2>

<h3>Medium</h3>

<hr>

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

### Example 1

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

### Example 2

```
Input: nums = [1], k = 1
Output: [1]
```

### Example 3

```
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
```

### Constraints

* `1 <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`
* `k` is in the range `[1, the number of unique elements in the array]`.
* It is guaranteed that the answer is unique.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where `n` is the array's size.

---

## Approach

**Pattern: Hash Map + Bucket Sort.**

Sorting the elements by frequency would cost `O(n log n)`, which the follow-up rules out. The key observation is that a frequency can never exceed `n`, so frequencies can be used directly as array indices.

1. **Count frequencies.** Build a hash map from each number to how many times it appears.
2. **Bucket by frequency.** Create an array of `n + 1` buckets, where bucket `i` holds all numbers that appear exactly `i` times.
3. **Collect from the top.** Walk the buckets from the highest frequency down to the lowest, adding numbers to the result until `k` elements have been collected.

Since each step is a single pass over the data, no sorting is needed and the whole process runs in linear time.

An alternative is a min-heap of size `k`, which gives `O(n log k)`. It also beats `O(n log n)`, but bucket sort is the tighter `O(n)` solution.
