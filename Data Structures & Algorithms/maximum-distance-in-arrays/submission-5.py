class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        c_min = arrays[0][0]
        c_max = arrays[0][-1]

        for i in range(1, len(arrays)):
            res = max(res, c_max - arrays[i][0], arrays[i][-1] - c_min)
            c_min = min(c_min, arrays[i][0])
            c_max = max(c_max, arrays[i][-1])
        return res