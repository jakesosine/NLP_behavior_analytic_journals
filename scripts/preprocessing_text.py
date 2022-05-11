import re
import pandas as pd
import os
import numpy as np
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.tag import StanfordNERTagger
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
import string
import re
import seaborn as sns
from nltk.util import ngrams
#not needed
nltk.download('punkt')
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import collections
#from normalise import normalise
from nltk.corpus import wordnet as wn
from nltk import pos_tag
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


# passes an open text file through this function with a start and end string to return what is between those two values.
def remove_proper_noun_singular(text):
    word_tokens = word_tokenize(text)
    tagged_sentence = pos_tag(word_tokens)
    text = [word for (word,tag) in tagged_sentence if tag not in set(['NNP',"NNPS"])]
    joined = ' '.join(text)
    return joined

def remove_url(text):
    text = re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '', text)
    return text

def remove_whitespace(text):
    return  " ".join(text.split())

def remove_html(text):
    soup = BeautifulSoup(text,'lxml')
    html_free = soup.get_text()
    return html_free

def remove_numbers(text):
    number_free = re.sub(r'\d+', '', text)
    return number_free

def remove_punctuation_with_period(text):
    punct = set(string.punctuation)
    text = text.lower()
    text = "".join([c for c in text if c not in punct])
    text = re.sub(r"""[()\’°"#/@;¢€:£<“>{}«®`©”+=~‘|.!?,]""", "", text)
    text = re.sub(r'/[^a-zA-Z]',"",text)
    text = " ".join(text.split())
    return text


def remove_stopwords(text):
    stopwords_ = set(stop_words)
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stopwords_]
    text = " ".join(filtered_text)
    return text


def word_lemmatizer(text):
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(text)
    lem_text = " ".join([lemmatizer.lemmatize(i)for i in word_tokens])
    return lem_text


def word_stemmer(text):

    word_tokens = word_tokenize(text)
    stem_text = " ".join([stemmer_port.stem(i) for i in word_tokens])
    return stem_text

if __name__ == '__main__':
    df = pd.read_csv('../data/all_text_articles.csv')
    df['removed']  = df['text'].apply(lambda x: remove_proper_noun_singular(x))
    df['removing_url'] = df['removed'].apply(lambda x: remove_url(x))
    df['remove_whitespaces'] = df['removing_url'].apply(lambda x: remove_whitespace(x))
    df['text_less_html'] = df['remove_whitespaces'].apply(lambda x: remove_html(x))
    df['numbers_removed'] = df['text_less_html'].apply(lambda x: remove_numbers(x))
    df['punct_removed'] = df['numbers_removed'].apply(lambda x: remove_punctuation_with_period(x))
    lst = ['eg','et','al','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','doi','ry','baa','rya','og','cs']
    stop_words = stopwords.words("english")
    for i in lst:
        stop_words.append(i)
        print(stop_words)
    df['stopwords_removed'] = df['punct_removed'].apply(lambda x: remove_stopwords(x))
    df['lemmatization'] = df['stopwords_removed'].apply(lambda x: word_lemmatizer(x))
    df['porter_stemmed'] = df['lemmatization'].apply(lambda x: word_stemmer(x))
    df['word_count'] = df['text'].apply(lambda x: len(str(x).split()))
    data_frame = df[['text','years','journals','file_path','lemmatization', 'word_count']]
    data_frame.to_csv('../data/Only_essential_columns.csv')
