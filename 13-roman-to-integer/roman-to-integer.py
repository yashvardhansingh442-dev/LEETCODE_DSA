class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        prev_max = 0
        for ch in reversed(s):
            val = values[ch]
            if val < prev_max:
                total -= val
            else:
                total += val
                prev_max = val
        return total