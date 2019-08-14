import pandas as pd
import json
f = open('data.json', encoding='utf-8')
file = json.load(f)
for k, v in file.items():
    print(k, v)