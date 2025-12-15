import streamlit as st
import pandas as pd
st.title("chai Sale Dashboard")
file=st.file_uploader("Upload your cs file", type=["csv"])
if file:
    df=pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)
if file:
    st.subheader("summary stats")
    st.write(df.describe()) 
if file:
    cities=df["place"]
    selected_city=st.selectbox("filter by place", cities)
    filtered_data=df[df["place"]==selected_city]
    st.dataframe(filtered_data)       