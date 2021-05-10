# Biblioteca

from random import shuffle
import os

os.system("")

# Group of Different functions for different styles

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def mostrar_baralho(baralho):
  j = 1
  for carta in baralho:
    if "♣" in carta : 
      print(style.WHITE + "{}.".format(j), style.BLUE + "{}".format(carta))
    elif "♠" in carta:
      print(style.WHITE + "{}.".format(j), style.GREEN + "{}".format(carta))
    elif "♥" in carta:
      print(style.WHITE + "{}.".format(j), style.RED + "{}".format(carta))
    else :
      print(style.WHITE + "{}.".format(j), style.MAGENTA + "{}".format(carta))
    j += 1

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
    
def empilha(baralho,origem,destino):
    baralho[destino] = baralho[origem]
    del baralho[origem]
    return baralho

def possui_movimentos_possiveis(baralho):
    
  for i in range(1,len(baralho)):
    if extrai_valor(baralho[i]) == extrai_valor(baralho[i-1]) or (extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1])):
      return True
    elif (extrai_valor(baralho[i]) == extrai_valor(baralho[i-3])) or (extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3])):
      return True
    else:
      return False


# Teste

print(cria_baralho())

print(extrai_valor('J♣'))
print(extrai_valor('10♠'))

print(extrai_naipe('J♣'))
print(extrai_naipe('10♠'))

# Código - Jogo de paciência Arcodeão

print('Jogo de paciência Acordeão')

print('=====================================================================')

# Iniciando o jogo


baralho = cria_baralho()

movimentos = [0]

while not possui_movimentos_possiveis(baralho) :
  baralho = cria_baralho()

