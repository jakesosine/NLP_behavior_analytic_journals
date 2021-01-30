#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:27:39 2021

@author: jacobsosine
"""

from PyPDF2 import PdfFileReader
import os
import pandas as pd 
import re

df = pd.DataFrame()



def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        return info, number_of_pages
journal_title = 'Journal of Applied Behavior Analysis'
journal_year = '2018'
#%%


authors = []
creators =  []
subjects = []
titles = []
number_of_pages = []
file_name = []
page_ranges = []
issues = []
journal_titles = []
years = []
dois = []
for root, dirs, files in os.walk('../articles'):
    for file in files:
        if file.endswith('.pdf'):
            file_name.append(file)
            file_path = os.path.join(root, file)
            info, number_of_page = get_info(file_path)
            author_ = info.author
            creator = info.creator
            producer = info.producer
            subject = info.subject
            pattern0 = re.compile(r'[0-9]+:')
            matches0 = pattern0.finditer(subject)
            for match in matches0:
                issues.append(match.group(0))
            pattern1 = re.compile(r'[0-9]+-[0-9]+')
            matches1 = pattern1.finditer(subject)
            for match in matches1:
                page_ranges.append(match.group(0))
            journal_titles.append(journal_title)
            pattern3 = re.compile(r'[0-9][0-9][0-9][0-9]')
            matches3 = pattern3.finditer(subject)
            for match in matches3:
                years.append(match.group(0))
            subjects.append(subject)
            title = info.title
            titles.append(title)
            authors.append(author_)
            creators.append(creator)
            number_of_pages.append(number_of_page)
            print(info.items())
            lst =(list(info.items()))
            dois.append(lst[-1])
            years.append(journal_year)

#%%
df['file_name'] = file_name
df['page_num'] = number_of_pages
df['page_ranges']= page_ranges
#df['authors'] = authors
#df['creators'] = creators
#df['subjects'] = subjects
df['titles'] = titles
df['issues'] = issues
df['journal'] = journal_titles
df['years'] = years
df['doi'] = dois

#%%

df.to_csv(f'../{journal_title}_{journal_year}_metadata.csv')
df.to_excel(f'../{journal_title}_{journal_year}_metadata.xlsx')
                
#%%

string = 'Journal of the Experimental Analysis of Behavior 2019.112:47-59'






#%%
if __name__ == '__main__':
    path = '../articles/40616_2018_Article_94.pdf'
    info, page =get_info(path)
    print(info)
    