import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

from asciiUi import PublicWordGen


def OnlineGame():
    secret_word = requests.get('https://api.dicionario-aberto.net/random').json()['word'].lower()
    public_word = PublicWordGen(secret_word)
    tip = genTip(secret_word)

    return (secret_word, public_word, tip)


load_dotenv(override=True)
api_key = os.getenv('API_KEY')

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def genTip(secret_word):
    response = model.generate_content(
    f'''Descrevendo palavras "use uma frase curta para descrever de alguma forma a palavra dada sem citar o seu radical na dica":
    Banana;
    banana: é uma fruta amarela

    comer;
    comer: é algo que se faz para se alimentar

    andar;
    andar: é algo que se faz para se locomover

    Arteria;
    Arteria: algo que carrega sangue oxigenado pelo corpo

    {secret_word};
    ''')

    return response.text[response.text.find(':')+2:] #extrating the tip from response

