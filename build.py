"""
事前にcsvファイルをダウンロードしておく
curl -o items.csv https://raw.githubusercontent.com/kagasan/sample_repository/main/sample.csv

python3 build.py
でdocsにitems.jsonを吐き出す
"""

import csv
import json

with open('items.csv') as file:
    reader = csv.reader(file)
    rows = [row for row in reader][1:]
    data = {
        'items': [{'item': row[0], 'value': row[1]} for row in rows]
    }
    with open('docs/items.json', 'w') as f:
        json.dump(data, f)
