import pandas as pd
from glob import glob
import os
import json

for f in glob(os.path.join('data', 'pan', f'*.parquet')):
    df = pd.read_parquet(f)
    lang = os.path.basename(f).split('-')[0]
    # print(df.head())

    df.to_csv(os.path.join('data', 'pan', f'{lang}.tsv'), sep='\t', index=False)

    # text_list = [x for x in df['text'].tolist() if x.count(' ') == 0]
    # with open(f'data/{lang}_toxic_vocab.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(text_list, json_file, indent=2)