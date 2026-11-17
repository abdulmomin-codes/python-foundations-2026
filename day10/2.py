#Given two lists headers = ["id", "name", "role"] and values = [101, "David", "Engineer"],
# merge them into a dictionary using zip(). Then, take a list of 
#strings passwords = ["secret123", "Admin!", "qwerty"] and use any() and all() to verify if 
#any password contains an exclamation mark and if all passwords are longer than 4 characters.
headers = ["id", "name", "role"]
values = [101, "David", "Engineer"]

dic = {}
for h, v in zip(headers, values):
    dic[h] = v
print(dic)

dict1 = {h: v for h, v in zip(headers, values)}
print(dict1)

# ///next answer///
passwords = ["secret123", "Admin!", "qwerty"]

has_exclamation = any("!" in password for password in passwords)
all_long_enough = all(len(password) > 4 for password in passwords)

print(has_exclamation)
print(all_long_enough)

