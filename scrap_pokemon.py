import requests
import json

req = requests.get('https://pokeapi.co/api/v2/pokemon/charmander')

json_response = json.loads(req.content)
print("Pokemon Name: " + json_response['name'])

abilities = json_response['abilities']

for i in abilities:
    ability_name = i['ability']['name']
    if ability_name == 'blaze':
        is_hidden = i['is_hidden']
        print('Ability ' + ability_name +" Existe - is_hidden: " + str(is_hidden))
    if ability_name == 'solar-power':
        is_hidden = i['is_hidden']
        print('Ability ' + ability_name + " Existe - is_hidden: " + str(is_hidden))


