class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            nums[i] = nums[i] ^ nums[j]
        return nums[i]
        