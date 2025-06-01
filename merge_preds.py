import pandas as pd
from os.path import join, basename
from glob import glob

for sub in glob(join('preds', 'en', '*_sub.tsv')):
    sub_fname = basename(sub)
    ref_fname = sub_fname.replace('_sub', '_ref')

    en_sub_df = pd.read_csv(sub, sep='\t')
    # print(len(en_sub_df))
    es_sub_df = pd.read_csv(join('preds', 'es', sub_fname), sep='\t')
    # print(len(es_sub_df))

    en_ref_df = pd.read_csv(join('preds', 'en', ref_fname), sep='\t')
    es_ref_df = pd.read_csv(join('preds', 'es', ref_fname), sep='\t')

    sub_df = pd.concat([en_sub_df, es_sub_df])
    sub_df.reset_index(inplace=True,drop=True)

    ref_df = pd.concat([en_ref_df, es_ref_df])
    ref_df.reset_index(inplace=True,drop=True)
    # print(en_sub_df.head())
    # print(en_sub_df.tail())
    # print(len(en_sub_df))

    sub_df.to_csv(join('preds', sub_fname), sep='\t')
    ref_df.to_csv(join('preds', ref_fname), sep='\t')
    # break