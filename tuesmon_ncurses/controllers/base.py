# -*- coding: utf-8 -*-

"""
tuesmon_ncurses.controllers.base
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


class Controller:
    view = None

    def handle(self, key):
        return key
