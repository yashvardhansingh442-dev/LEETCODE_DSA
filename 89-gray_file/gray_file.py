class Solution:
    def grayCode(self, n: int) -> list[int]:
        res = [0]
        for i in range(n):
            # mirror the list, setting the new highest bit on the mirrored half
            for x in reversed(res):
                res.append(x | (1 << i))
        return res
