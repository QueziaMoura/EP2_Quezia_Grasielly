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
def cria_baralho():
    cartas = ['A♣','K♣','Q♣','J♣','10♣','9♣','8♣','7♣','6♣','5♣','4♣','3♣','2♣','A♠','K♠','Q♠','J♠','10♠','9♠','8♠','7♠','6♠','5♠','4♠','3♠','2♠','A♦','K♦','Q♦','J♦','10♦','9♦','8♦','7♦','6♦','5♦','4♦','3♦','2♦','A♥','K♥','Q♥','J♥','10♥','9♥','8♥','7♥','6♥','5♥','4♥','3♥','2♥']
    shuffle(cartas)
    return cartas

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
    numero = extrai_valor(baralho[i])

    naipe = extrai_naipe(baralho[i])

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
    if (extrai_valor(baralho[i]) == extrai_valor(baralho[i-3])) or (extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3])):
      return True
    return False



# Código - Jogo de paciência Arcodeão

print('Jogo de paciência Acordeão')

print('=====================================================================')

print('Seja bem-vindo(a) ao jogo de Paciência Acordeão!')

print('O objetivo deste jogo é colocar todas as cartas em uma mesma pilha\n')

print('Existem apenas dois movimentos possíveis: ')

print('1. Empilhar uma carta sobre a carta imediatamente anterior;')
print('2. Empilhar uma carta sobre a terceira carta anterior.\n')

print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n')

print('- As duas cartas possuem o mesmo valor ou \n- As duas cartas possuem o mesmo naipe.\n')



# Iniciando o jogo


baralho = cria_baralho()

movimentos = [0]

while not possui_movimentos_possiveis(baralho) :
  baralho = cria_baralho()

input('Aperte [Enter] para iniciar o jogo... \n')

while True:
  print('O estado atual do baralho é:\n')

  mostrar_baralho(baralho)
  print('')

  i = int(input("Escolha uma carta (digite um número entre 1 e {}): ".format(len(baralho))))
  i = i - 1 #Para que o usuário acesse a lista a posição correspondente ao valor digitado (1 - 52)
            #Já que o primeiro elemento da lista corresponde a zero e o digitado pelo usuário para acessá-lo é 1
            
#########################################################################

 while True:
    
    if 1 < i < len(baralho):
      movimentos = lista_movimentos_possiveis(baralho,i)
      if len(movimentos) != 0:
        break
      if len(movimentos) == 0:
        i = int(input("A carta {} não pode ser movida. Por favor, digite um número entre 1 e {}: ".format(baralho[i],len(baralho))))
        i = i - 1
        
    if not (1 < i < len(baralho)):
      i = int(input("Posição inválida. Por favor, digite um número entre 1 e {}: ".format(len(baralho))))
      i = i - 1
      
#########################################################################