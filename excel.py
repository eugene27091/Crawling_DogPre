import pandas as pd
import numpy as np
from itertools import chain

df = pd.read_csv('C:/Users/EUGENE/PycharmProjects/dogpre_final/dogPre2021_8_17_page10_20.csv')

def chainer(s):
    return list(chain.from_iterable(s.str.split(',')))

# calculate lengths of splits
lens = df['review_date'].str.split(',').map(len)

# 'item_name', 'review_title', 'review_content','review_date', 'review_star', 'dog_breed', 'dog_age'

# print(chainer(df['review_title']))
print(len(chainer(df['review_title'])))

# print(chainer(df['review_content']))
print(len(chainer(df['review_content'])))

res = pd.DataFrame({'item_name': np.repeat(df['item_name'],lens),
                    'review_title': chainer(df['review_title']),
                    'review_content': chainer(df['review_content']),
                    'review_date': chainer(df['review_date']),
                    'review_star': chainer(df['review_star']),
                    'dog_breed': chainer(df['dog_breed']),
                    'dog_age': chainer(df['dog_age'])})

res["review_total"] = res["review_title"].map(str) + " " + res["review_content"]
res = res.drop(columns = ['review_title', 'review_content'])

res.to_csv('10p_20(완성)' + '.csv', encoding='utf-8-sig')
print("Finish!")