class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initially the final position is the last index
        final_position = len(nums) - 1

        # Start with the second last index
        for idx in range(len(nums) - 2, -1, -1):

            # If you can reach the final position from this index
            # update the final position flag
            if idx + nums[idx] >= final_position:
                final_position = idx

        # If we reach the first index, then we can
        # make the jump possible
        return final_position == 0