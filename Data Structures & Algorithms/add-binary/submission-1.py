class Solution:
    def addBinary(self, a: str, b: str) -> str:
        k=int(a,2)
        l=int(b,2)
        p=k+l
        r=bin(p)[2:]
        return r