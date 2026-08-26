class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = [-1] * len(nums)
        stack = []

        i = 0
        j = 0

        while j < 2:
            while stack and nums[i] > nums[stack[-1]]:
                popped_idx = stack.pop()
                answer[popped_idx] = nums[i]
            
            if j == 0:
                stack.append(i)
            i+=1

            if i == len(nums):
                i = 0
                j+=1
        
        return answer
            
            
        
