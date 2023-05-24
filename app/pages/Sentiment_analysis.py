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
    "All",
)

seasons = (1, 2, 3, 4, 5, 6, 7, 8, 9, "All",)


def sentiment_character(character, season):
    # load sentiment data
    
    df = load_data()

    df["sentiment"] = df["BERT_uncased_sentiment"].round(2)
    df = df.loc[df["speaker"].isin(speakers)]
    # select all seasons
    if season == "All":
        if character == "All":
            # calculate mean per character per season
            df = df.groupby(["season", "speaker"], as_index=False).mean()
            df.reset_index(inplace=True)
            fig = px.line(
                df,
                x="season",
                y="sentiment",
                color="speaker",
                title="Sentiment analysis",
            )
        else:
            df = df.loc[df["speaker"] == character]
            df = df.groupby(["season", "speaker"], as_index=False).mean()
            df.reset_index(inplace=True)
            fig = px.line(
                df,
                x="season",
                y="sentiment",
                color="speaker",
                title="Sentiment analysis",
            )
    # select only selected season
    else:
        df = df.loc[df["season"] == season]
        if character == "All":
            df.reset_index(inplace=True)
            df = df.groupby(["episode", "speaker"], as_index=False).mean()
            fig = px.line(
                df,
                x="episode",
                y="sentiment",
                color="speaker",
                title="Sentiment analysis",
            )
        # select only lines from selected character
        else:
            df = df.loc[df["speaker"] == character]
            df = df.groupby(["episode", "speaker"], as_index=False).mean()
            fig = px.line(
                df,
                x="episode",
                y="sentiment",
                color="speaker",
                title="Sentiment analysis (Negative = -1, Neutral = 0, Positive = 1)",
            )
    st.plotly_chart(fig)


character = st.selectbox(label="Select a character", options=speakers)
season = st.selectbox(label="Select a season", options=seasons)

ok = st.button("View sentiment analysis")

if ok == True:
    sentiment_character(character, season)
