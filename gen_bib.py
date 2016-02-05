#! /bin/sh
""":"
exec python3 "$0" ${1+"$@"}
"""
import csv
import re
from datetime import datetime
from html_format import HTML_FORMAT
def readStyles(style_csv_fname):
    styles = {}
    f = open(style_csv_fname, encoding='sjis')
    reader = csv.reader(f)
    next(reader)
    for style_name, style in reader:
        styles[style_name] = style
    return styles

def readBibList(biblist_csv_fname):
    f = open(biblist_csv_fname, encoding='sjis')
    reader = csv.reader(f)
    properties = next(reader)
    bib_list = []
    for bib in reader:
      current_bib = {}
      i = 0
      for i in range(len(properties)):
          current_bib[properties[i]] = bib[i]
      bib_list.append(current_bib)
    return bib_list

def applyStyleToBib(style, bib_dict):
    for prop, value in bib_dict.items():
        style = re.sub(prop, value, style)
        style = re.sub('///(.*)///', '<I>\\1</I>', style)
    return style

def generateHTML(stylefname, biblistfname):
    styles = readStyles(stylefname)
    biblist = readBibList(biblistfname)
    body = ''
    for bib in biblist:
        bib_style = styles[bib['Category']]
        body += applyStyleToBib(bib_style, bib) + '<BR/>\n'
    outputfile = open('result.html', 'w', encoding='utf-8')
    outputfile.write(HTML_FORMAT.format(bib_body=body,
                                        time_stamp=datetime.now()))

def main():
    generateHTML('styles.csv', 'biblist.csv')


if __name__ == '__main__':
    main()
