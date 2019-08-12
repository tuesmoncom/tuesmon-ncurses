# -*- coding: utf-8 -*-

"""
tuesmon_ncurses.cli
~~~~~~~~~~~~~~~~~
"""

from tuesmon_ncurses.api.client import TuesmonClient
from tuesmon_ncurses.core import TuesmonCore
from tuesmon_ncurses.config import settings
from tuesmon_ncurses.executor import Executor


def main():
    settings.load()
    client = TuesmonClient(settings.host)
    if settings.data.auth.token:
        client.set_auth_token(settings.data.auth.token)
    executor = Executor(client)
    program = TuesmonCore(executor, settings, authenticated=settings.data.auth.token)
    program.run()
