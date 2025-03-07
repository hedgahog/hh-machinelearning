import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('🤖Machine Learning App')

st.info('This app builds a machine learning model!')
with st.expander('Data'): # Dropdown for data below
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/da9653dfdb975b7342fa3a1a3b74375e35a9c1e5/penguins_cleaned.csv')
  df

  st.write('**X**')
  X_raw = df.drop('species', axis=1) # exclude species column
  X_raw

  st.write('**y**')
  y_raw = df.species
  y_raw
# Scatter plot for data
with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# Input features
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
  input_penguins = pd.concat([input_df, X_raw], axis=0)
with st.expander('Input features'):
  st.write('**Input penguin**')
  input_df
  st.write('**Combined penguin data**')
  input_penguins
# Data preparation
# Encode X
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)

X = df_penguins[1:]
input_row = df_penguins[:1]

# Encode y
target_mapper = {'Adelie': 0,
                 'Chinstrap': 1,
                 'Gentoo': 2}
def target_encode(value):
  return target_mapper[value]
y_raw = y_raw.str.strip().str.capitalize()
y = y_raw.apply(target_encode)
y
y_raw

with st.expander('Data preparation'):
  st.write('**Encoded X (input penguin)**')
  input_row
  st.write('**Encoded y**')
  y
  
# Model training and inference
## Train the ML model
clf = RandomForestClassifier()
clf.fit(X, y)

## apply model to make predictions
prediction = clf.predict(input_row)
prediction_proba = clf.predict_proba(input_row)

df_prediction_proba = pd.DataFrame(prediction_proba)

  
