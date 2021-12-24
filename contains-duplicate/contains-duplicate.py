class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dicc = dict()
        for i in nums:
            if dicc.get(i,0) == 1:
                return True
            else:
                dicc[i] =1
        
        return False