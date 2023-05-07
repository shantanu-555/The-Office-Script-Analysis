import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from collections import Counter
from nltk.tokenize import word_tokenize
import nltk.corpus

# Header
st.title("An exploratory analysis of The Office (US)")

def load_data():
    df = pd.read_csv("The_Office_lines.csv", index_col='id')
    df.drop(['scene'], axis = 1, inplace=True)
    df.rename({'line_text': 'line'}, axis=1, inplace=True)
    return(df)

df = load_data()

# Show data
st.header("The data")
st.dataframe(df)

# Lines spoken
lines_spoken = df.speaker.value_counts()[:20]
st.header("Number of Dialogues spoken by major characters throughout the show")
st.table(lines_spoken)

fig = px.bar(lines_spoken, title='Lines spoken by popular characters', 
            labels=dict(index = "Speaker", value = "Dialogues spoken", variable=""))
st.write(fig)