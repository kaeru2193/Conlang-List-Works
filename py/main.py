import csv
from convert import HTMLToTable, TableProcess, DataFormat
from bs4 import BeautifulSoup
import requests

url = 'https://migdal.miraheze.org/wiki/%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%9C%8F%E3%81%AE%E4%BA%BA%E5%B7%A5%E8%A8%80%E8%AA%9E%E3%81%AE%E4%B8%80%E8%A6%A7%E8%A1%A8'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

table = soup.select("div#mw-content-text > div.mw-parser-output table")[0] #wiki中から表部分を抽出

rawTable = HTMLToTable(table)
processedTable = TableProcess(rawTable)
formattedTable = DataFormat(processedTable)

outPath = r"./migdal-wiki-list.ctc"

f = open(outPath, 'w', encoding='UTF-8', newline="")
writer = csv.writer(f)
writer.writerows(formattedTable)
f.close()