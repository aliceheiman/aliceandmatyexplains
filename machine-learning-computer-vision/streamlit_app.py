import streamlit as st

st.set_page_config(page_title="Introduction")

pages = {
    "Introduction": [
        st.Page("pages/0a_introduction.py", title="Welcome!"),
        st.Page("pages/0b_reference.py", title="Reference"),
    ],
    "Chapter 1: Machine Learning Fundamentals": [
        st.Page("pages/1a_linear_regression.py", title="Linear Regression"),
        st.Page("pages/1b_linear_classification.py", title="Linear Classification"),
    ],
    "Chapter 2": [
        # st.Page("learn.py", title="Learn about us"),
    ],
}

pg = st.navigation(pages)
pg.run()
