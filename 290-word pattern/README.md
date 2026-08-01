## 290. Word Pattern

**Difficulty:** Easy
**Topics:** Hash Table, String
**Companies:** —

---

### Problem

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Follow means a **full match**, such that there is a **bijection** between a letter in `pattern` and a non-empty word in `s`. Specifically:

- Each letter in `pattern` maps to exactly one unique word in `s`.
- Each unique word in `s` maps to exactly one letter in `pattern`.
- No two letters map to the same word, and no two words map to the same letter.

---

### Examples

**Example 1:**
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```
`'a' -> "dog"`, `'b' -> "cat"`

**Example 2:**
```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

**Example 3:**
```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

---

### Constraints

- `1 <= pattern.length <= 300`
- `pattern` contains only lower-case English letters.
- `1 <= s.length <= 3000`
- `s` contains only lowercase English letters and spaces `' '`.
- `s` has no leading/trailing spaces; words separated by a single space.

---

### Approach

- Split `s` into words. If `len(words) != len(pattern)` → false immediately (length mismatch = no bijection).
- Use two hashmaps: `char -> word` and `word -> char`.
- Walk through `pattern[i]` and `words[i]` together:
  - If `char` already mapped, check it maps to the current `word`; if not, false.
  - If `word` already mapped, check it maps to the current `char`; if not, false.
  - Otherwise, insert both mappings.
- If loop completes without conflict → true.

This is the classic **bijection / isomorphic mapping** pattern (same family as Isomorphic Strings, LC 205).

---

### Complexity

- **Time:** O(n) — n = length of pattern / number of words
- **Space:** O(n) — for the two hashmaps

---

### Edge Cases

- Length mismatch between pattern and word count → false
- Pattern longer than distinct words needed, or vice versa (many-to-one) → caught by dual hashmap check
- Single character pattern / single word

---
