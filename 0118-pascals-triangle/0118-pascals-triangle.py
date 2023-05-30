class Solution:
    def generate(self, N: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(1,N):
            pre = 1
            currlist = [1]
            for i in range(1,_+1):
                curr = (pre * (_ - i + 1))/i
                currlist.append(int(curr))
                pre = curr
            ans.append(currlist)
        return ans
            