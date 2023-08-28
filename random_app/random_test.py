import streamlit as st

st.title('🦜🔗 Test Trial App')

st.sidebar.selectbox("How would you like to be contacted?", ("Email", "Home phone", "Mobile phone","snail mail"))

with st.form('my_form'):
  text = st.text_area('Please enter your query:', 'What are the three key pieces of advice for learning how to code?')