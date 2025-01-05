import requests

secret_word = requests.get('https://api.dicionario-aberto.net/random').json()['word']
public_word = []

def PublicWordGen(secret_word):
        if '-' in secret_word:
            public_word = ['_' if i != '-' else '-' for i in secret_word]

        else:
            public_word = ['_' if i != ' ' else ' ' for i in secret_word]
        
        return ''.join(public_word)

if __name__ == '__main__':
    public_word = PublicWordGen(secret_word)
    print(secret_word)