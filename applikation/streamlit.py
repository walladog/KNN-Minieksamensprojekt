import streamlit as st
import Themoviedb_API
from BetterMovieDB_API import *

st.write("""
# Bing chilling
Goddav *skøge!*
""")

x = st.text_input("How big = cock?")
st.write(f"din pik er {x} lang")
is_clicked = st.button("click for bitches :eggplant:")

PosterURL = findFilm('forest gump')['poster_path']

st.image(f'https://image.tmdb.org/t/p{PosterURL}', caption='Sunrise by the mountains')
choice = st.radio("kan du lide denne film?", ["Ja","Nej","Har ikke set den"])

