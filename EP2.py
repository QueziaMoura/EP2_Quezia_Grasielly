# Biblioteca

from random import shuffle

def cria_baralho():
    cartas = ['A♣','K♣','Q♣','J♣','10♣','9♣','8♣','7♣','6♣','5♣','4♣','3♣','2♣','A♠','K♠','Q♠','J♠','10♠','9♠','8♠','7♠','6♠','5♠','4♠','3♠','2♠','A♦','K♦','Q♦','J♦','10♦','9♦','8♦','7♦','6♦','5♦','4♦','3♦','2♦','A♥','K♥','Q♥','J♥','10♥','9♥','8♥','7♥','6♥','5♥','4♥','3♥','2♥']
    shuffle(cartas)
    return cartas

def extrai_valor(carta):
    if carta == '10♣' or carta == '10♥' or carta == '10♠' or carta == '10♦':
        return '10'
    else:
        return carta[0]

def extrai_naipe(carta):
    if carta == '10♣' or carta == '10♥' or carta == '10♠' or carta == '10♦':
        return carta[2]
    else:
        return carta[1]

def lista_movimentos_possiveis(baralho,i):
    resultado = []
    if 'A' in baralho[i]:
        numero = 'A'
    if '1' in baralho[i]:
        numero = '1'
    if '2' in baralho[i]:
        numero = '2'
    if '3' in baralho[i]:
        numero = '3'
    if '4' in baralho[i]:
        numero = '4'
    if '5' in baralho[i]:
        numero = '5'
    if '6' in baralho[i]:
        numero = '6'
    if '7' in baralho[i]:
        numero = '7'
    if '8' in baralho[i]:
        numero = '8'
    if '9' in baralho[i]:
        numero = '9'
    if '10' in baralho[i]:
        numero = '10'
    if 'J' in baralho[i]:
        numero = 'J'  
    if 'Q' in baralho[i]:
        numero = 'Q'
    if 'K' in baralho[i]:
        numero = 'K'

    if '♣' in baralho[i]: 
        naipe = '♣'
    if '♠' in baralho[i]:
        naipe =  '♠'
    if '♥' in baralho[i]:
        naipe = '♥'
    if '♦' in baralho[i]:
        naipe = '♦'
  
    if i == 0 :
        return []
    if numero in baralho[i-1] or naipe in baralho[i-1]:
        resultado.append(1)
    if i-3 >= 0:
        if numero in baralho[i-3] or naipe in baralho[i-3]:
            resultado.append(3) 

    return resultado
    

# Teste

print(cria_baralho())

print(extrai_valor('J♣'))
print(extrai_valor('10♠'))

print(extrai_naipe('J♣'))
print(extrai_naipe('10♠'))

# Código - Jogo de paciência Arcodeão

print('Jogo de paciência Acordeão')

print('===========================================================')


