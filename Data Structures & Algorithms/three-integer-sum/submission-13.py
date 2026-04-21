class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        sorted_nums = sorted(nums)
        result = []


        
        for i in range (length):
            curr_val = sorted_nums[i]
            target = 0 - curr_val
            left = i
            right = length - 1
            
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            while left < right:
                two_sum = sorted_nums[left] + sorted_nums[right]
                if left == i or two_sum < target:
                    left += 1
                elif right == i or two_sum > target:
                    right -= 1
                else:
                    result.append([curr_val, sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1

                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1

            
        return result
                
