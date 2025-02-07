from core import offline_words as words
from core import hangman, PublicWordGen
from core import cls
from random import choice

def findIndex(char, text):
    index = 0
    list_index = []
    while index != -1:
        index = text.find(char, index+1)
        list_index.append(index)
    list_index.pop()

    return list_index


def Lose(secret):
    cls()
    print('---------------------------')
    print('  Oce Perdeu meu chapa :(')
    print('---------------------------')
    print(secret)
    exit()


def Win():
    cls()
    print('---------------------------')
    print('  Oce Ganhou meu chapa :D')
    print('---------------------------')
    exit()

def offline_game():
    secret_word, tip = choice(words)
    secret_word = secret_word.lower()
    gues_list = []
    public_word = PublicWordGen(secret_word)


    attempt = 0
    while True:
        cls()
        print(hangman[attempt], end='')
        print(f'   DICA: {tip} {len(secret_word)} Letras.')
        print(f'              Tentativas: {gues_list}', end='\n\n')
        print(f'                == {public_word} ==', end='\n\n')
        guess = input('Digite uma letra ou uma palavra: ')
        gues_list.append(guess)


        if len(guess) > 1:
            print(guess)
            print(secret_word)
            if guess == secret_word:
                Win()
            
            else:
                attempt += 1
        
            

        elif len(guess) == 0:
            ...
        
        else:
            found = findIndex(guess, secret_word)
            if found == []:
                attempt += 1
            
            else:
                for i in found:
                    public_word = public_word[:i] + secret_word[i:i+1] + public_word[i+1:]

        
        if attempt == 6: Lose(secret=secret_word)
        if public_word == secret_word: Win()
                

    