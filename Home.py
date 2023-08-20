import streamlit as st
import pandas as pd
import pathlib
st.set_page_config(page_title="My portfolio",layout="wide")

col1,col2=st.columns(2)


with col1:
    st.write(" ")
    st.write(" ")
    st.image("images/photo.png",width=450 )
    #st.empty()

with col2:

    st.title("Muneeb Ur Rehman")
    content="""As a skilled Python programmer and developer, 
    I hold a strong command over the language and take pleasure in crafting efficient and elegant solutions.
     My expertise was further solidified by completing a comprehensive Udemy certification,
      where I honed my skills and delved into various Python applications. 
      Additionally, I hold a Bachelor of Science in Computer Science from Fast NUCES Lahore, 
      which provided me with a robust foundation in computer science principles and practices.
       With a passion for continuous learning and a proven track record of successful projects,
     I am ready to take on new challenges and contribute to the
      world of software development with dedication and creativity."""
    st.info(content)
st.write(" ")
st.write("Below You can find some of the apps I have built in Python,Feel free to Contact me.")

col3,empty,col4=st.columns([1.5,0.5,1.5])
"""This list indicates that the thereare 3 columns in total and 1st and 3rd columns are 3 times wider than the 2nd column """
df=pd.read_csv("data.csv",sep=";")
st.write(" ")
st.write(" ")
with col3:

    for index,row in df[:10].iterrows():# slicing of the dataframe
        st.header(row["title"])# as it is described that row is a tuple so we need to access it by index, not by name
        st.write(row["description"])
        img=row["image"]
        path=f"images/{img}"
        st.image(path)
        link=row["url"]
        st.markdown("[Source Code](link)")
with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        img = row["image"]
        path = f"images/{img}"
        st.image(path)
        link = row["url"]
        st.markdown("[Source Code](link)")





