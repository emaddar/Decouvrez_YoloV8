import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")


st.set_page_config(page_title="Computer vision", page_icon="🖥️", layout="wide")

st.markdown("""

# Welcome to our Computer Vision project! 😃 

""")

st.image("https://blog.deloitte.fr/wp-content/uploads/2019/02/computer-vision-blog.png")

st.markdown("""

## Please choose a model from the left-hand menu. 🖥️
""")