class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        circle_bracket_left = 0
        curly_bracket_left = 0
        square_bracket_left = 0
        
        circle_bracket_right = 0
        curly_bracket_right = 0
        square_bracket_right = 0
        
        for x in s:
            if (x == "("):
                circle_bracket_left += 1
            elif (x == ")"):
                circle_bracket_right += 1
            elif (x == "{"):
                curly_bracket_left += 1
            elif (x == "}"):
                curly_bracket_right += 1
            elif (x == "["):
                square_bracket_left += 1
            elif (x == "]"):
                square_bracket_right += 1
        
        if ((circle_bracket_left == circle_bracket_right) and (curly_bracket_left == curly_bracket_right) and       (square_bracket_left == square_bracket_right)):
            return True
        else:
            return False