class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, r = 0, len(nums) - 1

        while s <= r:
            m = s + ((r - s) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                s = m + 1
            else:
                return m
        return -1