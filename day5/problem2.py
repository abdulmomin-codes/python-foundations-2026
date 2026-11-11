#Write a function comparing two lists to return three distinct sets:
#common elements, elements unique to List 1, and elements unique to List 2.

def compare_collections(list1: list, list2: list) -> tuple[set, set, set]:
    set1, set2 = set(list1), set(list2)
    
    common = set1 & set2
    unique_to_first = set1 - set2
    unique_to_second = set2 - set1
    
    return common, unique_to_first, unique_to_second

courses1 = ['math', 'science', 'physics', 'biology']
courses2 = ['compsci', 'physics', 'art', 'science']

common, unique1, unique2 = compare_collections(courses1, courses2)
print(f"Common: {common}")
print(f"Unique to List 1: {unique1}")
print(f"Unique to List 2: {unique2}")