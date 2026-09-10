import csv
import pandas as pd
import numpy as np
import os
import math
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.output_parsers import StrOutputParser
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

DATA_FILE = Path(__file__).parent / "prod_small2.csv"

load_dotenv()
if not os.getenv("OPENAI_API_KEY") and os.getenv("openai_api_key"):
    os.environ["OPENAI_API_KEY"] = os.environ["openai_api_key"]

df = pd.read_csv(DATA_FILE)

if not os.getenv("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY is not set. Set it before running the app.")
else:
    client = OpenAI()
#print(df.head())

product_description = []
product_description_len = []

#print(type(df.columns)  )

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

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=False
)

documents = text_splitter.create_documents(product_description)
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)

llmBrain = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.0, max_tokens=500)
output_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template(
    """Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}"""
)

documents_chain = create_stuff_documents_chain(llmBrain, prompt)

retrieval_chain = create_retrieval_chain(
    vectorstore.as_retriever(),
    documents_chain
)

retrieval_chain.invoke({"input": "what are some of the best shoes available?"})

print("Retrieval chain invoked successfully.")
print(f"response: {retrieval_chain.invoke({'input': 'what are some of the best shoes available?'})} ")






