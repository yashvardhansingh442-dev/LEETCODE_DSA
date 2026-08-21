# 91. Decode Ways

**Difficulty:** Medium
**Tags:** `#DP` `#String` `#Decoding`
**Link:** https://leetcode.com/problems/decode-ways/

## Problem

You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

```
"1" -> 'A'
"2" -> 'B'
...
"25" -> 'Y'
"26" -> 'Z'
```

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (`"2"` and `"5"` vs `"25"`).

For example, `"11106"` can be decoded into:

- `"AAJF"` with the grouping `(1, 1, 10, 6)`
- `"KJF"` with the grouping `(11, 10, 6)`
- The grouping `(1, 11, 06)` is invalid because `"06"` is not a valid code (only `"6"` is valid).

**Note:** there may be strings that are impossible to decode.

Given a string `s` containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return `0`.

The test cases are generated so that the answer fits in a 32-bit integer.

## Examples

**Example 1:**
```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

**Example 2:**
```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

**Example 3:**
```
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
In this case, the string is not a valid encoding, so return 0.
```

## Constraints

- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zero(s).

## Edge Cases to Watch

- Leading `'0'` in the whole string → invalid, return `0` immediately
- A `'0'` that isn't part of a valid `"10"` or `"20"` → dead end
- Strings like `"100"`, `"10"`, `"0"` — most common trip-ups in interviews

## Approach

DP where `dp[i]` = number of ways to decode `s[0:i]`. At each position, check:
1. Single digit (`s[i] != '0'`) → add `dp[i-1]`
2. Two digit (`10 <= int(s[i-1:i+1]) <= 26`) → add `dp[i-2]`

Can be optimized to O(1) space using two rolling variables instead of a full DP array.

**Time:** O(n) | **Space:** O(1) (optimized)
