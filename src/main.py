import csv
import pandas as pd
import numpy as np
import os
import math
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

df = pd.read_csv('/Users/rushika/Desktop/e-commerce_bot/src/prod_small2.csv')
print(df.head())

product_description = []
product_description_len = []

print(type(df.columns)  )

for r in df.iterrows():
    product_data = []

    title = r[1]['TITLE']
    description = r[1]['DESCRIPTION']

    if type(title) == str and type(description) == str:
        product_data.append(title.strip() + ' ' + description.strip())
        product_description.append(product_data[0])
        product_description_len.append(len(product_data[0].split()))
        #print(f"Product {product_description} description length: {len(product_data[0].split())}")
#print(f"Number of elements {len(product_description)}")
#print(f"product_description_len: {product_description[2]}")



