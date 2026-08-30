class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []
        
        def backtrack(start):
            if len(path) == k:
                result.append(path[:])
                return
            
            # Pruning: if remaining numbers aren't enough to fill path, stop early
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1)
                path.pop()
        
        backtrack(1)
        return result
