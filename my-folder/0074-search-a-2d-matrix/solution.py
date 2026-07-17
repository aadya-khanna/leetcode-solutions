class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target: # checked all numbers upto that point
                    return False
        
        return False
                
                

        
