class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for s in range(len(numbers)):
            for x in range(s + 1, len(numbers)):
                if numbers[s] + numbers[x] == target:
                    return [s + 1, x + 1]
        return []