from zope import schema
from zope.interface import Interface

from collective.atspreadsheet import atspreadsheetMessageFactory as _


class ICSVSpreadsheet(Interface):
    """A contenttype to display a spreadsheet from CSV file"""

    # -*- schema definition goes here -*-
