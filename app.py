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
st.header("Leaves of grass; let 'em pass.")
# st.header("Leaves of grass;")
# st.header("let 'em pass.")

# words to disallow from being the final word
non_enders = ['the', 'a', 'as', 'or', 'but', 'and', 'nor']

# generate poem
tanka = tankanizer(whit_dict, non_enders=non_enders)

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
