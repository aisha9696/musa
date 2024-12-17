import random
from collections import Counter


class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["\u2660", "\u2665", "\u2666", "\u2663"]

    def __init__(self, rank=0, suit=0):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.RANKS[self.rank] + self.SUITS[self.suit]


class Deck:
    def __init__(self):
        self.cards = []
        for rank in range(13):
            for suit in range(4):
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def give(self):
        random_card = random.choice(self.cards)
        self.cards.remove(random_card)
        return random_card

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + str(self.cards[i])
        return s


class Hand:
    def __init__(self):
        self.lst = []

    def take(self, card):
        self.lst.append(card)

    def __str__(self):
        s = "| 1   | 2   | 3   | 4   | 5   |\n"
        for i in range(len(self.lst)):
            s = s + f'| {str(self.lst[i]):^3} '
        s += "|"
        return s

    def change(self, num, card):
        self.lst[num - 1] = card


class Checker:
    @staticmethod
    def check(hand):
        need = True
        arr = []
        if need:
            for i in hand:
                arr.append(i.rank)
            c = Counter(arr)
            a = dict(c)
            d = list(a.values())

            if max(a.values()) == 4:
                need = False
                print("Four of kind - 8 scores")
            elif max(a.values()) == 3:
                if 2 in d:
                    print("Full house - 7 scores")
                else:
                    print("Three of kind - 4 scores")
                need = False
            elif max(a.values()) == 2:
                need = False
                print("Pair - 2 scores")
        if need:
            num = 0
            for i in hand:
                if i.rank > num:
                    num = i.rank
            for i in hand:
                if num == i.rank:
                    print(str(i) + " High card - 1 score")


class Application:
    @staticmethod
    def app():
        while True:
            deck = Deck()
            deck.shuffle()
            hand = Hand()
            for y in range(5):
                hand.take(deck.give())
            print(hand)
            a = input("Do you wanna change cards? Write numbers of cards (from 1 to 5) by "
                      "gap and press 'Enter' or press 'Enter' with no input if you don`t need: ")
            if a == "":
                Checker.check(hand.lst)
                again = input("Do you wanna play again? Write 'yes' if you want: ")
                if again.lower() == 'yes':
                    continue
                else:
                    break
            else:
                try:
                    lst = list(map(int, a.split()))
                    for y in lst:
                        for i in range(len(hand.lst)):
                            if i == y - 1:
                                hand.change(y, deck.give())
                    print(hand)
                    Checker.check(hand.lst)
                    again = input("Do you wanna play again? Write 'yes' if you want: ")
                    if again.lower() == 'yes':
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid input, game stopped. Please be careful next time "
                          "and write only numbers of cards")
                    again = input("Do you wanna play again? Write 'yes' if you want: ")
                    if again.lower() == 'yes':
                        continue
                    else:
                        break


Application.app()
