# Returns if list A and B have the same elements just in different order
def is_rotation(list1,list2):
    dic1 = {key:value for value,key in enumerate(list1)}
    
    for i in list2:
        if i not in dic1:
            return False
    return True

A = [1,2,3,4,5,6,7]
B = [4,5,6,7,1,2,3]
print(is_rotation(A,B))