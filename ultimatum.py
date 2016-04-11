from random import randrange as r_r, shuffle
"""
this is my logic for a simple three player ultimatum,
a game theory algorithm that involves three parties, a dictator, a recipient &
an observer.
1. dictator => someone making the offer,
2. recipient => someone listening to the offer,
3. Sobserver => someone that observes and punishes accordingly.
"""

"""
##rules of the game
every party starts off with an endowment or at least on party, the dicating
party then makes an offer, the rules are:

1. if the party has $100 dollars and he offers less than that, the recipient
   will deny or accept the offer, logic dictates he/she will deny the offers.
2. the observer has the right to punish for an offer less than half i.e. $50.
3. the obser can punish the recipient for refusing an offer >= half >
   i.e. more than or $50
4. the observer can reward themselves after punishing a party with the amoung
   they deducted.
"""

class Dictator(object):
    # gold_coins = 10

    def __init__(self):
        self.gold_coins = 10

    # this is where the dictator make the offer, in this case a random one
    def offer(slef):
        return int(r_r(0, self.gold_coins + 1, 5))


class Recipient(object):
    # gold_coins = 10

    def __init__(self):
        self.gold_coins = 10

    # always deny any offer
    def deny_always(self, offered_gold_coins):
        return False

    # always accept any offer
    def accept_always(seld, offered_gold_coins):
        return True

    # think about the offer
    def accept_deny_think(self, offered_gold_coins):
        return True if offered_gold_coins > 5 else False


class Observer(object):
    dictator = Dictator()
    recipient = Recipient()

    def __init__(self, offer, lst_responses=[]):
        self.offer = offer
        self.lst_responses = lst_responses
        self.gold_coins = 10

    # punish accordingly
    def reward_punish(self):
        if self.offer >= 5:
            rand_list_responses = self.lst_responses
            shuffle(rand_list_responses)
            if [bool(response) for response in rand_list_responses][0]:
                recipient.gold_coins += self.offer
                dictator.gold_coins -= self.offer
            else:
                recipient.gold_coins -= self.offer
                self.gold_coins += self.offer / 2
                dictator.gold_coins += self.offer / 2
        else:
            dictator.gold_coins -= self.offer


if __name__ == "__main__":

    dictator = Dictator()
    recipient = Recipient()

    observer = Observer(dictator.offer(),
                        [recipient.accept_deny_think(dictator.offer()),
                         recipient.accept_always(dictator.offer()),
                         recipient.deny_always(dictator.offer())])

    print("****Before dealing*****")
    print(dictator.gold_coins)
    print(observer.gold_coins)
    print(recipient.gold_coins)

    # observer.reward_punish_dictator()

    observer.reward_punish()

    print("****After dealing*****")
    print("Dictator", dictator.gold_coins)
    print("Recipient", recipient.gold_coins)
    print("Observer", observer.gold_coins)
