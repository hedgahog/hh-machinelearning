import streamlit as st
import pandas as pd

st.title('🤖Machine Learning App')

st.write('This app builds a machine learning model!')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/da9653dfdb975b7342fa3a1a3b74375e35a9c1e5/penguins_cleaned.csv')
df
