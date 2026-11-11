#Write a function is_leap_year(year: int) -> bool 
#handling century rules (divisible by 4, unless divisible by 100, except when divisible by 400).

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = 2001
if is_leap_year(year):
    print('yes')
else:
    print('no')    