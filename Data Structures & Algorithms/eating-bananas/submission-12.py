import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBananas = max(piles)
        left = 1
        right = maxBananas
        ans = right

        while left <= right:
            mid = (left + right)//2
            hs1 = [math.ceil(p / mid) for p in piles]
            hSum1 = sum(hs1)
            if hSum1 <= h:
                ans = mid
                right = mid - 1
            if  hSum1 > h:
                left = mid + 1
        
        return ans
            

        