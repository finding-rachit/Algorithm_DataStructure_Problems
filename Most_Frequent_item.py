# Returns the most frequent item of an array
def most_frequent_item(arr):
    max_count = 0
    max_item = None
    count = {}
    # O(n) -> Running through array once, and adding it to dictionary
    for i in arr:
        # if char not in dic, add it
        if i not in count:
            count[i] = 1
        # if char in dic, increase it count
        else:
            count[i] += 1
        # Keeping track of the item and its max_count
        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    return max_item

lst = [1,3,1,3,2,1]
print(most_frequent_item(lst))