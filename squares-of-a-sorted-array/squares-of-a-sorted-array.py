class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length
        left = 0
        right = length -1
        pointer = length -1
        while(pointer >= 0):
            if abs(nums[left]) > abs(nums[right]):
                print(pointer,left,right)
                res[pointer] = nums[left]**2
                left+=1
            else:
                print(pointer,left,right)
                res[pointer] = nums[right]**2
                right -=1
                
            pointer-=1
        
        return res