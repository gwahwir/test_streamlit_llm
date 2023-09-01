import streamlit as st
import time

st.title('🦜🔗 Test Trial App')

st.write("the first of where will this code be")
st.markdown("what is a markdown")
st.subheader("subheaders are funny")
st.code("st.latex(r''' a+a r^1+a r^2+a r^3 ''')")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


with st.sidebar:
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

    st.write("where will this code be?")

    
with st.form('my_form'):
    text = st.text_area(
        'Please enter your query:', 
        'What are the three key pieces of advice for learning how to code?'
        )

    st.write("where will this code be then?")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

st.video("https://www.youtube.com/watch?v=_JTLesSMw1s")