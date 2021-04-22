import re
import pandas as pd
import os
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


#text = keywords_text(test_string, 'Key words:', 'posture')
#print(clean_text(text, "Key words:"))
path = '/Users/jacobsosine/Dropbox/'

df = pd.DataFrame()

methods = []
results = []
discussions = []
references = []

for root, dirs, files in os.walk(path):
    for file_ in files:
        if file_.endswith('.txt'):
            text_path = os.path.join(root, file_)
            print(text_path)

"""

            with open(text_path, 'r') as f:
                file_contents = f.read()
                method = text_gathering(
                    file_contents, 'METHOD', 'RESULTS')
                method = clean_text(method, "METHOD")
                methods.append(method)

                result = text_gathering(
                    file_contents, "RESULTS", "DISCUSSION")
                result = clean_text(result, "RESULTS")
                results.append(result)
                discussion = text_gathering(
                    file_contents, "DISCUSSION", "REFERENCES")
                discussion = clean_text(discussion, "DISCUSSION")
                discussions.append(discussion)
                reference = text_references(file_contents, "REFERENCES")
                references.append(reference)


df['methods'] = methods
df['results'] = results
df['discussions'] = discussions
df['references'] = references


print(df['methods'][30])
print(df['results'][30])
print(df['discussions'][30])
print(df['references'][30])

dataframe = df.applymap(lambda x: x.encode('unicode_escape').
                        decode('utf-8') if isinstance(x, str) else x)
#df.to_csv('first_run.csv', index=False, header=True)
#dataframe.to_excel('df.xlsx', index=True, header=True)
"""
