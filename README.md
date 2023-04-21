# "That's what she said!" - The Office Script Analysis
### Luuk Boekestein, Shantanu Motiani and Eline Westerbeek, 

---

## Abstract

---

In this project, we aim to analyze the scripts of the hit TV show ‘The Office’. We will be using a dataset from Kaggle, which contains the season, episode, scene, line of dialogue, the speaker  and whether the scene was deleted or not. Our goals include training a model to predict which character is the speaker, exploring interactions between characters, performing a sentiment analysis and doing topic modelling. Through this, we want to determine if there are certain topics that certain characters tend to talk about (which we can express using word clouds) and identify the main topics of different episodes/seasons. We think this is interesting because these characters are so iconic, and we want to explore whether we can find out what sets them apart and makes them unique. All three of us are big Office fans, so extracting underlying patterns in these scripts is really interesting to us!

## Research Questions

---

- Can we predict which character in the Office says which line of dialogue?
- What are the interactions between characters throughout the seasons?
- Sentiment analysis – What are the sentiments expressed in the dialogues, and how do they vary per character and season?
- Topic modelling – Are there certain topics that certain characters tend to talk about? And can we identify the primary topics of an episode? (We want to create word clouds to visualize this)
- *Possible extra*: generate quote from each character

## Dataset

---

For this project, we used a dataset that we found on Kaggle.com, containing all the scripts of the American TV series "The Office". It contains the season, episode, scene, line of dialogue, the speaker  and whether the scene was deleted or not. The dataset can be found [here](https://www.kaggle.com/datasets/lillitarhea/the-office-script-lines).

To process, we will employ various preprocessing techniques discussed throughout the course, such as dealing with punctuation, stopwords, lowercasing, tokenization, lemmatization, etc. The data size is sufficiently big, containing almost 60,000 rows (lines), with 7 columns indicating season, episode, scene, speaker, line, deleted and episode name. The dataset is in a .csv format.

A simple overview of the dataset using `ProfileReport` from `ydata_profiling` can be found in the [data_report.html](data_report.html) file.

## Milestones

---

### Planning

| Date | Milestone goal | Formal deadlines |
| --- | --- | --- |
| 19/04 | Finish and submit a project proposal | Project proposal due | 
25/04 | Submit project update 1 | Project update 1 due
| 09/05 | Submit project update 2| Project update 2 due
| 30/05 | Submit final project | Final project due

### Goals Project update 1

TODO:
- **Annotating dataset** Each manually annotate 100 lines of dialogue for sentiment analysis
    - Make sample [Luuk]
- **Preprocessing** Finding most effective pre-processing pipeline for sentiment analysis [Luuk]
- **Visualizations** Basic visualizations and analyis of the data [Shantanu]
- **Topic modeling** Start exploring topic modeling [Eline]


### Goals Project update 2 (To be specified)

- Sentiment analysis
    - lexicon-based
    - ML-based
- Topic modelling
    - general
    - per character 
    - per episode
    - Wordclouds


## Documentation

---

- *TBA* 