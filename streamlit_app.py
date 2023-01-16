import streamlit as st
import pandas as pd

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

df = pd.DataFrame(option, columns=('Test'))

st.table(df)
