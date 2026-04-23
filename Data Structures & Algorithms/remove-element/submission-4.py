class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for c in range(len(nums)):
            if nums[c] != val:
                nums[k] = nums[c]
                k += 1
        return k