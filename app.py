
# python
import streamlit as st
import pandas as pd
from data_cleaner import clean_data
from llm_helper import ask_llm

st.title("AI Data Assistant")

st.header("AI Data Cleaning Chatbot")

uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Raw Data")
    st.dataframe(df)

    if st.button("Clean Data"):

        clean_df, report = clean_data(df)

        st.write("Cleaning Report")
        for r in report:
            st.write(r)

        st.write("Cleaned Data")
        st.dataframe(clean_df)

        st.download_button(
            "Download Clean Data",
            clean_df.to_csv(index=False),
            "cleaned_data.csv"
        )

question = st.text_input("Ask about your dataset")

if question:
    answer = ask_llm(question)
    st.write(answer)
st.markdown("---")
st.markdown("Developed by **Swarup Raut** 🚀")
