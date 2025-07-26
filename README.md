🎬 Movie Recommender System


A content-based Movie Recommender System built with Python, Pandas, Scikit-learn, and Streamlit. This app suggests similar movies based on the user's selected movie using cosine similarity on movie metadata.


🔍 Features
Content-based filtering using genres, keywords, cast, and crew

Dataset Link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata


Cosine similarity for recommendation


Interactive frontend built with Streamlit

Clean UI with styled interface

Easy to use and fast responses

🚀 Live Demo link: https://movie-recommender-bysatyam.streamlit.app/

🔗 Check it out on Streamlit
(Replace with your deployed URL)


🧠 Tech Stack


Language:	Python

Data Handling: Pandas, NumPy

ML & NLP: Scikit-learn, NLTK

Deployment:	Streamlit, GitHub

Visualization: Matplotlib, Seaborn (if used)


🛠️ Installation

Clone the repository:

bash


git clone https://github.com/Satyam-Singh-x/movie-recommender.git

cd movie-recommender

Install dependencies:

bash

pip install -r requirements.txt


📁 Files in this Repository


app.py: Main Streamlit web app script for movie recommendation

movie-recommender-system.ipynb:  Data preprocessing , EDA and model building using NLTK

movies.pkl: Pickle file storing cleaned and processed movie metadata

requirements.txt: Lists all dependencies required to run the application

Note:
The similarity.pkl file is not stored in the repository due to its size.
It is loaded dynamically from Google Drive at runtime using gdown.


🧠 How It Works
Load movie metadata and similarity matrix from .pkl files.

User selects a movie from the dropdown.

System finds top 5 similar movies using cosine similarity.

Titles and posters of recommended movies are displayed.

📸 Screenshots
Home: https://drive.google.com/file/d/1gErr2yVMo1rr8zJaJeMrDMmARccZj7ZL/view?usp=drive_link

📦 Deployment
Deployed using Streamlit. For deployment:

Push your code to GitHub

Create an app on Streamlit Cloud

Add app path and repo link

Make sure requirements.txt is present


🙋‍♂️ Author

Satyam Singh

B.Tech, Chemical Engineering – Jadavpur University

LinkedIn: https://www.linkedin.com/in/satyam-singh-61152a334 | singhsatyam.0912@gmail.com



📄 License
This project is licensed under the MIT License











