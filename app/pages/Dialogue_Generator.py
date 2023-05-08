import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from collections import Counter
from nltk.tokenize import word_tokenize
import nltk.corpus
import markovify
import streamlit as st

# Header
st.title("Dialogue Generator using Markov Chains")

def load_data():
    df = pd.read_csv("The_Office_lines.csv", index_col='id')
    df.drop(['scene'], axis = 1, inplace=True)
    df.rename({'line_text': 'line'}, axis=1, inplace=True)
    return(df)

df = load_data()

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

# Defining the function
def dialogue_generator(speaker):
    # Get raw text as string.
    with open(f"./character_lines/{speaker}_lines.txt", "r") as f:
        text = f.read()

    # Build the model.
    markov_model = markovify.NewlineText(text)
    
    return(markov_model.make_sentence(max_overlap_ratio=0.4))

# Taking user input
speaker = st.selectbox(label="Select a Character", options=speakers)
ok = st.button("Generate Dialogue")

# Generating dialogue
if ok == True:
    st.write(dialogue_generator(speaker))