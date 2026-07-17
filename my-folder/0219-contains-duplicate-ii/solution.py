class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # is there a duplicate?
        # what is the distance between them (is it <=  k)

        # keep track of where the duplicate is happening for ALL the dups present

        dic = {}

        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        
        return False


                

        


            
            
        
