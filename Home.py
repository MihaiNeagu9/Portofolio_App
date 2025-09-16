import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Neagu Mihai-Daniel")
    content = """ 
    Passionate about technology and programming, self-taught with a solid foundation in the fundamental concepts of computer science. 
    I have taken online courses and developed practical projects that have strengthened my skills in programming, web development, and problem solving.
    """
    st.info(content)

content2 = """ 
 Below you can find some of the apps I have built in Python.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row["image"]}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[4:8].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row["image"]}")
        st.write(f"[Source Code]({row['url']})")
