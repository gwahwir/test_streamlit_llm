import streamlit as st

st.title('🦜🔗 Test Trial App')


with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

    add_selectbox = st.selectbox(
       "How would you like to be contacted?", 
       ("Email", "Home phone", "Mobile phone","snail mail")
       )

with st.form('my_form'):
  text = st.text_area('Please enter your query:', 'What are the three key pieces of advice for learning how to code?')