class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sums = None
        left = 0
        right = len(numbers) - 1
        while(sums != target):
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1,right+1]
                
            