class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        p,q = 0,len(s)
        for i,v in c.items():
            if v % 2 == 0:
                q = min(q,v)
            else:
                p = max(p,v)
        return p-q
        
