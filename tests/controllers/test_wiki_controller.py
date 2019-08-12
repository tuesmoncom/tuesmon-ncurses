from concurrent.futures import Future
from unittest import mock

from tuesmon_ncurses.ui import signals, views
from tuesmon_ncurses import controllers, config
from tuesmon_ncurses.executor import Executor
from tuesmon_ncurses.core import StateMachine

from tests import factories


