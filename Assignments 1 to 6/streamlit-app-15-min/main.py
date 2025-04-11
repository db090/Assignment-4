import streamlit as st
import pandas as pd
import numpy as np

#title
st.title("Titanic Dataset Viewer")

#load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("train.csv")

df=load_data()
df["Age"]=np.floor(df["Age"].fillna(df["Age"].mean()))



# Option to show shape
if st.checkbox("Show dataset shape"):
    st.write(f"Rows:{df.shape[0]}, Columns:{df.shape[1]}")

# Option to show only five rows from start
if st.checkbox("Show First five rows"):
    st.dataframe(df.head())

# Option to see how many people got killed and how many survived
if st.checkbox("Show how many people died or survived"):
    survived_count=df["Survived"].value_counts()
    st.write("Survived:",survived_count.get(1,0))
    st.write("Died:",survived_count.get(0,0))
#Option to view specific columns
columns=st.multiselect("Select columns to view",df.columns.tolist(),default=df.columns.tolist())
st.dataframe(df[columns])