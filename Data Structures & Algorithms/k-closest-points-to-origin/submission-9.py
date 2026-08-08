import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculateED(point):
            x1,y1 = point
            return x1**2 + y1**2
        points.sort(key=calculateED)
        return points[:k]

        