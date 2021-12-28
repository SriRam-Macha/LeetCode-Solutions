class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        if numRows == 1:
            return(arr)
        else:
            for i in range(2,numRows+1):
                if i == 2:
                    arr.append([1,1])
                else:
                    
                    drr = [0]*i
                    drr[-1] = drr[0] = 1
                    for j in range(1,i-1):
                    
                        drr[j] = arr[-1][j-1] + arr[-1][j] 
                    arr.append(drr)



        return(arr)
                    
                