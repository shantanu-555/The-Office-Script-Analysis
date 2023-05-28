import streamlit as st
import pandas as pd
import plotly.express as px
import os

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