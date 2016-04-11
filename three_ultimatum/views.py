# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Offer(Page):
    form_model = models.Group
    form_fields = ['offered_coins']

    def is_displayed(self):
        return self.player.id_in_group == 1

    timeout_seconds = 600


class WaitForRecipient(WaitPage):
    pass


class Accept(Page):

    form_model = models.Group
    form_fields = ['offer_accepted']

    def is_displayed(self):
        return self.player.id_in_group == 2


class WaitForDictator(WaitPage):
    pass


class Punish(Page):
    form_model = models.Group
    form_fields = ["punish_dictator"]

    def is_displayed(self):
        return self.player.id_in_group == 3


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        return {"payoffs": self.player.payoff}

page_sequence = [
    Introduction,
    Offer,
    Accept,
    WaitForDictator,
    Punish,
    ResultsWaitPage,
    Results
]
