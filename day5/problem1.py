#Write a function deduplicate_preserve_order(lst: list) -> list 
#removing duplicate items without altering initial order.


def deduplicate_preserve_order(lst: list) -> list:
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

items = ['pen', 'bag', 'cat', 'dog', 'pen', 'bag', 'cat', 'dog', 'cat', 'dog', 'pen', 'bag']  

test = deduplicate_preserve_order(items)

print(test)  