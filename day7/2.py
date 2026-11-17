#Write a script that defines a user dictionary, saves it to users.json using json.dump(),
#reads it back using json.load(), modifies an attribute (e.g., sets active: False), 
#and saves the updated dictionary to users_updated.json.
import json
user_data = {
    "user_id": 1042,
    "username": "dev_explorer",
    "email": "explorer@example.com",
    "active": True,
    "roles": ["member", "contributor"],
    "login_count": 14
}

with open('users.json', 'w') as wf:
    json.dump(user_data, wf, indent=4)
    
with open('users.json', 'r') as rf:
    data = json.load(rf)   

data['active'] = False
with open('users_updated.json', 'w') as uf:
    json.dump(data, uf, indent=4)  
    