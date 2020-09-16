# app building library
import streamlit as st

# # custom functions
from functions import *

# necessary libraries
import json
import random
import pronouncing as pr


# load markov dictionary
with open('data/whitman_dictionary.json', 'r') as hello:
    whit_dict = json.load(hello)

    
# message from the recommender-bot
st.title('Greetings from the whitman_tankanizer.')
st.header('Leaves of grass; let them pass.')
# st.subheader()

tanka = tankanizer(whit_dict)

# format blank space
st.markdown('')
# format blank space
st.markdown('')

if st.button('TO WHIT!'):
    # format blank space
    st.markdown('')
    # format blank space
    st.markdown('')

    st.text(tanka)