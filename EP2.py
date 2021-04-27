# Jogo de paciência acordeão
print('Jogo de paciência acordeão')

print('===========================================================')


from random import shuffle

def cria_baralho():
    cartas = ['A♣','K♣','Q♣','J♣','10♣','9♣','8♣','7♣','6♣','5♣','4♣','3♣','2♣','A♠','K♠','Q♠','J♠','10♠','9♠','8♠','7♠','6♠','5♠','4♠','3♠','2♠','A♦','K♦','Q♦','J♦','10♦','9♦','8♦','7♦','6♦','5♦','4♦','3♦','2♦','A♥','K♥','Q♥','J♥','10♥','9♥','8♥','7♥','6♥','5♥','4♥','3♥','2♥']
    lista = shuffle(cartas)
    return cartas

def extrai_naipe(carta):
    if carta == '10♣' or carta == '10♥' or carta == '10♠' or carta == '10♦':
        return carta[2]
    else:
        return carta[1]



print(cria_baralho())
print(extrai_naipe('J♣'))
print(extrai_naipe('10♠'))

