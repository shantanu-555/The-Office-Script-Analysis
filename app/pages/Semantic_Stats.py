import textstat as txs
import streamlit as st

def dialogue_stats(character):
    with open(f'data/character_lines/{character}_lines.txt', 'r') as file:
        text = file.readlines()
    length = len(text)
    
    def gunning_fog():
        gf_score_total = 0
        for i in text:
            temp = txs.gunning_fog(i)
            gf_score_total += temp
        gf_score = gf_score_total/length
        st.write(f"Gunning Fog index score = {round(gf_score, 1)} (School grade required to comprehend)")
    
    def automated_readablity():
        ar_score_total = 0
        for i in text:
            temp = txs.automated_readability_index(i)
            ar_score_total += temp
        ar_score = ar_score_total/length
        st.write(f"Automated Readability score = {round(ar_score, 1)} (School grade required to comprehend)")
        
    def dc_readablity():
        dc_score_total = 0
        for i in text:
            temp = txs.dale_chall_readability_score(i)
            dc_score_total += temp
        dc_score = dc_score_total/length
        st.write(f"Dale–Chall Readability score = {round(dc_score, 1)} (School grade required to comprehend)")
        
    def reading_time():
        time_total = 0
        for i in text:
            temp = txs.reading_time(i, ms_per_char=14.69)
            time_total += temp
        time = time_total/length
        st.write(f"Average Reading time for dialogues = {round(time, 2)} (in minutes)")
        
    def syllable_count():
        syllable_total = 0
        for i in text:
            temp = txs.syllable_count(i)
            syllable_total += temp
        average_syllables = syllable_total/length
        st.write(f"Average syllables in dialogues = {int(round(average_syllables, 0))}")
        
    def polysyllable_percent():
        poly_total = 0
        words_total = 0
        for i in text:
            temp = txs.polysyllabcount(i)
            poly_total += temp
            words_total += len(i)
        poly_percent = poly_total/words_total
        st.write(f"Percentage of poly-syllable words in dialogues = {round(poly_percent, 1)}% (words with 3 or more syllables)")
        
    def monosyllable_percent():
        mono_total = 0
        words_total = 0
        for i in text:
            temp = txs.monosyllabcount(i)
            mono_total += temp
            words_total += len(i)
        mono_percent = mono_total/words_total
        st.write(f"Percentage of mno-syllable words in dialogues = {round(mono_percent, 1)}% (words with 1 syllable)")
    
    st.subheader(f"Statistics for {character}'s dialogues:\n____________________________________________")
    
    gunning_fog()
    automated_readablity()
    
    st.write("____________________________________________")
    
    syllable_count()
    monosyllable_percent()
    # polysyllable_percent()

st.header("Semantic Statistics for character")

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

speaker = st.selectbox(label="Select a Character", options=speakers)
ok = st.button("Generate Dialogue Statistics")

if ok == True:
    dialogue_stats(speaker)