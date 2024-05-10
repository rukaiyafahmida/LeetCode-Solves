class Solution:
    def isPathCrossing(self, path: str) -> bool:
        point = (0, 0)
        visited = [point]
        for dir in path:
            if dir == 'N':
                point = (point[0], point[1]+1)
            elif dir == 'S':
                point = (point[0], point[1]-1)
            elif dir == 'E':
                point = (point[0]+1, point[1])
            else:
                point = (point[0]-1, point[1])
            if point in visited:
                return True
            visited.append(point)
        return False
