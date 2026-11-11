#Write a frequency counting function manually using standard dicts and 
#compare it with an implementation using collections.Counter.
from collections import Counter
def freq_counter(lst):
    seen = {}
    for item in lst:
        if item not in seen:
            seen[item] = 1
        else:
            seen[item] += 1    
    return seen

def counter_method(lst):
    return Counter(lst)



items = ['pen', 'pencil', 'pen', 'cat', 'dog', 'pencil', 'dog', 'cat', 'dog', 'cat']
test = freq_counter(items)
built_in_test = counter_method(items)
print(test)
print(built_in_test)