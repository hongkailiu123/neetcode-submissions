from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        heap = [-count for count in counts.values()]
        heapq.heapify(heap)

        cooldown = deque()
        time = 0

        while heap or cooldown:
            time += 1
            if heap: 
                count = heapq.heappop(heap)
                count += 1

                if count != 0:
                    cooldown.append((count, time + n))
            
            if cooldown and cooldown[0][1] == time:
                count, _ = cooldown.popleft()
                heapq.heappush(heap, count)
        
        return time
        