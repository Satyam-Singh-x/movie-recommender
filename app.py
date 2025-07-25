import streamlit as st
import pickle
import pandas as pd
import requests

import gdown
import os

# Google Drive file ID (extracted from your link)
file_id = '17IyZf2_kLW59zNVCcMDgByVBIMUpryNi'
output_file = 'sim.pkl'

# Download only if not already downloaded
if not os.path.exists(output_file):
    with st.spinner('Downloading large model file...'):
        gdown.download(f'https://drive.google.com/uc?id={file_id}', output_file, quiet=False)

# Load the pickle file
with open(output_file, 'rb') as f:
    similarity = pickle.load(f)

def fetch_poster(movie_id):
 response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=82b6234edc23f067feacca6bbd34e865&language=en-US'.format(movie_id))
 data=response.json()
 return 'https://image.tmdb.org/t/p/w500/'+ data['poster_path']


def recommend(movie):
 movie_index = movies[movies['title'] == movie].index[0]
 distances = similarity[movie_index]
 movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

 recommended_movies = []
 recommended_movies_posters=[]

 for i in movies_list:
  movie_id=movies.iloc[i[0]].movie_id
  #fetch poster from api
  recommended_movies_posters.append(fetch_poster(movie_id))
  recommended_movies.append(movies.iloc[i[0]].title)
 return recommended_movies,recommended_movies_posters


movies=pickle.load(open('movies.pkl', 'rb'))
movies_list_name=movies['title'].values


import streamlit as st

st.markdown(
    """
    <style>
    .main-title {
        font-size: 36px;
        font-weight: 600;
        text-align: center;
        color: white;
        font-family: 'Georgia', serif;
        padding: 15px 0;
        letter-spacing: 1px;
    }
    </style>
    <div class="main-title">MOVIE RECOMMENDER SYSTEM</div>
    """,
    unsafe_allow_html=True
)



st.markdown(
    """
    <style>
    .custom-label {
        font-size: 24px;
        font-weight: bold;
        color: #1f77b4;
        font-family: 'Segoe UI', sans-serif;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom label text
st.markdown("<div class='custom-label'>Search Your Favourite Movies Here:</div>", unsafe_allow_html=True)

selected_movie_name=st.selectbox(
 '',
 movies_list_name
)
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

if st.button('Recommend'):
  names,posters = recommend(selected_movie_name)
  col1, col2,col3,col4,col5= st.columns(5)
  with col1:
   st.text(names[0])
   st.image(posters[0])
  with col2:
   st.text(names[1])
   st.image(posters[1])
  with col3:
   st.text(names[2])
   st.image(posters[2])
  with col4:
   st.text(names[3])
   st.image(posters[3])
  with col5:
   st.text(names[4])
   st.image(posters[4])
