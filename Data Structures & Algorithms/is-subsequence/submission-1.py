class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        i = j
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)