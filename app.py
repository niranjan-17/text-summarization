import streamlit as st
from transformers import pipeline


def summary(text):
    pipe = pipeline('summarization', model='t5_samsum_summarization', device=0)
    output = pipe(text)
    return output

st.title("Text Summarizer")
st.write("This app uses a pre-trained T5 model to summarize text.")

# Input text area for user input
input_text = st.text_area("Input Text", placeholder="Write text to summarize")

# Button to generate summary
if st.button("Summarize"):
    if input_text:
        output= summary(input_text)
        # Display the summary
        st.subheader("Summary")
        st.write(output[0]['summary_text'])
    else:
        st.write("Please enter text to summarize.")

st.write("---")
st.write("Created  using Streamlit and Transformers")