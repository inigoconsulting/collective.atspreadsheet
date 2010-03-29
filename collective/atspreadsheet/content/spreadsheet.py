"""Definition of the Spreadsheet content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.document import ATDocument 
from Products.ATContentTypes.content.document import ATDocumentSchema 

from collective.atspreadsheet import atspreadsheetMessageFactory as _
from collective.atspreadsheet.interfaces import ISpreadsheet
from collective.atspreadsheet.config import PROJECTNAME
from collective.atspreadsheet.widget import SpreadsheetWidget

SpreadsheetSchema = ATDocumentSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

SpreadsheetSchema['text'].widget = SpreadsheetWidget(label='Spreadsheet')
SpreadsheetSchema['presentation'].widget.visible = {'edit':'invisible','view':'invisible'}
SpreadsheetSchema['tableContents'].widget.visible = {'edit':'invisible','view':'invisible'}

schemata.finalizeATCTSchema(SpreadsheetSchema, moveDiscussion=False)


class Spreadsheet(ATDocument):
    """A simple spreadsheet contenttype based on jQuery.sheet"""
    implements(ISpreadsheet)

    meta_type = "Spreadsheet"
    schema = SpreadsheetSchema

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Spreadsheet, PROJECTNAME)
