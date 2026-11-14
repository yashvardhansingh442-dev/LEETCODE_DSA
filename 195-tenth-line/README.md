# 195. Tenth Line

[LeetCode Link](https://leetcode.com/problems/tenth-line/) | **Difficulty:** Easy | **Topic:** Shell (Bash)

## Problem

Given a text file `file.txt`, print just the 10th line of the file.

## Example

Assume that `file.txt` has the following content:

```
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
```

Your script should output the tenth line, which is:

```
Line 10
```

## Notes

1. If the file contains fewer than 10 lines, what should you output?
   **Answer:** Nothing. All solutions below print nothing in that case.
2. There are at least three different solutions. Try to explore all possibilities.

## Solutions

### 1. sed

```bash
sed -n '10p' file.txt
```

`-n` turns off automatic printing, and `10p` prints only line 10.

### 2. awk

```bash
awk 'NR==10' file.txt
```

`NR` is the current line number. awk prints a line when the condition is true.

### 3. tail + head

```bash
tail -n +10 file.txt | head -n 1
```

`tail -n +10` outputs from line 10 to the end, and `head -n 1` keeps only the first of those lines.

## Solution file

`solution.sh`
