import numpy as np
import pandas as pd
import streamlit as st 
import plotly.express as px

#loading the data 
@st.cache_data
def load_data():
    path = 'data/kc_house_data.csv'
    df = pd.read_csv(path)
    return df 

#call the load_data function 
with st.spinner('loading data....'):
     df = load_data()  


#create a little for your app
st.title('house price Data Analysis')
st.subheader('key performance indicator')

#get the list of all coloums 
cols = df.columns.tolist()
selected_cols = st.multiselect('select columns',cols)
st.write(f'you selected:{len(selected_cols)} columns')

for col in selected_cols:
    try:
        st.metric(label=f'mean {col}',
                value=round(df[col].mean()),
                delta=round(df[col].std()))
        st.line_chart(df[col],use_container_width=True)
    except Exception as e:
       
        st.error(f'cannot display{col} numeric data')
        
          



