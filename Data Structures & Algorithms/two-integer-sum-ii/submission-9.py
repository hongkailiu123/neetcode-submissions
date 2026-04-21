class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        def binarySearch(target: int) -> int:
            left_b = 0
            right_b = length-1
            while left_b <= right_b:
                mid_i = (right_b + left_b)//2
                if numbers[mid_i] == target:
                    return mid_i
                if numbers[mid_i] > target:
                    right_b = mid_i -1 
                else:
                    left_b = mid_i + 1 
                print(left_b)
                print(right_b)
            
            return -1
        
        for i in range(length):
            a = numbers[i]
            c = binarySearch(target - a)
            if c  != -1:
                return[i + 1, c + 1]
        return [-1, -1]
                

        