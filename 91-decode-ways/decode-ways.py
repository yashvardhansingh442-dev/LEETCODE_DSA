class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        prev2, prev1 = 1, 1  # dp[i-2], dp[i-1]
        
        for i in range(1, n):
            current = 0
            
            # single digit check (s[i] != '0')
            if s[i] != '0':
                current += prev1
            
            # two digit check (10-26)
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
            
            if current == 0:
                return 0  # invalid encoding, no need to continue
            
            prev2, prev1 = prev1, current
        
        return prev1
