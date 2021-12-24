class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicc = dict()
        c = 0
        for i in nums:
            k = dicc.get(target - i,(0,0))
            if k[0] == 1:
                return [k[1] , c]
            else:
                dicc[i] = (1,c)
                c+=1
                
            
                
        