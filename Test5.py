import streamlit as st
import pandas as pd
from pandasai import PandasAI
import streamlit as st
from pandasai.llm.openai import OpenAI
import matplotlib
matplotlib.use('TkAgg')


st.title("Data Analysis With PandasAI")
api_key = st.text_input("PLease provide the api key to start your Analysis")


def res(df,a):
    if a != '':
        try:
            with st.spinner("Please Wait....."):
                st.write(Pandas_ai.run(df,prompt = a))
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Wait a Minute")

if api_key != '':
        llm = OpenAI(api_key)
        Pandas_ai = PandasAI(llm)
        uploaded_file = st.file_uploader('Upload a file')
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.info("File Uploaded Successfully")
            st.write(df.head())
            a = st.text_input("How can I help you")
            st.button("Submit", on_click=res(df, a))
            #st.download_button("Download CSV", df.to_csv(), mime='text/csv')
