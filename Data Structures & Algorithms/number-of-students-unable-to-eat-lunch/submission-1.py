class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sand0 = students.count(0)
        sand1 = students.count(1)
        for sand in sandwiches:
            if sand == 0 and sand0 > 0:
                sand0 -= 1
            elif sand == 1 and sand1 > 0:
                sand1 -= 1
            else:
                break
        return sand1 + sand0

        