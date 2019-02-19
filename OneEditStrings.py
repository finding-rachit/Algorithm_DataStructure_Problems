# Returns true if string one can become string two with just one edit (change,add,delete)
def one_edit_string(str1,str2):
    change = 0
    dic1 = {key:index for index,key in enumerate(str1)}
    dic2 = {key:index for index,key in enumerate(str2)}

    # condition to check if both str are same!
    if (str1 == str2):
        return True
    # condition if the length is same and only need to edit one char
    elif (len(str1) == len(str2)):
        print("Condition 1")
        for i in range(len(str2)):
            if ((str2[i] in dic1) and (dic1[str2[i]] == i)) :
                continue
            else:
                change += 1
                if change > 1:
                    return False
    # condition if there as to be a char deleted in str1
    elif (len(str1) == len(str2)+1):
        print("Condition 2")
        for i in range(len(str1)):
            if ((str1[i] in dic2) and (dic2[str1[i]] == i or dic2[str1[i]] == i-1)) :
                continue
            else:
                change += 1
                if change > 1:
                    return False
    # condition if there has to be a char added to str1
    elif (len(str1) == len(str2)-1):
        print("Condition 3")
        for i in range(len(str2)):
            if ((str2[i] in dic1) and (dic1[str2[i]] == i or dic1[str2[i]] == i-1)) :
                continue
            else:
                change += 1
                if change > 1:
                    return False
    return (change == 1)

A = 'xyz'
B = 'xyaz'
print(one_edit_string(A,B))
