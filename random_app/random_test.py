import streamlit as st
import time

st.title('🦜🔗 Test Trial App')


with st.sidebar:
    
    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)", "SLOW (100 days)")
    )

    add_selectbox = st.selectbox(
       "How would you like to be contacted?", 
       ("Email", "Home phone", "Mobile phone","snail mail")
       )
    
    with st.echo():
        st.write("This code will be printed to the sidebar.")
    
    add_write = st.write("where will this code be?")

    
with st.form('my_form'):
  text = st.text_area('Please enter your query:', 'What are the three key pieces of advice for learning how to code?')

  st.write("where will this code be?")
