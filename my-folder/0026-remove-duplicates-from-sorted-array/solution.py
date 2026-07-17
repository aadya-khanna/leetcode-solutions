class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = float('-inf')

        k = 0

        for n in nums:
            if n != prev:
                nums[k] = n
                prev = n
                k+=1
        return k            






        
        
