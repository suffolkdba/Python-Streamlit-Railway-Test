import io
import os
import streamlit as st
import pandas as pd


st.set_page_config(
    page_title = 'Railway.io Deployment Test',
    page_icon = '🍻',
    layout = 'wide',
)


st.title("Railway Test")

testdata = ['Bob', 'Alice', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy', 'Mallory', 'Oscar', 'Peggy', 'Trent', 'Victor', 'Walter', 'Zoe']
df = pd.DataFrame(testdata, columns=['Names'])

with st.expander("Test Data", expanded=True):
    st.write(df)

