import streamlit as st
import pandas as pd
import plotly.express as px
import os
from wordcloud import WordCloud
from nltk.tokenize import RegexpTokenizer
import nltk.corpus
from collections import Counter
import matplotlib.pyplot as plt

st.title("Topic Modelling of The Office (US)")

st.header("Topics:")

st.write("0: general dialogue")
st.write("1: phone calls")
st.write("2: the office")
st.write("3: the company and business")
st.write("4: parties and party planning")
st.write("5: apologising")
st.write("6: humour and jokes")
st.write("7: roles/positions in the company")
st.write("8: friendships and relationships")

def load_data():
    # find absolute path to csv file
    print(os.path.abspath(os.curdir))
    csv_file_path = (
        os.path.abspath(os.curdir) + "/topics_by_scene.csv"
    )
    print(csv_file_path)
    df = pd.read_csv(csv_file_path)
    return df
df = load_data()

topics = [0, 1, 2, 3, 4, 5, 6, 7, 8, "All"]
topics_lala = [0, 1, 2, 3, 4, 5, 6, 7, 8,]


def show_topics(selected_topic):
    df = load_data()
    if selected_topic == "All":
        topic_counts = df.groupby(['nmf_topic', pd.Grouper(key='season')]).size().reset_index(name='count')
        total_counts = topic_counts.groupby('season')['count'].transform('sum')
        topic_counts['proportion'] = topic_counts['count'] / total_counts
        reshaped_data = topic_counts.pivot(index='season', columns='nmf_topic', values='proportion')
        fig = px.line(
            reshaped_data,
            x=reshaped_data.index,
            y=reshaped_data.columns,
            title="Topic Modelling",
        )
        fig.update_layout(
            xaxis_title='Season',
            yaxis_title='Proportion',
            legend_title='NMF Topics',
        )
        st.plotly_chart(fig)
    else:
        topic_counts = df.groupby(['nmf_topic', pd.Grouper(key='season')]).size().reset_index(name='count')
        total_counts = topic_counts.groupby('season')['count'].transform('sum')
        topic_counts['proportion'] = topic_counts['count'] / total_counts
        topic_counts = topic_counts.drop(topic_counts[topic_counts["nmf_topic"] != selected_topic].index)
        reshaped_data = topic_counts.pivot(index='season', columns='nmf_topic', values='proportion')
        fig = px.line(
            reshaped_data,
            x=reshaped_data.index,
            y=reshaped_data.columns,
            title="Topic Modelling",
        )
        fig.update_layout(
            xaxis_title='Season',
            yaxis_title='Proportion',
            legend_title='NMF Topics',
        )
        st.plotly_chart(fig)
            

selected_topic = st.selectbox(label="Select a topic", options=topics)
ok = st.button("Generate topics over the seasons")


if ok == True:
    show_topics(selected_topic)
    
st.title("Wordclouds per topic")

tokenizer = RegexpTokenizer(r'\w+')

with open('most_common_english_words.txt', 'r') as file:
    most_common = [i.strip('\n') for i in file.readlines()]

stopwords = set(nltk.corpus.stopwords.words('english'))

def topic_wordcloud(selected_topic_lala):
    topic_lines = df.loc[df['nmf_topic'] == selected_topic_lala, 'line_text_pp']
    topic_words = []
    for line in topic_lines:
        if isinstance(line, str):
            words = tokenizer.tokenize(line)
            topic_words.extend(words)

    topic_words = [word.lower() for word in topic_words]
    topic_words = list(filter(lambda x: x not in most_common, topic_words))
    topic_words = list(filter(lambda x: x not in stopwords, topic_words))
    topic_words = list(filter(lambda x: len(x) > 2, topic_words))
    
    #convert it to dictionary with values and its occurences
    word_could_dict = Counter(topic_words)
    wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)

    fig = plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    return fig

selected_topic_lala = st.selectbox(label="Select a topic", options=topics_lala)
lala = st.button("Generate WordCloud")

if lala == True:
    st.write(topic_wordcloud(selected_topic_lala))
