class Solution:
    def firstUniqChar(self, s: str) -> int:
        for q in range(len(s)):
            flag = True
            for j in range(len(s)):
                if q == j:
                    continue
                if s[q] == s[j]:
                    flag = False
                    break
            if flag:
                return q
        return -1