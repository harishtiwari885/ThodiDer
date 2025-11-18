
def find_common_elements(list1, list2):
    # Convert both lists to sets so duplicates are removed, then find intersection
    return list(set(list1) & set(list2))

# Example
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = find_common_elements(list1, list2)
print(result)   # Output → [3, 4] (order may vary because of set)
