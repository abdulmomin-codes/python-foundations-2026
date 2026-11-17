#Write a script day14_big_o.py containing 4 separate functions that solve target search problems
# using different algorithmic complexity profiles
#:get_first_element(lst) -> O(1) Time
#find_element_linear(lst, target) -> O(N) Time
#generate_all_pairs(lst) -> O(N^2) Time
#binary_search_demo(sorted_lst, target) -> O(log N) Time
def get_first_element(lst: list):
    if lst:
        first = lst[0]
    else:
        first = None
    return first    
"""time is O(1) because we only look for the first element and add it, space also would  
be O(1) cause it doesnt take much memory except storing it in first variable """    

def find_element_linear(lst, target):
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1
"""we are searching for a target element by element and so max would be O(n) cause at most
it will search complete list, and space will probably be O(1) cause its simply once again
storing a simple index"""      
def generate_all_pairs(lst):
    lst_final = []
    for i in lst:
        for j in lst:
            lst_final.append((i, j))
    return lst_final
""" O(n**2) cause simply we are iterating using two loops so nested loops are n**2, space
will also be n**2 cause like suppose we have 3 elements and so all the pairs equal 9"""
def binary_search_demo(sorted_lst, target):
    left = 0
    right = len(sorted_lst) - 1
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_lst[mid] == target:
            return mid
        elif sorted_lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
""" binary search works by halving the array each step so time is O(logn) and space is O(1)
because it stores 1 element in the end which is the target."""

if __name__ == '__main__':
    lst1 = []    
    result1 = get_first_element(lst1)
    print(result1)    

    lst2 = [1, 2, 3, 4, 5, 6]
    result2 = find_element_linear(lst2, 0)         
    print(result2) 

    lst3 = [1, 2, 3]
    result3 = generate_all_pairs(lst3) 
    print(result3)

    nums = [1, 2, 3, 4, 5, 6, 7]
    result4 = binary_search_demo(nums, 0)
    print(result4)