tuesmon-ncurses
=================

.. image:: http://kaleidos.net/static/img/badge.png
    :target: http://kaleidos.net/community/greenmine/
.. image:: https://tuesmon.com/media/support/attachments/article-22/banner-gh.png
    :target: https://tuesmon.com
.. image:: https://travis-ci.org/tuesmoncom/tuesmon-ncurses.svg?branch=master
    :target: https://travis-ci.org/tuesmoncom/tuesmon-ncurses
.. image:: https://coveralls.io/repos/tuesmoncom/tuesmon-ncurses/badge.svg?branch=master 
    :target: https://coveralls.io/r/tuesmoncom/tuesmon-ncurses?branch=master



A NCurses client for Tuesmon.

Project status
--------------

Currently on design phases: This project was a proof of concept to try to create a curses client 
for Tuesmon in the 6th `PiWeek`_. It isn't finished yet and currently it isn't 
feature complete. You can see some screenshots at https://github.com/tuesmoncom/tuesmon-ncurses/issues/4#issuecomment-57717386 

Setup development environment
-----------------------------

Just execute these commands in your virtualenv(wrapper):

.. code-block::

    $ pip install -r dev-requirements.txt
    $ python setup.py develop
    $ py.test               # to run the tests
    $ tuesmon-ncurses         # to run the app


Obviously you need the `tuesmon backend`_ and, if you don't fancy living in darkness,
you can use the `tuesmon web client`_, sometimes. :P

Note: tuesmon-ncurses only runs with python 3.3+.

Community
---------

Tuesmon has a `mailing list`_. Feel free to join it and ask any questions you may have.

To subscribe for announcements of releases, important changes and so on, please follow 
`@tuesmoncom`_ on Twitter.

.. _tuesmon backend: https://github.com/kaleidos/tuesmon-back
.. _tuesmon web client: https://github.com/kaleidos/tuesmon-front
.. _mailing list: http://groups.google.com/d/forum/tuesmoncom
.. _@tuesmoncom: https://twitter.com/tuesmoncom
.. _PiWeek: http://piweek.com
