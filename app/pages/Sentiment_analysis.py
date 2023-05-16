import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Sentiment analysis of The Office (US)")


def load_data():
    # find absolute path to csv file
    print(os.path.abspath(os.curdir))
    csv_file_path = (
        os.path.abspath(os.curdir) + "/sentiment_analysis/Sentiment_labeled_data.csv"
    )
    print(csv_file_path)
    df = pd.read_csv(csv_file_path, index_col="id")
    df.drop(["scene"], axis=1, inplace=True)
    return df

speakers = (
    "All",
    "Michael",
    "Dwight",
    "Jim",
    "Pam",
    "Andy",
    "Kevin",
    "Angela",
    "Oscar",
    "Erin",
    "Ryan",
    "Darryl",
    "Phyllis",
    "Kelly",
    "Jan",
    "Toby",
    "Stanley",
    "Meredith",
    "Holly",
    "Nellie",
    "Creed",
)


def sentiment_character(character):
    df = load_data()
    if not character == "All":
        df = df.loc[df["speaker"] == character]
    df = df.groupby(["season", "episode"]).mean()
    df.reset_index(inplace=True)
    df["sentiment"] = df["BERT_uncased_sentiment"].round(2)
    fig = px.line(
        df, x="episode", y="sentiment", color="season", title="Sentiment analysis"
    )
    st.plotly_chart(fig)


character = st.selectbox(label="Select a character", options=speakers)

ok = st.button("View sentiment analysis")

if ok == True:
    sentiment_character(character)
