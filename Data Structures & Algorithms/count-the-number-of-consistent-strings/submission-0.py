class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0

        for s in words:
            flag = 1
            for c in s:
                if c not in allowed:
                    flag = 0
                    break
            result += flag

        return result