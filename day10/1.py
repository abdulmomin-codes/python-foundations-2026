#Given a list of user dictionaries users = [{"name": "Alice", "age": 25, "active": True},
 #{"name": "Bob", "age": 17, "active": True},
 # {"name": "Charlie", "age": 30, "active": False}]:
#  Use a List Comprehension to extract names of active users who are 18 or older.
#Use a Dictionary Comprehension to map names to ages for active users only ({"Alice": 25}).
users = [{"name": "Alice", "age": 25, "active": True},
 {"name": "Bob", "age": 17, "active": True},
  {"name": "Charlie", "age": 30, "active": False}]
lst = []
for person in users:
    if person['age'] >= 18 and person['active']:
        lst.append(person['name'])
print(lst)        
my_list = [n['name'] for n in users if n['age'] >= 18 and n['active']]
print(my_list)
#///Dictionary Comprehension///
dics = {}
for person in users:
    if person['active'] == True:
        dics [person['name']] = person['age']
print(dics)        
my_dics = {person['name']: person['age'] for person in users if person['active']}
print(my_dics)