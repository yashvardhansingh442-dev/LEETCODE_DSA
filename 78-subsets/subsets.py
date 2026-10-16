class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        
        def backtrack(start):
            result.append(path[:])  # every state is a valid subset
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return result
