#Create two files in the same directory: string_utils.py and day10_modules.py.
# In string_utils.py, write helper functions slugify(text) and count_vowels(text).
# Inside day10_modules.py, import these functions using 
#from string_utils import slugify, count_vowels and execute them on sample input strings.
from string_utils import slugify, count_vowels

sample = '   HeLlO   WorLD  '
test = slugify(sample)
print(test)

sample1 = 'HI my name is ISAAC, and I am a COMPUTER SCIENCE STUDENT.'
result = count_vowels(sample1)
print(result)
