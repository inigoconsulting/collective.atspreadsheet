from Products.Archetypes.Registry import registerWidget
from Products.Archetypes.Widget import TextAreaWidget
from AccessControl import ClassSecurityInfo

class SpreadsheetWidget(TextAreaWidget):
   _properties = TextAreaWidget._properties.copy()
   _properties.update({
        'macro' : "spreadsheetwidget",
        'helper_js': ('jquery.sheet.min.js',
                      'jquery.scrollTo-min.js',
                      'jquery-ui-1.8.custom.min.js',
                      'jgcharts.min.js',
                      'spreadsheetwidget.js'),
        'helper_css' : ('jquery.sheet.css',
                         'jquery-ui-1.8.custom.css'),
        })

registerWidget(SpreadsheetWidget,
               title="SpreadSheetWidget",
               description=("Renders a jQuery spreadsheet"),
               used_for=('Products.Archetypes.Field.TextField'),
              )
