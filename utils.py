import collections
import re
import os
import xlwt


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)


def AnalyzeText(text_file, keywords):
    text = ""
    with open(text_file, encoding='utf8') as file:
        text = file.read()
    text = re.sub('[^\u4e00-\u9fa5]', '', text)

    stat = {}
    for key in keywords:
        stat[key] = text.count(key)

    return stat


def SetStyle(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def StatWriter(file_path, keywords, stats):
    xls = xlwt.Workbook()

    sheet = xls.add_sheet('Sheet', cell_overwrite_ok=True)
    row0 = [''] + keywords
    colum0 = list(stats.keys())

    for i in range(0, len(row0)):
        sheet.write(0, i, row0[i])
    for i in range(0, len(colum0)):
        sheet.write(i + 1, 0, colum0[i])
    for i in range(0, len(colum0)):
        for j in range(1, len(row0)):
            sheet.write(i + 1, j, stats[colum0[i]][row0[j]])

    xls.save(file_path)


def MergeDict(a, b):
    for key in a:
        a[key] += b[key]
    return a
