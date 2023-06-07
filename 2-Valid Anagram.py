class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def Convert(string):
            list1 = []
            list1[:0] = string
            return list1

        list_s = Convert(s)
        list_s.sort()
        list_t = Convert(t)
        list_t.sort()
        if(len(list_s) != len(list_t)):
            return False
        
        for i in range(len(list_s)):
            if(list_s[i] != list_t[i]):
                return False
                break

        return True