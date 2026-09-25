class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # frequency mapping for BOTH s and t
        # if frequency of letters are the same, return true 

        if (len(s) != len(t)):
            return False

        from collections import Counter
        freq_s = Counter(list(s))
        freq_t = Counter(list(t))

        return freq_t == freq_s
            
           


        
