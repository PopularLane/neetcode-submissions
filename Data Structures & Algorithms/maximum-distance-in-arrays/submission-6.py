class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        minimum = arrays[0][0]
        maximum = arrays[0][-1]

        for i in range(1, len(arrays)):
            res = max(res, maximum - arrays[i][0], arrays[i][-1] - minimum)
            minimum = min(minimum, arrays[i][0])
            maximum = max(maximum, arrays[i][-1])
        return res