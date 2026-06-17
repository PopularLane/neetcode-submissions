class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        result = 0
        for num1 in a:
            for num2 in b:
                for num3 in c:
                    if (num1^num2^num3).bit_count() % 2 == 0:
                        result += 1
        return result