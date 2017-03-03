import xlwt

def export(bugList):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('something',cell_overwrite_ok=True)

    title = ('product', 'module', 'kind', 'title', 'version', 'surroundings', 'describe', 'level', 'seriousnessd', 'setup', 'setuptime', 'appoint', 'starttime', 'endtime', 'state', 'source' )
    count =0
    for i in title:
        ws.write(0,count,title[count])
        count += 1

    rowcount = 1
    colcount = 0

    for bug in bugList:
        ws.write(rowcount,colcount,bug.product)
        colcount += 1
        ws.write(rowcount,colcount,bug.module)
        colcount += 1
        ws.write(rowcount,colcount,bug.kind)
        colcount += 1
        ws.write(rowcount,colcount,bug.title)
        colcount += 1
        ws.write(rowcount,colcount,bug.version)
        colcount += 1
        ws.write(rowcount,colcount,bug.surroundings)
        colcount += 1
        ws.write(rowcount,colcount,bug.describe)
        colcount += 1
        ws.write(rowcount,colcount,bug.level)
        colcount += 1
        ws.write(rowcount,colcount,bug.seriousnessd)
        colcount += 1
        ws.write(rowcount,colcount,bug.setup)
        colcount += 1
        ws.write(rowcount,colcount,bug.setuptime.strftime('%Y-%m-%d %H:%M:%S'))
        colcount += 1
        ws.write(rowcount,colcount,bug.appoint)
        colcount += 1
        ws.write(rowcount,colcount,bug.starttime.strftime('%Y-%m-%d'))
        colcount += 1
        ws.write(rowcount,colcount,bug.endtime.strftime('%Y-%m-%d'))
        colcount += 1
        ws.write(rowcount,colcount,bug.state)
        colcount += 1
        ws.write(rowcount,colcount,bug.source)
        colcount += 1


        colcount += 0
        rowcount += 1

    wb.save('ysk.xls')

    return 1