class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        counter = 1 
        original_A = A

        while (len(A) < len(B)):
            A += original_A
            counter += 1
        if(B in A):
            return counter
        A += original_A
        counter += 1
        if(B in A):
            return counter
        return (-1)
        
        
        
