import re
from datetime import datetime, timezone

from utils import AddCategoryData

defaultClass = [
    "name",
    "period",
    "creator",
    "desc",
    "world",
    "category",
    "desc",
]

classTable = [
    {"name": r"^twitter$", "category": "twitter"},
    {"name": r"^漢字言語名$", "category": "kanji"},
    {"name": r"^サイト[0-9]*$", "category": "site"},
    {"name": r"^辞書[0-9]*$", "category": "dict"},
    {"name": r"^文法[0-9]*$", "category": "grammar"},
    {"name": r"^異称$", "category": "name"},
    {"name": r"^説明$", "category": "example"},
    {"name": r"^表記$", "category": "script"},
]

categories = [
    "messier",
    "name",
    "kanji",
    "desc",
    "creator",
    "period",
    "site",
    "twitter",
    "dict",
    "grammar",
    "world",
    "category",
    "moyune",
    "cla",
    "part",
    "example",
    "script"
]

types = [
    "Any",
    "Array[NString]",
    "Array[NString]",
    "Array[NString]",
    "Array[NString]",
    "DateRange",
    "Array[Url]",
    "Array[Url]",
    "Array[NString]",
    "Array[NString]",
    "Array[NString]",
    "Array[Union[Pair[NString,NString],NString]]",
    "Array[MoyuneClass]",
    "Array[LangCode]",
    "Any",
    "Array[NString]",
    "Array[NString]"
]

def HTMLToTable(elem):
    tableArr: list[list[str]] = []
    rows = elem.find_all("tr")
    for row in rows: #1行ごとに処理
        rowArr = []
        for idx, cell in enumerate(row.findAll(['td', 'th'])): #1マスごとに処理
            for i in cell.select("br"): #brタグを改行に置換
                i.replace_with('\n')

            for a in cell.select("a"): #リンク周りの処理
                processed = ""

                if (idx == 6):
                    processed = a.get_text() + ": " + a.get("href") #資料欄のリンクはテキスト+urlで置換
                elif (idx == 2):
                    processed = a.get("href") #作者欄のリンク（ほぼTwitter）をurlで置換
                else:
                    processed = a.get_text() #その他のリンクは全てテキストとして置換

                a.replace_with(processed + "\n")
            
            trimed: str = cell.get_text().replace(u"\xa0", u" ").strip() #xa0(ノーブレークスペース)を通常のスペースに置き換え
                
            rowArr.append(trimed)
        tableArr.append(rowArr)

    return tableArr[1:len(tableArr)]

def splitValue(data):
    values = data.split(",") #カンマ区切り (複数のデータを持つ項目)を分割
    cleanValues = [str.strip(d) for d in values] #項目の空白削除

    return cleanValues

def TableProcess(tableArr):
    processArr = []
    for row in tableArr: #1行が1言語
        langEntry = [[""] for _ in range(17)]
        for idx, cell in enumerate(row):
            splitted = cell.split("\n")
            for data in splitted: #表の行ごとの処理
                categoryReg = re.compile(r"^(.+?):(.*)")
                result = categoryReg.search(data)
                
                if (idx == 5): #分類欄である場合、処理が特殊になる
                    values = splitValue(data)
                    converted = []
                    for value in values:
                        reg = categoryReg.search(value)
                        if (reg):
                            tag = str.strip(reg.group(1)) #コロン前のタグ名を抽出&前後の空白削除
                            tagValue: str = str.strip(reg.group(2))
                            converted.append(tag + ":" + tagValue)
                        else:
                            converted.append(value)
                    AddCategoryData(langEntry, "category", converted, categories)
                elif (result): #コロン付きの形式である場合
                    category = str.strip(result.group(1)) #カテゴリ名(コロン前)抽出&前後の空白削除
                    content: str = str.strip(result.group(2))
                    flag = False
                    for cat in classTable:
                        if (re.compile(cat["name"]).match(category)):
                            AddCategoryData(langEntry, cat["category"], splitValue(content), categories) #カテゴリ名がいずれかの正規表現に当てはまればその列へ追加
                            flag = True
                            break
                    if (not(flag)): #コロン付きであるにも関わらず該当するものが見つからない場合
                        AddCategoryData(langEntry, defaultClass[idx], splitValue(data), categories) #そのままのテキスト形式でデフォルトの欄に追加
                else: #コロン付きでない場合
                    AddCategoryData(langEntry, defaultClass[idx], splitValue(data), categories) #デフォルトの欄に追加
        processArr.append(langEntry)

    return processArr

def DataFormat(data):
    cleaned = []
    for row in data:
        rowArr: list[str] = []
        for cell in row:
            noBrank = re.compile(r"\S")
            trimed: list[str] = [a for a in cell if noBrank.match(a)]
            rowArr.append(";".join(trimed))
        cleaned.append(rowArr)

    head = [
        str(len(cleaned)) + "x" + str(len(categories)),
        "日本語圏の人工言語の一覧表 Cotec変換済みデータ",
        "みかぶる (Mikanixonable), かえる (kaeru2193), Migdal Conlang Wiki上の記事編集者",
        "2024-03-09T00:00:00.000Z",
        datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
        "CC BY-SA 4.0",
        "© みかぶる (Mikanixonable), かえる (kaeru2193), Migdal Conlang Wiki上の記事編集者 under CC BY-SA 4.0",
        "0"
    ]

    result = [head, categories, types] + cleaned #すべてのデータを纏める

    return result