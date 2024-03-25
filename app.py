import pandas as pd
import pandasai
from pandasai import SmartDatalake
from pandasai.llm import OpenAI
import streamlit as st
from dotenv import load_dotenv
import json


st.set_page_config(layout='wide')
load_dotenv()

def chat_with_csv(df, prompt) :
    llm = OpenAI()
    dl = SmartDatalake([df], config={"llm": llm})
    output = dl.chat(prompt)
    print(output)
    return output

st.title("chatCSV powered by LLM")

input_csv = st.file_uploader("Upload your CSV file", type=['csv'])
if input_csv :
    col1, col2 = st.columns([1,1])

    with col1 :
        st.info("CSV uploaded successfully...")
        data = pd.read_csv(input_csv)
        st.dataframe(data)
    with col2 :
        st.info("Chat with your CSV")
        input_text = st.text_input("Enter your query: ")
        if input_text :
            if st.button("chat with csv") :
                st.info("Your query: "+input_text)
                result = chat_with_csv(data, prompt=input_text)

                if type(result) == 'png' :
                    st.pyplot(result)
                st.success(result)



