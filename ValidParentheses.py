class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {"(":")","{":"}","[":"]"}

        for cha in s:
            if (cha in dic.keys()):
                stack.append(cha)
            elif (cha in dic.values()):
                if (len(stack) == 0):
                    return False
                else:
                    check = stack.pop()
                    if (dic[check] == cha):
                        continue
                    else:
                        return False
            else:
                print("You did not enter a bracket")
        return (len(stack) == 0)


            