import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculateED(point):
            x1,y1 = point
            return (math.sqrt((x1)**2 + (y1)**2))
        
        points_with_distance = [[calculateED(point), point] for point in points]
        sorted_points = sorted(points_with_distance, key = lambda x :x [0])
        return [x[1] for x in sorted_points[0:k]]



        