import streamlit as st
import Themoviedb_API
from BetterMovieDB_API import *

st.write("""
# Bing chilling
Goddav *skøge!*
""")

filmNavn = st.text_input("søg film:")
st.write(f"du har valgt {filmNavn}")

PosterURL = findFilm(f'{filmNavn}')['poster_path']
Overwiew = findFilm(f'{}')

st.image(f'https://image.tmdb.org/t/p/w500{PosterURL}', caption=findFilm(f'{filmNavn}')['overwiew'])
choice = st.radio("kan du lide denne film?", ["Ja","Nej","Har ikke set den"])
is_clicked = st.button("Enter")

