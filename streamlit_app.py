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
# Scatter plot for data
with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# Data preparatios
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)  
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5,17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass(g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender', ('Male', 'Female'))
# create dataframe for input features
  data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': gender}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, X], axis=0)
with st.expander('Input features'):
  st.write('**Input penguin**')
  input_df
  st.write('**Combined penguin data**')
  input_penguins
        
# Encode
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
df_penguins[:1]
  
