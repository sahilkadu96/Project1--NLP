# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 14:31:27 2022

@author: Sahil
"""

import streamlit as st
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\Sahil\.spyder-py3\Finer_aspect_v2.xlsx')

st.title('AI for soft skills')

st.header('Soft skill search')

skills_list = df['Skills category'].unique()

skill = st.selectbox('Skills', skills_list)

for i in range(len(skills_list)):
    if skill == skills_list[i] :
        sub_skills_list = df[df['Skills category'] == skill]['Skills sub-category'].unique()
        sub_skill = st.selectbox('Sub skills', sub_skills_list)
    
        for j in range(len(sub_skills_list)):
            if sub_skill == sub_skills_list[j]:
                finer_aspects_list = df[df['Skills sub-category'] == sub_skill]['Finer aspects'].unique()
                finer_aspect = st.selectbox('Finer aspects', finer_aspects_list)
                
                for k in range(len(finer_aspects_list)):
                    if finer_aspect == finer_aspects_list[k]:
                        paragraphs = df[df['Finer aspects'] == finer_aspect]['Content'].values
                        
                        for l in range(len(paragraphs)):
                            st.write(paragraphs[l])
                            
                        words = []
                        stopwords = set(STOPWORDS)
                        
                        for para in paragraphs:
                            tokens = para.split()
                           
                            
                            for i in range(len(tokens)):
                                if tokens[i].lower() not in stopwords:
                                    words.append(tokens[i].lower())
                                    
                        stri = ''
                        for i in words:
                            stri += i + ' '
                            
                        wordcloud = WordCloud(width = 800, height = 800,
                                              background_color ='white',
                                              stopwords = stopwords,
                                              min_font_size = 10).generate(stri)
                        
                        plt.figure(figsize = (8, 8), facecolor = None)
                        plt.imshow(wordcloud)
                        st.set_option('deprecation.showPyplotGlobalUse', False)
                        st.pyplot()
                            
                            
                            
