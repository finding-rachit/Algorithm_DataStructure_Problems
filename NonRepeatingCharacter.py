# Returns the first non-repeating charcter in a strong or -1 if None
def non_repeating_character(str):   
    dic = {}
    # Adding 'char' and its 'count' to the dictionary
    for i in str:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    # running through the string to match the value to 1
    for i in str:
        if dic[i] == 1:
            return i

    return -1
    
x =  'leetcode'
print(non_repeating_character(x))