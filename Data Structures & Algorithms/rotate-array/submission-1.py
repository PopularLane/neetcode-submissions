class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        while k:
            tmp = nums[n - 1]
            for s in range(n - 1, 0, -1):
                nums[s] = nums[s - 1]
            nums[0] = tmp
            k -= 1