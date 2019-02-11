#!/usr/bin/env python
from cleo import Application

from . import __version__

application = Application("annicli", __version__, complete=True)
