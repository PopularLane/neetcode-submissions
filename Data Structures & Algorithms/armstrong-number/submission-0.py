class Solution:
    def isArmstrong(self, n: int) -> bool:
        def getSumOfKthPowerOfDigits(num, k):
            result = 0

            while num != 0:
                result += (num % 10) ** k
                num //= 10

            return result

        length = int(math.log10(n)) + 1

        return getSumOfKthPowerOfDigits(n, length) == n