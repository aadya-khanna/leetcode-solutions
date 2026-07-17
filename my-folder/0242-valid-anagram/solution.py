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

        for i, key in enumerate(freq_s):
            if freq_s.get(key) != freq_t.get(key):
                return False
        
        return True
            
           


        
