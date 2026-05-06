class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        for s in range(len(nums)):
            curSum = nums[s]
            for x in range(s + 1, len(nums)):
                if nums[x] <= nums[x - 1]:
                    break
                curSum += nums[x]
            res = max(res, curSum)
        return res