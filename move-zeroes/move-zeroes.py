class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i-k] == 0:
                nums.pop(i-k)
                k+=1
        for i in range(k):
            nums.append(0)