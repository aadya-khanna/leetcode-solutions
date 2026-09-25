class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        from collections import Counter

        noteFreq = Counter(ransomNote)
        magazineFreq = Counter(magazine)

        return not noteFreq - magazineFreq


        
