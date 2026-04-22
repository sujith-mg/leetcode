class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        
        while n:
            n = n & (n - 1)  # remove last set bit
            count += 1
        
        return count