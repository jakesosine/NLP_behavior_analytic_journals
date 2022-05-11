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
    
def box_strip_plot(df,figsize,xlabel,ymin,ymax,title,ylabel,fpath,xmin,xmax):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=figsize)
    ax = sns.boxplot(y='journals',x='word_count',data=df)
    ax = sns.stripplot(y="journals", x="word_count",hue='years', size=2,data=df,jitter=.2)
    ax.get_legend().remove()

    plt.xlabel(xlabel,fontsize=30,labelpad=(16))
    plt.xticks(fontsize=20,rotation=60)
    plt.yticks(fontsize=20,rotation=0)
    positions = (0,1, 2, 3,4,5)
    labels = ("Journal of the Experimental \n Analysis of Behavior", "The Behavior Analyst", "Behavior Analysis \n in Practice",'Analysis of \n Verbal Behavior','Journal of Applied \n Behavior Analysis','Health Service Research')
    plt.yticks(positions, labels)
    plt.ylabel(ylabel,fontsize=35,labelpad=(16))

    plt.xlabel(xlabel,fontsize=35,labelpad=(16))
    plt.ylim(ymin,ymax)
    plt.xlim(xmin,xmax)
    plt.title(title,fontsize=24,pad=60)
    right_side=ax.spines['right']
    right_side.set_visible(False)
    top = ax.spines['top']
    top.set_visible(False)
    plt.tight_layout()
    plt.savefig(fpath)


def scatter(figsize,xlabel,ymin,ymax,title,ylabel,fpath):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=figsize)
    ax = sns.scatterplot(data=df, x="years", y="word_count", hue="journals")
    plt.xlabel(xlabel,fontsize=30,labelpad=(16))
    plt.yticks(fontsize=20,rotation=0)
    plt.xticks(fontsize=30,rotation=60)
    plt.ylabel(ylabel,fontsize=30,labelpad=(16))
    plt.ylim(ymin,ymax)
    plt.title(title,fontsize=24,pad=60)
    right_side=ax.spines['right']
    right_side.set_visible(False)
    top = ax.spines['top']
    top.set_visible(False)
    plt.tight_layout()
    plt.savefig(fpath)
    
def box_strip_plot_(df, figsize,xlabel,title,ylabel,fpath,ymin,ymax):
    from matplotlib import rcParams
    import matplotlib.pyplot as plt 
    import seaborn as sns
    rcParams['font.family'] = 'arial'
    fig, ax = plt.subplots(figsize=figsize)#,dpi=1200)
    ax = sns.boxplot(x='years',y='word_count',data=df,color='White',showfliers=False)
    ax = sns.stripplot(x="years", y="word_count",hue='replaced', size=4,data=df,edgecolor='black',palette=sns.color_palette("colorblind"))

    plt.xlabel(xlabel,fontsize=30,labelpad=(16))
    plt.xticks(fontsize=20,rotation=60)
    plt.yticks(fontsize=20,rotation=0)
    positions = (0,1, 2, 3,4,5)
    #labels = ("Journal of the Experimental \n Analysis of Behavior", "The Behavior Analyst", "Behavior Analysis \n in Practice",'Analysis of \n Verbal Behavior','Journal of Applied \n Behavior Analysis','Health Service Research')
   #plt.yticks(positions, labels)
    plt.ylabel(ylabel,fontsize=35,labelpad=(16))

    plt.xlabel(xlabel,fontsize=35,labelpad=(16))
    plt.ylim(ymin,ymax)
    plt.title(title,fontsize=24,pad=60)
    right_side=ax.spines['right']
    right_side.set_visible(False)
    top = ax.spines['top']
    top.set_visible(False)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles[1:], labels=labels[1:])
    plt.legend(frameon=False,fontsize=14)
    plt.tight_layout()
    plt.savefig(fpath)
    
def box_strip_plot_(df, figsize,xlabel,title,ylabel,fpath,ymin,ymax):
    from matplotlib import rcParams
    from matplotlib import rcParams
    import matplotlib.pyplot as plt 
    import seaborn as sns
    rcParams['font.family'] = 'arial'
    fig, ax = plt.subplots(figsize=figsize)#,dpi=1200)
    ax = sns.boxplot(x='years',y='word_count',data=df,color='White',showfliers=False)
    ax = sns.stripplot(x="years", y="word_count",hue='replaced', size=4,data=df,edgecolor='black',palette=sns.color_palette("colorblind"))

    plt.xlabel(xlabel,fontsize=30,labelpad=(16))
    plt.xticks(fontsize=20,rotation=60)
    plt.yticks(fontsize=20,rotation=0)
    positions = (0,1, 2, 3,4,5)
    #labels = ("Journal of the Experimental \n Analysis of Behavior", "The Behavior Analyst", "Behavior Analysis \n in Practice",'Analysis of \n Verbal Behavior','Journal of Applied \n Behavior Analysis','Health Service Research')
   #plt.yticks(positions, labels)
    plt.ylabel(ylabel,fontsize=35,labelpad=(16))

    plt.xlabel(xlabel,fontsize=35,labelpad=(16))
    plt.ylim(ymin,ymax)
    plt.title(title,fontsize=24,pad=60)
    right_side=ax.spines['right']
    right_side.set_visible(False)
    top = ax.spines['top']
    top.set_visible(False)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles[1:], labels=labels[1:])
    plt.legend(frameon=False,fontsize=14)
    plt.tight_layout()
    plt.savefig(fpath)

    
    
    
if __name__ == '__main__':
    barplot(data=jeab_top_25,
            figsize=(20,12),
            xlabel='Count',
            title="Journal of the Experimental Analysis\nof Behavior",
            ylabel='Bigrams',
            fpath='drive/MyDrive/jaba_nlp/jeab_bigrams.png')
