import re
import pandas as pd
import os


year = '2016'
journal = 'Journal of the Experimental Analysis of Behavior'

def context(opened_file,start_identifier,end_):
    start = opened_file.find(start_identifier)
    return opened_file[start:end_]


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
#%%
for root, dirs, files in os.walk('../txt_files'):
    for file in files:
        if file.endswith('.txt'):
            text_path = os.path.join(root, file)
            with open(text_path, 'r') as f:
                quick_review = input('enter Yes or No if you modified variables: ')
                quick_reviews.append(quick_review)
                file_contents = f.read()
                years.append(year)
                journals.append(journal)
                print(file_contents[:2000])
                page = input('Enter Page Number: ')
                pages.append(page)
                volume = input('enter volume: ')
                volumes.append(volume)
                issue = input('enter issue: ')
                issues.append(issue)
                title = input('enter a title: ')
                titles.append(title)
                author = input('enter authors: ')
                authors.append(author)
                abstract = input('Enter Abstract:')
                abstracts.append(abstract)
                keyword = input('enter keywords: ')
                keywords.append(keyword)
                introduction = text_gathering(file_contents, input(
                    "Enter two starting words: "), 'Method')
                introductions.append(introduction)
                method = text_gathering(
                    file_contents, 'Method', 'Results')
                methods.append(method)
                result = text_gathering(
                    file_contents, "Results", "Discussion")
                results.append(result)
                discussion = text_gathering(
                    file_contents, "Discussion", "References")
                discussions.append(discussion)
                reference = text_references(file_contents, "References")
                references.append(reference)

                
                
#%%      
df['journal'] = journals
df['year'] = years
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

#%%
df.to_csv(f'../{journal}_{year}.csv')



#page_num = r'\d{1, 3} -\d{1, 3}'
#year_with_comma = r'\d{4, 4},'
