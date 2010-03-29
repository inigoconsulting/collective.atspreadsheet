from zope import schema
from zope.interface import Interface

from collective.atspreadsheet import atspreadsheetMessageFactory as _


class ISpreadsheet(Interface):
    """A simple spreadsheet contenttype based on jQuery.sheet"""

    # -*- schema definition goes here -*-
