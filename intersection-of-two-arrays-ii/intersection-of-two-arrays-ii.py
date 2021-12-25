class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dicc = dict()
        for i in nums1: dicc[i] = dicc.get(i,0) + 1
        for i in nums2:
            if dicc.get(i,0):
                res.append(i)
                dicc[i] = dicc.get(i) - 1
                
        return res