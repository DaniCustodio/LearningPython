import requests
from random import choice

print('------------------DAD JOKES 3000------------------')
topic = input('Let me tell you a joke! Give me a topic: ')
url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers = {"Accept": "application/json"},
    params = {"term": topic}
)
data = response.json()
quant_jokes = data["total_jokes"]

if quant_jokes == 0:
    print(f"Sorry, I don't have any jokes about {topic}! Please try again")
elif quant_jokes == 1:
    print(f'I\'ve got one jokes about {topic}. Here it is: ')
    print(choice(data["results"])["joke"])
else:
    print(f'I\'ve got {quant_jokes} jokes about {topic}. Here\'s one: ')
    print(choice(data["results"])["joke"])
