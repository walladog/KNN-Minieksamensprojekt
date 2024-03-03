import streamlit as st
from BetterMovieDB_API import *

st.write("""
Goddag ! 
""")

filmNavn = st.text_input("søg film:")

PosterURL = findFilm(f'{filmNavn}')['poster_path']
Overwiew = findFilm(f'{filmNavn}')['overview']
Title = findFilm(f'{filmNavn}')['original_title']

st.write(f"Du har valgt {Title}")

st.image(f'https://image.tmdb.org/t/p/w500{PosterURL}', caption=f'{Overwiew}')
choice = st.radio("kan du lide denne film?", ["Ja","Nej","Har ikke set den"])
is_clicked = st.button("Enter")

