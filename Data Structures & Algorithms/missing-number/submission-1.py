class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for s in range(n):
            if nums[s] != s:
                return s
        return n