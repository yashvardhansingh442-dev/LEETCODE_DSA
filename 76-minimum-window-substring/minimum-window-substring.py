from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        missing = len(t)  # total chars still needed
        
        left = 0
        start, end = 0, 0  # best window found
        
        for right, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            
            # valid window found, shrink from left
            while missing == 0:
                if end == 0 or right - left < end - start:
                    start, end = left, right
                
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        
        return s[start:end]
