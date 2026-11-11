#Write a function using collections.defaultdict(list) to group a raw list of words 
#by their starting character (e.g., 'a': ['apple', 'avocado']).
from collections import defaultdict
def group_chars(lst):
    new_char = defaultdict(list)
    for word in lst:
        first = word[0]
        new_char[first].append(word)
    return new_char
    
    
raw_words = ['apple', 'banana', 'avocado', 'blueberry', 'cherry', 'apricot']    
test = group_chars(raw_words)
print(dict(test))