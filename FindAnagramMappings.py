class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        new_list = []
        
        for x in A:
            new_list.append(B.index(x))
        return new_list