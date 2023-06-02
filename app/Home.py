import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Header
st.title("An exploratory analysis of The Office (US)")

def load_data():
    df = pd.read_csv("data/dataset/The_Office_lines.csv", index_col='id')
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
lines_spoken_table = df.speaker.value_counts()[:20].reset_index(name="Lines spoken throughout the show")
st.table(lines_spoken_table)

fig = px.bar(lines_spoken, title='Lines spoken by popular characters', 
            labels=dict(index = "Speaker", value = "Dialogues spoken", variable=""))
st.write(fig)

# Dialogues per Season
season_dict = {'Michael': {1: 643,
  2: 2324,
  3: 1990,
  4: 1636,
  5: 2163,
  6: 1983,
  7: 1404,
  9: 2},
 'Dwight': {1: 326,
  2: 1114,
  3: 940,
  4: 547,
  5: 1075,
  6: 812,
  7: 703,
  8: 946,
  9: 1069},
 'Jim': {1: 285,
  2: 905,
  3: 783,
  4: 684,
  5: 875,
  6: 928,
  7: 687,
  8: 869,
  9: 798},
 'Pam': {1: 219,
  2: 729,
  3: 665,
  4: 528,
  5: 706,
  6: 706,
  7: 612,
  8: 475,
  9: 735},
 'Andy': {3: 391, 4: 223, 5: 497, 6: 538, 7: 557, 8: 1125, 9: 638},
 'Kevin': {1: 30,
  2: 157,
  3: 212,
  4: 141,
  5: 187,
  6: 228,
  7: 240,
  8: 247,
  9: 267},
 'Angela': {1: 32,
  2: 162,
  3: 243,
  4: 193,
  5: 221,
  6: 136,
  7: 161,
  8: 166,
  9: 381},
 'Oscar': {1: 58,
  2: 130,
  3: 72,
  4: 111,
  5: 216,
  6: 177,
  7: 197,
  8: 235,
  9: 295},
 'Erin': {5: 53, 6: 298, 7: 311, 8: 427, 9: 380},
 'Ryan': {1: 52,
  2: 227,
  3: 197,
  4: 228,
  5: 169,
  6: 125,
  7: 176,
  8: 189,
  9: 16},
 'Darryl': {1: 17,
  2: 76,
  3: 89,
  4: 59,
  5: 102,
  6: 100,
  7: 248,
  8: 312,
  9: 278},
 'Phyllis': {1: 11,
  2: 134,
  3: 112,
  4: 99,
  5: 180,
  6: 138,
  7: 147,
  8: 123,
  9: 127},
 'Kelly': {1: 4, 2: 115, 3: 176, 4: 95, 5: 156, 6: 120, 7: 153, 8: 123, 9: 14},
 'Jan': {1: 38, 2: 285, 3: 298, 4: 214, 5: 64, 7: 17, 9: 33},
 'Toby': {1: 23, 2: 148, 3: 122, 4: 144, 5: 71, 6: 100, 7: 97, 8: 106, 9: 125},
 'Stanley': {1: 27, 2: 108, 3: 94, 4: 81, 5: 113, 6: 72, 7: 75, 8: 91, 9: 100},
 'Meredith': {1: 18, 2: 41, 3: 60, 4: 62, 5: 115, 6: 82, 7: 70, 8: 83, 9: 114},
 'Holly': {4: 74, 5: 270, 7: 265},
 'Nellie': {7: 9, 8: 233, 9: 287},
 'Creed': {2: 77, 3: 71, 4: 67, 5: 52, 6: 38, 7: 66, 8: 33, 9: 52}}

plot_df = pd.DataFrame.from_dict(season_dict)
plot_df = plot_df.reindex([i for i in range(1, 10)])

st.header("Average dialogues per episode")

dialogues_per_season = plot_df.sum(axis=1)
dialogues_per_season = np.asarray(dialogues_per_season)

episodes_per_season = [6, 22, 25, 19, 28, 26, 26, 24, 25]

dialogues_per_episode_per_season = dialogues_per_season//episodes_per_season

fig = px.bar(y=dialogues_per_episode_per_season, x=[i for i in range(1, 10)], 
             labels={'x':'Season', 'y':'Dialogues per episode'})
st.write(fig)

st.header("Dialogues spoken by characters broken down by seasons")

st.dataframe(plot_df)

fig = make_subplots(rows=5, cols=4, subplot_titles=('Michael', 'Dwight', 'Jim', 'Pam', 'Andy', 'Kevin', 'Angela', 
                                                    'Oscar', 'Erin', 'Ryan', 'Darryl', 'Phyllis', 'Kelly', 'Jan', 
                                                    'Toby', 'Stanley', 'Meredith', 'Holly', 'Nellie', 'Creed'))

fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Michael),
    row=1, col=1,
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Dwight),
    row=1, col=2
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Jim),
    row=1, col=3
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Pam),
    row=1, col=4
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Andy),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Kevin),
    row=2, col=2
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Angela),
    row=2, col=3
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Oscar),
    row=2, col=4
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Erin),
    row=3, col=1
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Ryan),
    row=3, col=2
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Darryl),
    row=3, col=3
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Phyllis),
    row=3, col=4
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Kelly),
    row=4, col=1
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Jan),
    row=4, col=2
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Toby),
    row=4, col=3
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Stanley),
    row=4, col=4
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Meredith),
    row=5, col=1
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Holly),
    row=5, col=2
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Nellie),
    row=5, col=3
)
fig.add_trace(
    go.Scatter(x=plot_df.index, y=plot_df.Creed),
    row=5, col=4
)
fig.update_layout(height=800, width=900, showlegend=False)

st.write(fig)

def speaker_dialogue_pie(season:int):
    fig = px.pie(values=plot_df.iloc[season-1], names=plot_df.columns, title=f"Dialogues for season {season}", 
                 hover_name=plot_df.columns)
    return fig

season = st.slider(label="Select a season", min_value=1, max_value=9)

ok = st.button("Select")
if ok == True:
    st.write(speaker_dialogue_pie(season))