class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        s = len(nums)
        if nums[0] <= nums[-1]:
            for i in range(1, s):
                if nums[i] < nums[i - 1]:
                    return False
            return True
        else:
            for i in range(1, s):
                if nums[i] > nums[i - 1]:
                    return False
            return True