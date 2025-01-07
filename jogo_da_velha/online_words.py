import requests

word = requests.get('https://api.dicionario-aberto.net/random').json()['word']
