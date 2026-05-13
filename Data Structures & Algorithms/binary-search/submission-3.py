class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, r = 0, len(nums) - 1

        while s <= r:
            x = s + ((r - s) // 2)

            if nums[x] > target:
                r = x - 1
            elif nums[x] < target:
                s = x + 1
            else:
                return x
        return -1