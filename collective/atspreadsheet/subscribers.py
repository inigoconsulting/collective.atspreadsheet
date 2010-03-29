import csv
import StringIO

def generateTable(context,event):
    textmutator = context.Schema().getField('text').getMutator(context)
    csvfile = context.Schema().getField('file').getAccessor(context)()
    out = StringIO.StringIO()

    if csvfile.content_type != 'text/comma-separated-values':
       textmutator('<tr><td>File is not proper CSV, mimetype = %s</tr></tr>' % csvfile.content_type)
       return

    io = StringIO.StringIO(csvfile.data)
    reader = csv.reader(io)

    header = reader.next()

    # write colgroup
    out.write('<colgroup>')
    for i in header:
        out.write('<col width="%(width)sem" style="width: %(width)sem;">' % dict(width=len(i)+10))
    out.write('</colgroup>')

    out.write('<tbody>')
    out.write('<tr><td class="styleBold">')
    out.write('</td><td class="styleBold">'.join(header))
    out.write('</td></tr>\n')

    for line in reader:
        out.write('<tr><td>')
        out.write('</td><td>'.join(line))
        out.write('</td></tr>\n')

    out.write('</tbody>')
    textmutator(out.getvalue())
    context.reindexObject()
