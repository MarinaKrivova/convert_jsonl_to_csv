import pandas as pd
import glob
import os
import json
from pandas.io.json import json_normalize
import json_lines
os.chdir('json')

for file in glob.glob("*.jsonl"):
    #print(file)
    with open(file, 'rb') as f:
        contents =[]
        for item in json_lines.reader(f):
            contents.append(item)
            
    content_n=json_normalize(contents)
    content_n.to_csv(file.split('.')[0]+'.csv')