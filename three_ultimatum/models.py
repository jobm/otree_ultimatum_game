# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

from random import randrange as r_range

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'three_ultimatum'
    players_per_group = 3
    num_rounds = 1
    endowment = c(10)
    if_offer_rejected = c(0)
    offer_increment = c(5)
    offered_choices = currency_range(0, endowment + 1, offer_increment)


class Subsession(BaseSubsession):
    def before_session_starts(self):
        dictator, recipient, punisher = self.get_players()
        dictator.payoff = 10
        recipient.payoff = 10
        punisher.payoff = 10


class Group(BaseGroup):
    offered_coins = models.CurrencyField(choices=Constants.offered_choices)

    offer_accepted = models.BooleanField()

    response_0 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_5 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_10 = models.BooleanField(widget=widgets.RadioSelectHorizontal())

    def set_payoffs(self):
        dictator = self.get_player_by_id(1)
        recipient = self.get_player_by_id(2)
        punisher = self.get_player_by_id(3)
        # if offer is accepted the punisher does not get involved/punish
        if self.offer_accepted:
            dictator.payoff = Constants.endowment - self.amount_offered
            recipient.payoff = self.amount_offered
            punisher.payoff = 0

        # if the offer is rejected the punisher get invoved and deducts payoff
        # from the dictator or player one
        else:
            # dictators pay is cut in half by the punisher
            dictator.payoff = Constants.endowment / 2
            # recipient gets a quater off the dictators payoff
            recipient.payoff = (dictator.payoff / 2) / 4
            # punisher gets a quater off the dictators payoff
            punisher.payoff = (dictator.payoff / 2) / 4


class Player(BasePlayer):
    pass
