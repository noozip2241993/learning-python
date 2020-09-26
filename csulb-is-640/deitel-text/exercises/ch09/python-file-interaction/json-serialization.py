accounts_dict = {'accounts': [
    {'account': 100, 'name': 'Jones', 'balance': 24.98},
    {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

# Serializing an object to JSON
import json
with open('accounts.json', 'w') as accounts:
    json.dump(accounts_dict, accounts)

#Deserializing the JSON text
with open('accounts.json', 'r') as accounts:
    accounts_json = json.load(accounts)

# Interacting with deserialized JSON object
print(accounts_json)
print(accounts_json['accounts'])
print(accounts_json['accounts'][0])
print(accounts_json['accounts'][1])

with open('accounts.json', 'r') as accounts:
    print(json.dumps(json.load(accounts), indent=4))