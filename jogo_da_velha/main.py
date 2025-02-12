from offline_game import OfflineGame
from online_game import OnlineGame
from asciiUi import cls, hangman, Win, Lose


def remove_acentos(word):
    """Função criada por IA mas conferida manualmente. kk"""
    
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


def compareWords(word: str, word2: str):
    return remove_acentos(word.lower()) == remove_acentos(word2.lower())


def findIndex(char, text):
    index = text.find(char)
    list_index = [index]

    while index != -1:
        index = text.find(char, index+1)
        list_index.append(index)
    list_index.pop()

    return list_index

if __name__ == '__main__':
    cls()
    while True:
        print('Deseja jogar online ou offline?')
        print('1 - Online')
        print('2 - Offline')
        mode = input('==> ')
        if mode == '1':
            try:
                secret_word, public_word, tip = OnlineGame()
                break

            except:
                input('Conexão não disponível, aperte "ENTER" para continuar')
                mode = '2'

        if mode == '2':
            secret_word, public_word, tip = OfflineGame()
            break

        else:
            cls()

    attempt = 0
    guess_list = []
    while True:
        cls()
        if mode == '2': print('Offline')
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
            print(found)
            if found == []:
                attempt += 1
            
            else:
                for i in found:
                    public_word = public_word[:i] + secret_word[i:i+1] + public_word[i+1:]
        
        if attempt == 6: Lose(secret=secret_word)
        if compareWords(public_word, secret_word): Win()