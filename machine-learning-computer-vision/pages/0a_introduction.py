import streamlit as st

header = st.container()
introduction = st.container()

with header:
    st.title("🤖 Machine Learning and Computer Vision")
    st.info(
        "Welcome to **Machine Learning and Computer Vision**! The aim of this interactive course is to explore the algorithms of machine learning and computer vision, and build it up as if *you where discovering and creating this yourself*."
    )
    st.text("Let's go on an adventure!")

with introduction:
    st.header("Introduction")
