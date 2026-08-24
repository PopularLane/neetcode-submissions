class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        maximum = -1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                total = nums[i] + nums[j]

                if total < k:
                    maximum = max(maximum, total)

        return maximum