from offline_game import OfflineGame
from online_game import OnlineGame
from asciiUi import cls, hangman, Win, Lose


def remove_acentos(word):
    word = word.replace('á', 'a')
    word = word.replace('à', 'a')
    word = word.replace('ã', 'a')
    word = word.replace('â', 'a')

    word = word.replace('é', 'e')
    word = word.replace('è', 'e')
    word = word.replace('ê', 'e')

    word = word.replace('í', 'i')
    word = word.replace('ì', 'i')
    word = word.replace('î', 'i')

    word = word.replace('ó', 'o')
    word = word.replace('ò', 'o')
    word = word.replace('õ', 'o')
    word = word.replace('ô', 'o')

    word = word.replace('ú', 'u')
    word = word.replace('ù', 'u')
    word = word.replace('û', 'u')
    return word


def compareWords(word, word2):
    return word == remove_acentos(word2)


# Exemplo de uso:
word = "Olá, você! Tudo bem?"
new_word = remove_acentos(word)
print(new_word)  # Saída: Ola, voce! Tudo bem?

def findIndex(char, text):
    index = 0
    list_index = []
    while index != -1:
        index = text.find(char, index+1)
        list_index.append(index)
    list_index.pop()

    return list_index

if __name__ == '__main__':
    while True:
        print('Deseja jogar online ou offline?')
        print('1 - Online')
        print('2 - Offline')
        mode = input('==> ')
        if mode == '1':
            secret_word, public_word, tip = OnlineGame()
            break

        elif mode == '2':
            secret_word, public_word, tip = OfflineGame()
            break

        else:
            cls()

    attempt = 0
    guess_list = []
    while True:
        cls()
        print(hangman[attempt], end='')
        print(f'   DICA: {tip} {len(secret_word)} Letras.')
        print(f'              Tentativas: {guess_list}', end='\n\n')
        print(f'                == {public_word} ==', end='\n\n')
        guess = input('Digite uma letra ou uma palavra: ')
        guess_list.append(guess)

        if len(guess) > 1:
            print(guess)

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
        if compareWords(public_word, secret_word): Win()