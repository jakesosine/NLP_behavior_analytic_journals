import re
import pandas as pd
import os
import spacy
from spacy.matcher import Matcher


#%%
nlp = spacy.load('en')  
matcher = Matcher(nlp.vocab)



#%%


def extract_full_name(nlp_doc):
     pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
     matcher.add('FULL_NAME', None, pattern)
     matches = matcher(nlp_doc)
     for match_id, start, end in matches:
         span = nlp_doc[start:end]
         return span.text









year = '2020'
journal = 'Journal of Applied Behavior Analysis'
issue = '52'

def text_gathering(opened_file, start_identifier, end_identifier):
    start = opened_file.find(start_identifier)
    end = opened_file.find(end_identifier)
    return opened_file[start:end]


# This is specifically used to return the location, to the end of the text file (used here for references)
def text_references(opened_file, start_identifier):
    start = opened_file.find(start_identifier)
    return opened_file[start:]
#%%


df = pd.DataFrame()
journals = []
years = []
pages = []
volumes = []
issues = []
titles = []
authors = []
abstracts = []
keywords = []
introductions = []
methods = []
results = []
discussions = []
references = []
quick_reviews = []
file_names = []
peoples = []
#%%
for root, dirs, files in os.walk('../txt_files'):
    for file in files:
        if file.endswith('.txt'):
            text_path = os.path.join(root, file)
            with open(text_path, 'r') as f:
                file_contents = f.read()
                start_of_file = file_contents[:75]
                pattern = re.compile(r'[0-9]+-[0-9]+')
                matches = pattern.finditer(start_of_file)
                file_names.append(file)
                for match in matches:
                    pages.append(match.group(0))
                years.append(year)
                issues.append(issue)
                close_to_title =file_contents[40:222]


#%%
               
for root, dirs, files in os.walk('../txt_files'):
    for file in files:
        if file.endswith('.txt'):
            text_path = os.path.join(root, file)
            with open(text_path, 'r') as f:
                file_contents = f.read()
                file_names.append(file)
                start_of_file = file_contents[:400]
                print(extract_full_name(start_of_file))
                print(start_of_file)
                author = input('enter authors: ')
                authors.append(author)


#%%
for root, dirs, files in os.walk('../txt_files'):
    for file in files:
        if file.endswith('.txt'):
            text_path = os.path.join(root, file)
            with open(text_path, 'r') as f:
                file_contents = f.read()
                file_names.append(file)
                start_of_file = file_contents[:400]
                print(start_of_file)
                page = input('Enter Page Number: ')
                pages.append(page)
                volume = input('enter volume: ')
                volumes.append(volume)
                title = input('enter a title: ')
                titles.append(title)
                print(file_contents[:1900])
                author = input('enter authors: ')
                authors.append(author)
                abstract = input('Enter Abstract:')
                abstracts.append(abstract)
                keyword = input('enter keywords: ')
                issue = input('enter issue: ')
                issues.append(issue)        
                keywords.append(keyword)
                
#%%
df['file_name'] = file_names
#%%
df['page_num'] = pages

#%%
df['volume'] = volumes
#%%
df['issue'] = issues
#%%
df['titles'] = titles
#%%
df['authors'] = authors
#%%
df['abstract'] = abstracts
#%%
df['keywords'] = keywords
#%%

df.to_csv(f'../{journal}_{year}.csv')
df.to_excel(f'../{journal}_{year}.xlsx')
                




#%%
df['introduction'] = introductions
df['methods'] = methods
df['results'] = results
df['discussions'] = discussions
df['references'] = references
df.to_csv(f'../{journal}_{year}.csv')
df.to_excel(f'../{journal}_{year}.xlsx')
                
                df['journal'] = journals
df['year'] = years
                
                
#%%
                introduction = text_gathering(file_contents, input(
                    "Enter two starting words"), 'METHOD')
                introductions.append(introduction)
                method = text_gathering(
                    file_contents, 'METHOD', 'RESULTS')
                methods.append(method)
                result = text_gathering(
                    file_contents, "RESULTS", "DISCUSSION")
                results.append(result)
                discussion = text_gathering(
                    file_contents, "DISCUSSION", "REFERENCES")
                discussions.append(discussion)
                reference = text_references(file_contents, "REFERENCES")
                references.append(reference)
                years.append(year)
                journals.append(journal)
#%%

df['journal'] = journals
df['year'] = years
df['page_num'] = pages
df['volume'] = volumes
df['issue'] = issues
df['titles'] = titles
df['authors'] = authors
df['abstract'] = abstracts
df['keywords'] = keywords
df['introduction'] = introductions
df['methods'] = methods
df['results'] = results
df['discussions'] = discussions
df['references'] = references
df.to_csv(f'../{journal}_{year}.csv')
df.to_excel(f'../{journal}_{year}.xlsx')


#page_num = r'\d{1, 3} -\d{1, 3}'
#year_with_comma = r'\d{4, 4},'
#%%
for root, dirs, files in os.walk('../txt_files'):
    for file in files:
        if file.endswith('.txt'):
            text_path = os.path.join(root, file)
            with open(text_path, 'r') as f:
                file_contents = f.read()
                file_names.append(file)
                method = text_gathering(
                    file_contents, 'METHOD', 'RESULTS')
                methods.append(method)
                result = text_gathering(
                    file_contents, "RESULTS", "DISCUSSION")
                results.append(result)
                discussion = text_gathering(
                    file_contents, "DISCUSSION", "REFERENCES")
                discussions.append(discussion)
                reference = text_references(file_contents, "REFERENCES")
                references.append(reference)
                years.append(year)
                journals.append(journal)
#%%


df['file_name'] = file_names
df['journal'] = journals
df['year'] = years
#df['page_num'] = pages
#df['volume'] = volumes
#df['issue'] = issues
#df['titles'] = titles
#df['authors'] = authors
#df['abstract'] = abstracts
#df['keywords'] = keywords
#df['introduction'] = introductions
df['methods'] = methods
df['results'] = results
df['discussions'] = discussions
df['references'] = references
df.to_csv(f'../{journal}_{year}_methods_results_discussion_references.csv')


df.to_excel(f"../{journal}_{year}_methods_results_discussion_references.xlsx", engine='xlsxwriter')
