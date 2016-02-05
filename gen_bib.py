#! /bin/sh
""":"
exec python3 "$0" ${1+"$@"}
"""
import argparse
import csv
import re
from datetime import datetime
from html_format import HTML_FORMAT

def readStyles(style_csv_fname):
    styles = {}
    f = open(style_csv_fname, encoding='sjis')
    reader = csv.reader(f)
    category_header = next(reader)[0]
    for style_name, style in reader:
        style = re.sub('{', '{0[', style)
        styles[style_name] = re.sub('}', ']}', style)
    return category_header, styles

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

def applyStyleToBib(style, bib):
    line = style.format(bib)
    line = re.sub('///(.*)///', '<I>\\1</I>', line)
    return line

def generateHTML(stylefname, biblistfname):
    category_header, styles = readStyles(stylefname)
    biblist = readBibList(biblistfname)
    body = ''
    for current_bib in biblist:
        selected_style = styles[current_bib.pop(category_header)]
        body += applyStyleToBib(selected_style, current_bib) + '<BR/>\n'
    outputfile = open('result.html', 'w', encoding='utf-8')
    outputfile.write(HTML_FORMAT.format(bib_body=body,
                                        time_stamp=datetime.now()))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('styles_csv_fname', action='store', nargs='?',
                        const=None, default='styles.csv', type=str)
    parser.add_argument('biblist_csv_fname', action='store', nargs='?',
                        const=None, default='biblist.csv', type=str)
    args = parser.parse_args()
    generateHTML(args.styles_csv_fname, args.biblist_csv_fname)


if __name__ == '__main__':
    main()
