class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res, n = 0, len(s)

        for i in range(n):
            seen = set()
            cnt = curLen = 0
            for j in range(i, n):
                seen.add(s[j])
                if len(seen) > 2:
                    break
                curLen += 1
            res = max(res, curLen)

        return res