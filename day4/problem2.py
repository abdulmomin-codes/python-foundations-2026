#Write a function using enumerate() that accepts a list of item names and 
#prints indexed bullet points, skipping empty strings using continue.

def printer(names):
    for i, value in enumerate(names, start=1):
        if value == '':
            continue
        else:
            print(f'{i}. {value}')

items = ['cap', 'pen', 'pencil', '', 'scale']
hello = printer(items)