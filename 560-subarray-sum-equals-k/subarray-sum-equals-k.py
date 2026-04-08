class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        curr_sum = 0
        prefix = {0: 1}  # base case
        
        for num in nums:
            curr_sum += num
            
            if (curr_sum - k) in prefix:
                count += prefix[curr_sum - k]
            
            if curr_sum in prefix:
                prefix[curr_sum] += 1
            else:
                prefix[curr_sum] = 1
        
        return count