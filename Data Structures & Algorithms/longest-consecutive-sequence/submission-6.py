class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        num_set = set(nums)
        longest = 1
        curr = 0

        for num in nums:
            val = num
            if val-1 not in num_set:
                curr += 1

                while val + 1 in num_set:
                    curr += 1
                    val += 1
                    longest = max(longest, curr)
                
            curr = 0
        
        return longest
