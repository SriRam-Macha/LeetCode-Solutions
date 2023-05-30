class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        zero,one,two = 0,0,0
        
        for i in arr:
            if i == 0:
                zero +=1
            if i == 1:
                one +=1
            if i == 2:
                two +=1
                
        
        for i in range(n):
            if i < zero:
                arr[i] = 0
            elif i < zero+one:
                arr[i] = 1
            else:
                arr[i] = 2