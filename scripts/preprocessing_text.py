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


test_string = '''Kennedy, C. H. (2005). Single-case designs for educational
research. Boston: Pearson.

Krause, K., & Patrick, K. (2001, February 14). School
held bomb-like item 2 days. Sunsentinel.com.
Retrieved February 6, 2017 from http://articles.
sun-sentinel.com/2001-02-14/news/0102140266_1_
bomb-like-device-sheriff-s-bomb-suspicious-devices.

Krisberg, K. (2007). Planning ahead for health threats—
school preparedness crucial for safety of children,
communities. The Nation’s Health, 1, 20-21.

Logothetis, N. K., & Sheinberg, D. L. (1996). Visual

object recognition. Annual Review of Neuroscience,

19, 577-621. doi: https://doi-org/10.1146/annurev.
ne.19.030196.003045

Lu, S., Zhang, J., & Feng, D. (2006, November). A
knowledge-based approach for detecting unattended
packages in surveillance video. In JEEE International
Conference on Video and Signal Based Surveillance,
2006. (pp. 110-110). Sydney, Australia: IEEE.

Lynch, M. D. (2005). Developing a scenario-based train-
ing program: Giving officers a tactical advantage. FBI
Law Enforcement Bulletin, 74, \.

Maren, S. (2001). Neurobiology of Pavlovian fear condi-
tioning. Annual Review of Neuroscience, 24, 897-931.
doi: https://doi-org/10.1146/annurev.neuro.24.1.897

Miltenberger, R. G., Gatheridge, B. J., Satterlund, M.,
Egemo Helm, K. R., Johnson, B. M., Jostad, C....
Flessner, C. A. (2005). Teaching safety skills to chil-
dren to prevent gun play: An evaluation of in situ
training. Journal of Applied Behavior Analysis, 38,
395-398. doi: _ https://doi.org/10.1901/jaba.2005.
130-04

Miltenberger, R. G., & Olsen, L. A. (1996). Abduction
prevention training: A review of findings and issues
for future research. Education & Treatment of
Children, 19, 69-82.

Mujtaba, H., Haider, Z., Cameron-Moore, S., &
Tarrant, B. (2009, April 26). Weekend blasts kill
16 children in Pakistan. Reuters. Retrieved February
6, 2017, from http://af.reuters.com/article/newsOne/
idAFTRE53027920090426?pageNumber=2 &virtual
BrandChannel=0&sp=true

Shemkus, S. (2006, January 6). Tennis ball bomb sparks
fear in Fairhaven. Southcoast Today. Retrieved
February 6, 2017, from http://www.southcoasttoday.
com/article/20060106/News/301069998'''


#text = keywords_text(test_string, 'Key words:', 'posture')
#print(clean_text(text, "Key words:"))


df = pd.DataFrame()

methods = []
results = []
discussions = []
references = []

for root, dirs, files in os.walk('../txt_files'):
    for file_ in files:
        if file_.endswith('.txt'):
            text_path = str(root) + '/' + str(file_)
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
