import streamlit as st
import pandas as pd

st.title('🤖Machine Learning App')

st.info('This app builds a machine learning model!')
with st.expander('Data'): # Dropdown for data below
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/da9653dfdb975b7342fa3a1a3b74375e35a9c1e5/penguins_cleaned.csv')
  df

  st.write('**X**')
  X = df.drop('species', axis=1) # exclude species column
  X

  st.write('**y**')
  y = df.species
  y
with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')
