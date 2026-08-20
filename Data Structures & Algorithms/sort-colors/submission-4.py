class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        buckets = [0] * 3
        for num in nums:
            buckets[num]+=1
        
        index = 0
        for i in range(len(buckets)):
            while buckets[i]:
                buckets[i]-=1
                nums[index] = i
                index+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        