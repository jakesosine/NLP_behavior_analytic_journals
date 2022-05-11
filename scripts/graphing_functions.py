#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 20:16:57 2022

@author: jacobsosine
"""

def barplot(data,figsize,xlabel,title,ylabel,fpath):
    import matplotlib.pyplot as plt
    import seaborn as sns
    fig, ax = plt.subplots(figsize=figsize)
    ax = sns.barplot(x='count', y="bigrams", data=data,color='black')
    
    plt.xlabel(xlabel,fontsize=30,labelpad=(16))
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.ylabel(ylabel,fontsize=30,labelpad=(16))
    plt.title(title,fontsize=24,pad=60)
    right_side=ax.spines['right']
    right_side.set_visible(False)
    top = ax.spines['top']
    top.set_visible(False)
    plt.tight_layout()
    plt.savefig(fpath)
    
    
    
if __name__ == '__main__':
    barplot(data=jeab_top_25,
            figsize=(20,12),
            xlabel='Count',
            title="Journal of the Experimental Analysis\nof Behavior",
            ylabel='Bigrams',
            fpath='drive/MyDrive/jaba_nlp/jeab_bigrams.png')