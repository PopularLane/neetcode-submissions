class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s = set(source)
        for c in target:
            if c not in s:
                return -1
        res = 0
        # i points to target
        i = 0
        while i < len(target):
            # j points to source
            j = 0
            while j < len(source) and i < len(target):
                if target[i] == source[j]:
                    i += 1
                j += 1
            res += 1
        return res