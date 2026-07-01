class Solution:
    def removeDuplicates(self, nums):
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)
