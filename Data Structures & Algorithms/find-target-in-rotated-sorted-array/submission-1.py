class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for s in range(len(nums)):
            if nums[s] == target:
                return s
        return -1