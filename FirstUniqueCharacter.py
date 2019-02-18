def first_unique_character(str):   

    for i in str:
        if (str.count(i) == 1):
            return i
    return -1
    
x =  'leetcode'
print(first_unique_character(x))