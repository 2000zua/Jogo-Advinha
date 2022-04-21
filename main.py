import random

#Variveis globais
NUM_DIGITS = 3
MAX_ADVINHA = 10

#Função principal
def main():
    print(f"""\033[33;1m
    Eu estou pensando em {NUM_DIGITS} - numero de digitos sem digitos repetido.
    Tenta advinhar qual é. Aqui temos algumas pistas
    Quando eu dizer:         Isso significa:
        Pico                 Um digito está correcto e na posição certa.
        Fermi                Um digite está correcto e está na posição errada.
        Bagels               Nenhum dos digitos está certo.
    Por exemplo, se o numero secreto for 248 e sua tentativa for 843, as pistas seriam Fermi Pico\033[m""")
    print('~~'*40)
    #Circulo principal do jogo
    while True:
        secretoNum = getSecretNum() # função para advinhar no numero
        print('\033[1;34mEu estou pensando em um numero')
        print(f'Você tem {MAX_ADVINHA} tentativas para acertar.\033[m')

        # numero de tentativas
        numGuesses = 1
        while numGuesses <= MAX_ADVINHA:

            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'\033[1;34mTentativa nº{numGuesses}: \033[m')
                guess = input('\033[1;31m>>> \033[m')

            clues = getClues(guess, secretoNum ) # pistar ,
            print(clues)
            numGuesses += 1
            # verificar se acertou
            if int(guess) == int(secretoNum):
                break # Parabéns , saindo do circulo

            if numGuesses < MAX_ADVINHA:
                print('Voce pode tentar mais :-)')
                print(f'A sua resposta foi {guess}')


        # perguntando ao jogador , se ele deseja jogar ou sair
        sair = input('Você deseja sair do jogo ? (yes or no)').lower()
        if sair.lower() == 'yes':
            break
        print('Muito obrigado por jogar')


def getSecretNum():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)

    #pegar p primeiro NUM_DIGITS numero da lista para o numero secreto
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretoNum):
    #regreçãr um string com as dicas PICO, FERMI, e BAGELS
    if guess == secretoNum:
        return f'\033[1;34mMuitos parabéns você acertou o numero segretro {secretoNum} \033[m'

    claues = []

    for i in range(len(guess)):
        if guess[i] == secretoNum[i]:
            #Acertou, Numero na posição certa
            claues.append('Pico - \033[1;32mUm digito está correcto e na posição certa\033[m')
        elif guess[i] in secretoNum:
            #Acertou, mais o numero está na posição errada
            claues.append('Fermi - \033[1;35mUm digite está correcto e está na posição errada.\033[m')

    if len(claues) == 0:
        return 'Bagels - \033[1;31mNenhum dos digitos está certo.\033[m'
    else:
        claues.sort()
        return ' '.join(claues)

if __name__=='__main__':
    main()


#@Angelo Abreu Zua