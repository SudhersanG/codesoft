# Movie dataset (Movie names and their genres)
movies = {
    'Movie1': ['Action', 'Adventure', 'Sci-Fi'],
    'Movie2': ['Drama', 'Romance'],
    'Movie3': ['Action', 'Thriller'],
    'Movie4': ['Comedy', 'Romance'],
    'Movie5': ['Horror', 'Thriller'],
    'Movie6': ['Action', 'Adventure', 'Fantasy'],
    'Movie7': ['Drama', 'Mystery'],
    # Add more movies and their genres
}

# User preferences for genres
user_preferences = ['Action', 'Adventure']

# Function to recommend movies based on user preferences
def recommend_movies(preferences, movie_data):
    recommended_movies = []
    for movie, genres in movie_data.items():
        # Check if the movie contains any of the preferred genres
        if any(genre in preferences for genre in genres):
            recommended_movies.append(movie)
    return recommended_movies

# Get movie recommendations for the user
recommended_movies = recommend_movies(user_preferences, movies)

if recommended_movies:
    print("Recommended Movies:")
    for movie in recommended_movies:
        print(movie)
else:
    print("No movies found matching your preferences.")

