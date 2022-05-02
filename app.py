"""
    Launching application: streamlit run app.py
"""
import json

import streamlit as st
from faker import Faker

fake = Faker('en')

num_recommendations = 2


def generate_detailed_film_info(_):
    return [dict(
        id=fake.random.randint(0, 10000),
        title=fake.name()[:10],
        director=fake.name(),
        image='figures/sample_poster.webp',
        average_rating=fake.random.randint(1, 5),
    ) for _ in range(num_recommendations)]


is_user_rated_initial_films = False
is_user_rated_recommended_films = False

st.set_page_config(page_title="Recommendation system", page_icon="🐞", layout="centered")
st.sidebar.write("This contains information about how to use application")

st.title("Application for evaluation of recommendational system")
st.write("Please rate films by assigning rating from 1 to 5")

form = st.form("user_film_ratings")

# Stores tuples: (film title, rating)
user_ratings = []
with form:
    n_cols = 2
    n_rows = 1

    columns = st.columns(n_cols)

    for ii, column in enumerate(columns):
        for jj in range(n_rows):
            title = fake.name()[:10]
            column.write(title)
            column.image("figures/sample_poster.webp", width=150)

            select_box = column.selectbox(f'Rating', ['-', 1, 2, 3, 4, 5], key=f"selectbox_col_{ii}_row_{jj}")
            user_ratings.append((title, select_box))

    submitted = form.form_submit_button()

if submitted:
    if not all(map(lambda x: x[1] != '-' and x[1] > 0, user_ratings)):
        st.warning("Not all fields are filled")
    else:
        st.balloons()
        st.write('Successfully filled form, generating recommendations...')
        st.session_state.user_ratings = user_ratings

if 'user_ratings' in st.session_state:

    recommendations_form = st.form("recommendations_form")

    # Stores tuples of (film_id, film_rating)
    recommendation_ratings = []
    with recommendations_form:
        for ii, film in enumerate(generate_detailed_film_info(user_ratings)):
            image_column, info_column = st.columns(2)

            with image_column:
                st.image(film['image'], width=200)

            with info_column:
                st.write(f"Title: {film['title']}")
                st.write(f"Director: {film['director']}")
                st.write(f"Average rating: {film['average_rating']}")
                select_box = st.selectbox("Your rating", ['-', 1, 2, 3, 4, 5], key=f"recommendation_{ii}")

                recommendation_ratings.append((film['id'], select_box))

        button = st.form_submit_button()

    if button:
        if not all(map(lambda x: x[1] != '-' and x[1] > 0, recommendation_ratings)):
            st.warning("Not all fields are filled")
        else:
            st.balloons()
            st.write('Everything is ready, creating dump...')
            st.session_state.recommendation_ratings = recommendation_ratings
            st.write("Some logs...")
