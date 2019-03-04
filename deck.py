import random
cards = []
def deck():
    kolor = ["s", "c", "h", "d"]
    wartosc = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for i in kolor:
        for j in wartosc:
            cards.append((j, i))
    return cards

def shuffle_deck(lista):
    random.shuffle(lista)
    return lista

def deal(deck, n):
    dealt = []
    for i in range(n):
        templist = []
        for j in range(5):
            templist.append(deck.pop(0))
        dealt.append(templist)
        print('Gracz',i+1,':',templist)
    return dealt
