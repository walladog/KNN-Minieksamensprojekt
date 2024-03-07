import streamlit as st
from BetterMovieDB_API import *
from KNNactual import *

filmLiaste = FilmListeKlasse()



st.write("""
Goddag ! 
""")

filmNavn = st.text_input("søg film:")

response = findFilm(f'{filmNavn}')

PosterURL = findFilm(f'{filmNavn}')['poster_path']
Overwiew = findFilm(f'{filmNavn}')['overview']
Title = findFilm(f'{filmNavn}')['original_title']

st.write(f"Du har valgt {Title}")

st.image(f'https://image.tmdb.org/t/p/w500{PosterURL}', caption=f'{Overwiew}')
choice = st.radio("kan du lide denne film?", ["Ja","Nej"])
TilføjFilm_clicked = st.button("Tilføj film")

if TilføjFilm_clicked:
    if choice == 'Ja':
        st.write(f'filmen "{Title}" er nu tilføjet som en film du kan lide')
        filmLiaste.addFilm(response['original_title'],response['genre_ids'],response['vote_average'],response['vote_count'], 1)
    
    elif choice == 'Nej':
        st.write(f'filmen "{Title}" er nu tilføjet som en film du ikke kan lide')
        filmLiaste.addFilm(response['original_title'],response['genre_ids'],response['vote_average'],response['vote_count'], -1)

    st.write(f'{filmLiaste.filmListe}')

