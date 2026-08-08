import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first_largest = heapq.heappop(heap)
            second_largest = heapq.heappop(heap)
            # update the weight of heaviest stone
            first_largest = first_largest - second_largest
            if first_largest != 0:
                heapq.heappush(heap, first_largest)
            
        if len(heap) !=0:
            return abs(heap[0])
        return 0
        




        

        