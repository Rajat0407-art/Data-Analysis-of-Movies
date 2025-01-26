#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def load_data():
    """
    Load the ratings, movies, and users datasets from specified file paths.
    """
    try:
        # Update file paths
        ratings_file = r"C:\Users\rajat\Downloads\Dataset for Project\ml-1m\ratings.dat"  # Update the path as per your location
        movies_file = r"C:\Users\rajat\Downloads\Dataset for Project\ml-1m\movies.dat"    # Update the path as per your location
        users_file = r"C:\Users\rajat\Downloads\Dataset for Project\ml-1m\users.dat"      # Update the path as per your location

        # Load data with encoding specified
        ratings = pd.read_csv(ratings_file, sep="::", names=["UserID", "MovieID", "Rating", "Timestamp"], engine="python", encoding="ISO-8859-1")
        movies = pd.read_csv(movies_file, sep="::", names=["MovieID", "Title", "Genres"], engine="python", encoding="ISO-8859-1")
        users = pd.read_csv(users_file, sep="::", names=["UserID", "Gender", "Age", "Occupation", "ZipCode"], engine="python", encoding="ISO-8859-1")

        return ratings, movies, users

    except Exception as e:
        st.error(f"Error while loading data: {e}")
        return None, None, None


def create_dashboard(ratings, movies, users):
    """
    Create a minimalist dashboard for visualizing movie ratings data using Streamlit.
    """
    # Merge datasets
    merged_data = pd.merge(pd.merge(ratings, users, on="UserID"), movies, on="MovieID")

    # 1. Distribution of Ratings by Genres
    genres_data = merged_data["Genres"].str.get_dummies("|").multiply(merged_data["Rating"], axis=0)
    genre_ratings = genres_data.sum() / genres_data.count()

    # Display genre ratings bar chart
    st.subheader("Average Ratings by Genre")
    st.bar_chart(genre_ratings.sort_values(ascending=False))

    # 2. Popular Genres by User Demographics (Gender)
    gender_genre = merged_data.groupby(["Gender"]).sum(numeric_only=True).T
    gender_genre = gender_genre[~gender_genre.index.str.contains("UserID|MovieID|Age|Occupation|ZipCode|Timestamp")]
    gender_genre_plot = gender_genre.plot(kind="bar", figsize=(12, 6), stacked=True, color=["#FF9999", "#9999FF"], edgecolor="black")
    st.subheader("Popularity of Genres by Gender")
    st.pyplot(gender_genre_plot.figure)

    # 3. Heatmap: Correlation between Genres, User Activity, and Ratings
    genres_corr = genres_data.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(genres_corr, annot=False, cmap="coolwarm", cbar=True)
    st.subheader("Correlation Heatmap Between Genres and Ratings")
    st.pyplot(plt)

    # Displaying some basic stats or tables
    st.subheader("Sample Data Preview")
    st.write(merged_data.head())

    # Optionally, you can add more features or filters for interactivity:
    st.sidebar.header("Filters")
    selected_genre = st.sidebar.selectbox("Select a Genre", options=merged_data["Genres"].unique())
    filtered_data = merged_data[merged_data["Genres"].str.contains(selected_genre)]
    st.write(f"Filtered Data for Genre: {selected_genre}")
    st.write(filtered_data.head())

    st.success("Dashboard created successfully!")


def main():
    """
    Main function to load data and create the dashboard.
    """
    st.title("Movie Ratings Analysis Dashboard")

    ratings, movies, users = load_data()
    if ratings is not None and movies is not None and users is not None:
        create_dashboard(ratings, movies, users)
    else:
        st.error("Dashboard could not be created due to errors in data loading.")


if __name__ == "__main__":
    main()


# In[ ]:




