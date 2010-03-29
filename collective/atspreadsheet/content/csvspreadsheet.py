"""Definition of the CSVSpreadsheet content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from collective.atspreadsheet.content.spreadsheet import SpreadsheetSchema
from collective.atspreadsheet.content.spreadsheet import Spreadsheet

from collective.atspreadsheet import atspreadsheetMessageFactory as _
from collective.atspreadsheet.interfaces import ICSVSpreadsheet
from collective.atspreadsheet.config import PROJECTNAME

CSVSpreadsheetSchema = SpreadsheetSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.FileField('file',
           required= True,
           widget=atapi.FileField._properties['widget'](label=_(u'File'),
                     description=_("Upload CSV here. The first row of the CSV will be used as the header")
           )
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CSVSpreadsheetSchema['text'].widget.visible = {'edit':'invisible','view':'visible'}
CSVSpreadsheetSchema['text'].required = False

schemata.finalizeATCTSchema(CSVSpreadsheetSchema, moveDiscussion=False)


class CSVSpreadsheet(Spreadsheet):
    """Display a spreadsheet of a CSV file"""
    implements(ICSVSpreadsheet)

    meta_type = "CSVSpreadsheet"
    schema = CSVSpreadsheetSchema

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(CSVSpreadsheet, PROJECTNAME)
