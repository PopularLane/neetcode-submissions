class Solution:
    def majorityElement(self, nums):
        count = 0
        result = count

        for num in nums:
            if count == 0:
                result = num
            count += (1 if num == result else -1)
        return result