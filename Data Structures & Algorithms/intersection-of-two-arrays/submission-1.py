class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for s in nums1:
            for x in nums2:
                if s == x:
                    res.add(s)
                    break
        return list(res)