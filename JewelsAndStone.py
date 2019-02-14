class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter = 0
        
        for jewel in J:
            for stone in S:
                if (jewel == stone):
                    counter += 1
        return counter