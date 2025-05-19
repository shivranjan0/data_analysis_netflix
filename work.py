# netflix_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Netflix Dashboard", layout="wide")

# Load the dataset
df = pd.read_csv(r"E:\data_analysis_netflix\archive\netflix_titles.csv")

# Preprocessing
df = df.drop_duplicates()
df['director'].fillna("Unknown", inplace=True)
df['cast'].fillna("Unknown", inplace=True)
df['country'].fillna("Unknown", inplace=True)
df['rating'].fillna("Not Rated", inplace=True)
df.dropna(subset=['date_added'], inplace=True)

df['date_added'] = df['date_added'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

df['genre_list'] = df['listed_in'].str.split(', ')
df['country_list'] = df['country'].str.split(', ')
df['actor_list'] = df['cast'].str.split(', ')

# Title
st.title("Netflix Data Dashboard")
st.markdown("Explore trends, genres, countries, actors and directors on Netflix")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Content Overview", "Genres", "Countries", "Actors", "Directors"])

with tab1:
    st.header(" Content Added Per Year")
    content_count = df['year_added'].value_counts().sort_index()
    fig, ax = plt.subplots()
    content_count.plot(kind='bar', ax=ax, color='plum')
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Titles")
    ax.set_title("Content Added Per Year")
    st.pyplot(fig)

    st.subheader("Type of Content")
    st.bar_chart(df['type'].value_counts())

with tab2:
    st.header("Top 10 Genres")
    top_genres = df['genre_list'].explode().value_counts().head(10)
    fig, ax = plt.subplots()
    top_genres.plot(kind='barh', ax=ax, color='skyblue')
    ax.set_xlabel("Number of Titles")
    ax.set_title("Top 10 Genres on Netflix")
    ax.invert_yaxis()
    st.pyplot(fig)

with tab3:
    st.header("Top 10 Countries Producing Content")
    top_countries = df['country_list'].explode().value_counts().head(10)
    fig, ax = plt.subplots()
    top_countries.plot(kind='bar', ax=ax, color='orange')
    ax.set_ylabel("Number of Titles")
    ax.set_title("Top 10 Countries on Netflix")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with tab4:
    st.header("Top 10 Most Frequent Actors")
    top_actors = df['actor_list'].explode().value_counts().head(10)
    fig, ax = plt.subplots()
    top_actors.plot(kind='barh', ax=ax, color='mediumseagreen')
    ax.set_xlabel("Number of Titles")
    ax.set_title("Top 10 Most Frequent Actors")
    ax.invert_yaxis()
    st.pyplot(fig)

with tab5:
    st.header("Top 10 Most Frequent Directors")
    top_directors = df['director'].value_counts().head(10)
    fig, ax = plt.subplots()
    top_directors.plot(kind='bar', ax=ax, color='coral')
    ax.set_ylabel("Number of Titles")
    ax.set_title("Top 10 Most Frequent Directors")
    plt.xticks(rotation=45)
    st.pyplot(fig)


