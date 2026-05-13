class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for s in range(len(nums) - 1):
            if nums[s] > nums[s + 1]:
                return s

        return len(nums) - 1