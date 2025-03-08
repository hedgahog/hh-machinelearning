import streamlit as st
import pandas as pd
import numpy as np

st.title("EvoBeevos Variant Predictor 🐝")
st.write('About: VarEffectAI is a comprehensive Variant Effect Predictor
that leverages the Evo 2 AI model to predict genetic variant effects.
It compares these predictions with ClinVar/dbSNP data, offering users a 
thorough analysis of variant significance. The app features a Streamlit interface,
API integrations, a lightweight database for caching results, and an AI chatbot for user assistance.')

# Display result and score on main page
# Display CliVar comparison on main page as well?
# User info will be on main page
# Where to put chatbot?
# What kind of input do we want the user to put in (i.e DNA sequences? Should we cap how long the sequence can be?)
# Input will be chromosome location from ucsc style
# focus on human genome
# type variation in evo and it tells you health effect, include information from clivar
