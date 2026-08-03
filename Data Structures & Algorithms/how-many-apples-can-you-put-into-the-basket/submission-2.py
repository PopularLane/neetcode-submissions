class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        units = 0
        apples = units
        

        for weight in arr:
            units += weight
            if units > 5000:
                break

            apples += 1
        return apples
