class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
    
        
        row = -1
        for i in matrix:
            if i[0] <= target:
                row+=1
        
        if row == -1 : return False
        
        for j in matrix[row]:
            if j == target:
                return True
            
        return False
                