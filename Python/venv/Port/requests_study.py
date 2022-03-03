import requests
from pprint import pprint

r = requests.get('https://api.github.com/events')

pprint(r.text)
