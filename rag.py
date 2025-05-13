from dotenv import load_dotenv
from langchain_google_genai.llms import GoogleGenerativeAI
import streamlit as st
import PyPDF2 as pdf
import os
import warnings
warnings.filterwarnings("ignore")

load_dotenv()
GEMINI_API_KEY=st.sidebar.text_input(label="Enter your Gemini-pro API key",type ="password")

# Generate the LL response
def get_response(input):
    try:
        llm = GoogleGenerativeAI(
            api_key=GEMINI_API_KEY,  # Ensure the api_key is passed correctly
            model="gemini-2.0-flash"
        )
        response = llm.invoke(input)
        return response
    except Exception as e:
        return f"An error occurred: {e}"
    

def input_file(file):
    reader = pdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

st.title("Dock Ai")
file1 = st.file_uploader("Upload Your patient record", type="pdf", help="Please upload")
submit = st.button("Submit")


if submit:
    if file1 is not None:
        with st.spinner("Analyzing document, please wait..."):
            text = input_file(file1)

            # Construct the full prompt dynamically
            full_prompt = f"""
summary of the {text} with in 1000 words
"""

            response_stream = get_response(full_prompt)
            st.write(response_stream)
            st.success("✅ Analysis complete!")
    else:
        st.warning("Please upload a PDF file before submitting.")
            