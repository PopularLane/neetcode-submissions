class Solution:
    def isPathCrossing(self, path: str) -> bool:

        seen = set()

        x, y = 0, 0
        seen.add((0,0))
        for direction in path:
            if direction == 'N':
                y += 1
            if direction == 'S':
                y -=1
            if direction == 'E':
                x -= 1
            if direction == 'W':
                x += 1

            cords = (x, y)

            if cords in seen:
                return True
            else:
                seen.add(cords)

        return False

        