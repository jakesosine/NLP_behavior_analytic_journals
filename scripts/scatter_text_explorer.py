import scattertext as st
import re
import io
from pprint import pprint
import pandas as pd
import numpy as np
from scipy.stats import rankdata, hmean, norm
import spacy
import os
import pkgutil
import json
import urllib
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from IPython.display import IFrame
from IPython.core.display import display, HTML
from scattertext import CorpusFromPandas, produce_scattertext_explorer
display(HTML("<style>.container { width:98% !important; }</style>"))


nlp = spacy.load('en')


df = pd.read_excel(r'Book1.xlsx')
df['parsed'] = df.Text.apply(nlp)
print("Document Count")
print(df.groupby('Journal')['Text'].count())
print("Word Count")
print(df.groupby('Journal').apply(
    lambda x: x.Text.apply(lambda x: len(x.split()))))


corpus = st.CorpusFromParsedDocuments(
    df, category_col='Journal', parsed_col='parsed').build()

html = st.produce_scattertext_explorer(corpus,
                                       category='JABA',
                                       category_name='JABA',
                                       not_category_name='JEAB',
                                       width_in_pixels=1000,
                                       minimum_term_frequency=1,

                                       )
file_name = 'ScattertextScale.html'
open(file_name, 'wb').write(html.encode('utf-8'))
IFrame(src=file_name, width=1200, height=700)


# print(df.head())
