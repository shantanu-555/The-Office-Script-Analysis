# "That's what she said!" - The Office Script Analysis
### by Luuk Boekestein, Shantanu Motiani and Eline Westerbeek

## Quick links

- [Report](Final_report.pdf)
- [Code](src/)
- [Data](data/dataset/)
- [Webapp](app/)
- [Slides](docs/slides.pdf)

---

## Abstract

This project presents a comprehensive analysis of the character dialogue in the popular US TV show "The Office." Through the application of sentiment analysis and topic modelling on the lines in the show, and the development of a dialogue generator using Markov chains, we aim to uncover insights into the differences in emotional undertones, character interactions and patterns of the show’s dialogue. The sentiment analysis revealed the diverse range of emotions expressed by the characters, providing a nuanced understanding of their changing interactions. The topic modelling identified recurring themes and topics within the dialogue, shedding light on the show's narrative structures. Finally, the dialogue generator utilized Markov chains to mimic the unique speech patterns of the characters, allowing us to generate simplistic new dialogues. This project offers a valuable contribution to the analysis of "The Office," showcasing the potential of computational techniques in analysing character dialogue in TV shows.

## Research Questions

- What are the interactions between characters throughout the seasons?
- Sentiment analysis – What are the sentiments expressed in the dialogues, and how do they vary per character and season?
- Topic modelling – Are there certain topics that certain characters tend to talk about? And can we identify the primary topics of an episode?
- Dialogue generation: generate quote from each character

## Dataset

For this project, we used a dataset that we found on Kaggle.com, containing all the scripts of the American TV series "The Office". It contains the season, episode, scene, line of dialogue, the speaker  and whether the scene was deleted or not. The dataset contains almost 60,000 rows (lines), with 7 columns indicating season, episode, scene, speaker, line, deleted and episode name. The dataset is in a .csv format.
 The dataset can be found online [here](https://www.kaggle.com/datasets/lillitarhea/the-office-script-lines), or can be retreived from the [data/dataset](data/dataset/) folder.


A simple overview of the dataset using `ProfileReport` from `ydata_profiling` can be found in the [data_report.html](src/vizualizations/data_report.html) file.

## Documentation

### Report

A detailed report of the project can be found [here](Final_report.pdf). The 4-page report contains a detailed description of the project, the research questions, the methods used, the results, conclusions and references.

### Code

The main code used for this project can be found in the [src](src/) folder. Within the `src` folder there is a subfolder for each adressed research question: 
- the code for vizualizing the data can be found in the notebook in the [vizualizations](src/vizualizations) folder,
- the code for the sentiment analysis can be found in the notebook in the [sentiment analysis](src/sentiment_analysis) folder,
- and the code for the topic modelling can be found in the notebook in the [topic modeling](src/topic%20modelling/) folder

Furthermore, the code used to generate readability scores for each character is located in the [gunning fog](src/gunning%20fog/) folder.

The packages needed to run the code in this project (including the webapp) can be found in the [requirements.txt](requirements.txt) file. To install these packages, run the following command in your terminal:

    pip install -r requirements.txt

### Webapp

To enable an easy exploration of our results, we created a simple webapp using the `streamlit` package. To run the webapp, run the following command in your terminal:

    streamlit run .\app\Home.py

The code used to create the webapp can be found in the [app](/app/) folder.

### Further documentation

The project updates and initial project plan can be found in the [docs](docs/) folder. Furthermore, the slides that we used for the final presentation can be found in the [slides](docs/slides.pdf) pdf.