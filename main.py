import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Neagu Mihai-Daniel")
    content = """ 
    Absolvent al Facultății de Energetică, specializarea Energetică și
Tehnologii Nucleare, cu o bază solidă de cunoștințe teoretice în
domeniul energetic. Deși nu am experiență practică directă, sunt
dornic să aplic conceptele învățate și să îmi dezvolt abilitățile întrun mediu profesionist. Sunt motivat să contribui la proiecte
inovatoare și să învăț într-o echipă dinamică, orientată spre soluții
sigure și sustenabile în sectorul energetic.
    """
    st.info(content)

content2 = """ 
 Below you cand fiind some of the apps I have built in Python.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row["image"]}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row["image"]}")
        st.write(f"[Source Code]({row['url']})")