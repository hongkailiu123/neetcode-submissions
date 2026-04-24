class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1): return self.findMedianSortedArrays(nums2, nums1)
        total = len(nums1) + len(nums2)
        left, right = 0, len(nums1)

        while left <= right:
            i = (left + right) // 2
            j = (total + 1) // 2 - i

            A_left = nums1[i-1] if i > 0 else float('-inf')
            A_right = nums1[i] if i < right else float('inf')
            B_left = nums2[j-1] if j > 0 else float('-inf')
            B_right = nums2[j] if j < len(nums2) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                if total%2 == 1:
                   return float(max(B_left, A_left))
                else:
                    return float(max(B_left, A_left) + min(A_right, B_right))/2
            
            elif A_left > B_right:
                right = i - 1
            else: #B_left > A_right
                left = i + 1
        
        return 0.0

