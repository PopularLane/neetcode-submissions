class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        maxi=-1
        for i in nums:
            if nums.count(i)==1:
                maxi=max(maxi,i)
        return maxi