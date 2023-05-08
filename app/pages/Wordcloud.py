import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
import nltk.corpus

# Header
st.title("Wordcloud of the most spoken words by a character")

def load_data():
    df = pd.read_csv("The_Office_lines.csv", index_col='id')
    df.drop(['scene'], axis = 1, inplace=True)
    df.rename({'line_text': 'line'}, axis=1, inplace=True)
    return(df)

df = load_data()

tokenizer = RegexpTokenizer(r'\w+')

with open('most_common_english_words.txt', 'r') as file:
    most_common = [i.strip('\n') for i in file.readlines()]

stopwords = set(nltk.corpus.stopwords.words('english'))

speakers = ('Michael',
            'Dwight',
            'Jim',
            'Pam',
            'Andy',
            'Kevin',
            'Angela',
            'Oscar',
            'Erin',
            'Ryan',
            'Darryl',
            'Phyllis',
            'Kelly',
            'Jan',
            'Toby',
            'Stanley',
            'Meredith',
            'Holly',
            'Nellie',
            'Creed')

def speaker_wordcloud(speaker):
    speaker_lines = df.loc[df['speaker'] == speaker, 'line']
    speaker_words = []
    for line in speaker_lines:
        words = tokenizer.tokenize(line)
        speaker_words.extend(words)

    speaker_words = [word.lower() for word in speaker_words]
    speaker_words = list(filter(lambda x: x not in most_common, speaker_words))
    speaker_words = list(filter(lambda x: x not in stopwords, speaker_words))
    speaker_words = list(filter(lambda x: len(x) > 2, speaker_words))
    
    #convert it to dictionary with values and its occurences
    word_could_dict = Counter(speaker_words)
    wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)

    fig = plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    return fig

speaker = st.selectbox(label="Select a Character", options=speakers)
ok = st.button("Generate WordCloud")

if ok == True:
    st.write(speaker_wordcloud(speaker))