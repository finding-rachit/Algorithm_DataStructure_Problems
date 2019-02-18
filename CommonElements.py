# Return common Elements of List A & B
def common_elements(arr1,arr2):
    dic1 = {}
    common = []
    # Dic with array 1
    for i in arr1:
        dic1[i] = 1
    # Going through array 2, and checking if char in dic1
    for j in arr2:
        if (j in dic1):
            common.append(j)

    return common

A = [1,3,4,6,7,9]
B = [1,2,4,5,9,10]
print(common_elements(A,B))
        