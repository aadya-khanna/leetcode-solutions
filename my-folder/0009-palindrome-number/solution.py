class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # use 2 pointer approach
        arr_x = list(str(x))

        print(arr_x)

        reverse = arr_x[::-1]
        print(reverse)

        for i in range(0, len(arr_x) // 2):
            if arr_x[i] != reverse[i]:
                return False
        
        return True
        
        return True



        

        

      


        
