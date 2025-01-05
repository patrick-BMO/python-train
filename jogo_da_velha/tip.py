import google.generativeai as genai

import os
from dotenv import load_dotenv

load_dotenv(override=True)


api_key = os.getenv('API_KEY')

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def genTip(secret_word):
    response = model.generate_content(
    f'''Descrevendo palavras:
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





