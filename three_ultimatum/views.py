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


class Results(Page):
    def vars_for_template(self):
        return {"payoffs":
                list([player.payoff for player in self.group.get_players()])}


page_sequence = [
    Introduction,
    Offer,
    Results
]
