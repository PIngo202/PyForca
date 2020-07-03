from random import choice
import os
frases = [ # Palavras para escolher
        'Arvores',
        'Corpo Humano',
        'Flores',
        'Orgaos Humanos',
        'Sistema Digestório',
        'Sistema de informatica'
]
letras = {} # Iniciando dict de letras
letrasp = {} # iniciando Dict de letra das palavras
palavra = choice(frases) # Escolhendo palavra
for i in range(len(palavra)):# Colocando todas as letras no dict
    if palavra[i] == ' ':# Retira o espaço
        continue
    if palavra[i].lower() in letrasp: # verifica se tem a lentra no dict
        continue
    else:# Se nao tiver coloca a letra no dict
        letrasp[i] = palavra[i].lower()
os.system('cls') # Limpa o terminal
erros = 0#Contabiliza os erros
while True:# Inicia o Loop Infinito
    if erros >= 5:#Verifica se voce ja errou mt
        letra = str(input('Chute uma palavra ou vai perder: '))
        if letra.lower() == palavra.lower():#Verifica se a palavra é igual ao input
            print('Voce Ganhou!!!')
            break# Sai do loop
        else:# Caso não
            print('Voce Perdeu!!!')
            print('A palavra era ' + palavra)#Informa a palavra
            break# sai do loop
    else:
        letra = str(input('Digite uma letra: ')).strip()#input
    if len(letra) > 1 or len(letra) == 0 and erros <= 5:# verifica se digitou mais de uma ou nenhuma caso sim da um continue
        continue
    for i in range(len(palavra)):#verifica todas as letras da palavra e coloca no dict de letras (se a letra ja estiver e for a mesma letra vai dar 1 de erro)
        if letra.lower() == palavra[i].lower():
            if letra not in letras:
                letras[i] = letra
            else:
                erros += 1
    if letra not in palavra:#Verifica se errou e caso sim da mais 1 erros 
        erros += 1
    os.system('cls')# Limpa o terminal
    for l in range(len(palavra)):#Escreve as palavras acertadas até a gora e coloca um >> _ << nas que nao foi acertado
        if palavra[l] == ' ':#escreve o espaco em branco e volta para o inicio do for
            print(' ', end='')
            continue
        if letras.get(l):#Verifica se ta no index da letra e escreve ela se tiver
            print(letras.get(l), end='')
        else:#Caso não escreve um >> _ << no lugar
            print('_', end='')
    if letras == letrasp:#Verifica se todas as letras do letras(Que sao as que o player digitou) e as letrasp(Que sao as geradas pelo sistema) sao iguais
        print('')
        print('Voce Ganhou!!')
    print('')
