class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""
        value = 0

        for c in range(len(num) - 2):
            if num[c] == num[c + 1] == num[c + 2]:
                tmp = num[c : c + 3]
                if value <= int(tmp):
                    value = int(tmp)
                    result = tmp

        return result