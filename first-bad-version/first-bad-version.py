# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = n
        low = 1
    
        while(high > low):
            mid = round(high + low )//2
            if(isBadVersion(mid)):
                high = mid
            else:
                low = mid + 1
                
        return low