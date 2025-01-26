# **Mini Project: Descriptive Analytics on Movie Ratings**

## **Overview**

This mini project focuses on **Descriptive Analytics** using file handling, where we analyze a dataset of movie ratings. The project covers various aspects of the movie industry, such as distribution of ratings, genre insights, user engagement, rating distributions by demographics, top performers, and more. The goal is to generate meaningful insights and visualize the data in an interactive and user-friendly way.

---

## **Project Objectives**

- **Descriptive Analysis**: Understand the distribution of movie ratings, including high, medium, and low ratings, and identify the top 10 most-rated movies.
- **Genre Insights**: Investigate which movie genres are most frequently rated and analyze average ratings across different genres.
- **User Engagement Analysis**: Identify the most active users based on the number of ratings they’ve given and explore the relationship between user demographics and their movie preferences.
- **Rating Distribution by Demographics**: Analyze how ratings vary by user demographic attributes (age, gender, occupation) and whether certain genres are preferred by specific groups.
- **Top Performers**: Identify movies with the highest average ratings and analyze their characteristics such as release year and genres.
- **Exploring Long Tail**: Investigate movies that receive very few ratings and compare their characteristics to those of popular movies.
- **Tag Analysis**: Analyze the most frequently used tags and check if they align with movie genres.
- **Visualization**: Create dashboards to visualize:
  - Distribution of ratings by genres and years.
  - Popular genres by user demographics.
  - Heatmaps showing the correlation between genres, user activity, and ratings.

---

## **Dataset Description**

This project uses the MovieLens dataset (1M ratings) which includes the following files:
- **ratings.dat**: Contains user ratings for movies.
  - Columns: `UserID`, `MovieID`, `Rating`, `Timestamp`
- **movies.dat**: Contains information about the movies.
  - Columns: `MovieID`, `Title`, `Genres`
- **users.dat**: Contains demographic information of the users.
  - Columns: `UserID`, `Gender`, `Age`, `Occupation`, `ZipCode`

---

## **Features and Insights**

### **1. Descriptive Analysis**
- Distribution of movie ratings into high (5), medium (3-4), and low (1-2) ratings.
- Top 10 most-rated movies.

### **2. Genre Insights**
- The most frequently rated movie genres.
- Comparison of average ratings across different genres.

### **3. User Engagement Analysis**
- Identification of the most active users based on the number of ratings.
- Analysis of user demographics (age, gender, occupation) and their rating patterns.

### **4. Rating Distribution by Demographics**
- Investigating how ratings vary based on user demographics (age, gender, occupation).
- Analysis of genre preferences across different demographics.

### **5. Top Performers**
- Identification of the highest-rated movies, considering a minimum number of ratings for fairness.
- Analysis of movie characteristics (release year, genre) for top-rated movies.

### **6. Exploring Long Tail**
- Analysis of movies that receive very few ratings.
- Comparison of characteristics between less-rated and popular movies.

### **7. Tag Analysis**
- Most frequently used tags associated with movies.
- Consistency of tags with movie genres.

### **8. Visualization**
- Dashboards visualizing:
  - Rating distribution by genres and years.
  - Popular genres by user demographics.
  - Heatmap showing correlations between genres, user activity, and ratings.

---

## **Technology Stack**

- **Python Libraries**:
  - `pandas`: Data manipulation and analysis.
  - `matplotlib`: Plotting and visualization.
  - `seaborn`: Statistical data visualization.
  - `streamlit`: For creating interactive dashboards.
  
- **Dataset**: MovieLens 1M Dataset (available at [MovieLens](https://grouplens.org/datasets/movielens/1m/)).

---

## **Installation Instructions**

### **1. Install Dependencies**

To run this project, you'll need to install the following Python libraries:

```bash
pip install pandas matplotlib seaborn streamlit
