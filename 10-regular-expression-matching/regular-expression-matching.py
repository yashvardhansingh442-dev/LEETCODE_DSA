class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] = does s[:i] match p[:j]?
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Empty string vs patterns like a*, a*b*, a*b*c* ...
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Case 1: '*' matches zero of the preceding char
                    dp[i][j] = dp[i][j - 2]
                    # Case 2: '*' matches one or more, if the preceding char fits s[i-1]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    # Plain char or '.', must match the current char
                    if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]