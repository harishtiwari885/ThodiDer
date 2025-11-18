
def find_common_elements(list1 , list2):
    set2 = set(list2)
    result = []
    for a in list1:
        if a in set2 and a not in result:
            result.append(a)
    return result

list1 = [1 , 2 , 3 , 4]
list2 = [3 , 4 , 5 , 6]
print(find_common_elements(list1 , list2))
"""
def find_common_elements(list1, list2):
    set2 = set(list2)     
    result = []           

    for x in list1:       # Check each element of list1
        if x in set2 and x not in result:
            result.append(x)

    return result

# Example
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(find_common_elements(list1, list2))   # Output → [3, 4]

"""