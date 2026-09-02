# Word Search

**Difficulty:** Medium

## Problem

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Examples

**Example 1:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consist of only lowercase and uppercase English letters.

**Follow-up:** Could you use search pruning to make your solution faster with a larger board?

## Approach

**Backtracking (DFS):** For each cell in the board matching `word[0]`, start a DFS attempting to match the rest of the word by exploring the 4 neighboring directions (up, down, left, right).

- Mark the current cell as visited (e.g., temporarily overwrite it with a sentinel character like `'#'`) before recursing, and restore it afterward (backtrack) so other paths can reuse the cell.
- If the current cell's character doesn't match the current character in `word`, or the cell is out of bounds / already visited, return `false` immediately.
- If we've matched all characters in `word`, return `true`.

**Search Pruning (Follow-up):** A few optimizations help significantly on larger boards:
- **Frequency pre-check:** Count character frequencies in `board` and in `word` upfront. If `word` needs more of some character than the board contains, return `false` immediately without searching.
- **Direction ordering by frequency:** Precompute frequency counts for board characters; if `word[-1]` is rarer than `word[0]`, reverse the word before searching (matching from the rarer end fails faster).
- **Bitmask/bitset instead of mutating the board:** Use a visited bitmask instead of mutating the grid in place, avoiding potential edge-case bugs if the board must remain unmodified between calls (useful for concurrent searches).


```

## Complexity

| Approach              | Time                  | Space |
|------------------------|------------------------|-------|
| Backtracking (DFS)     | O(m * n * 4^L)         | O(L)  |

Where `m x n` is the board size, `L` is the length of `word`, and `4^L` bounds the branching factor of the DFS at each starting cell (in practice much smaller due to early termination on mismatches). Space is O(L) for the recursion stack.
