import re
import pandas as pd
# passes an open text file through this function with a start and end string to return what is between those two values.


def text_gathering(opened_file, start_identifier, end_identifier):
    start = opened_file.find(start_identifier)
    end = opened_file.find(end_identifier)
    return opened_file[start:end]


# This is specifically used to return the location, to the end of the text file (used here for references)
def text_references(opened_file, start_identifier):
    start = opened_file.find(start_identifier)
    return opened_file[start:]

# Identifying the keywords:


def keywords_text(opened_file, start_identifier, end_identifier):
    start = opened_file.find(start_identifier)
    end = opened_file.find(end_identifier)
    return opened_file[start:end]


def clean_text(text, start_identifier):
    text = text.replace(start_identifier, "")
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"how's", "how is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"n't", " not", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", text)
    return text


test_string = '''Key words: ambulation responses, microswitches, multiple disabilities, indices of happiness,
contingency, quality of life, social validation

Children with severe to profound develop-
mental, disabilities
sometimes present with gait and posture'''


#text = keywords_text(test_string, 'Key words:', 'posture')
#print(clean_text(text, "Key words:"))


df = pd.DataFrame()


# Open file With context manager
with open('txt_files/article978.txt', 'r') as f:
    f_contents = f.read()
    #print(keywords_text(f_contents, 'Key words', 'METHOD'))
    method = (text_gathering(f_contents, "METHOD", "RESULTS"))
    method = clean_text(method, "METHOD")
    # print(method)
    results = text_gathering(f_contents, "RESULTS", "REFERENCES")
    print(results)
    #print(text_references(f_contents, "REFERENCES"))
