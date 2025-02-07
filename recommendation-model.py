import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


csv_path = "user_data.csv"
train_data = pd.read_csv(csv_path)

train_data['combined'] = train_data['preferences'] + ',' + train_data['artists']

vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(train_data['combined'])

similarity_matrix = cosine_similarity(feature_matrix)


def recommend(user_id, train_data, similarity_matrix, top_n=3):


    if user_id not in train_data['id'].values:
        print(f"User ID {user_id} not found in the dataset.")
        return pd.DataFrame()

    user_idx = train_data[train_data['id'] == user_id].index[0]


    similarity_scores = similarity_matrix[user_idx]

    similar_users_indices = similarity_scores.argsort()[::-1][1:top_n+1]

    recommended_users = train_data.iloc[similar_users_indices]
    return recommended_users

try:
    user_id = int(input("Enter the user ID for recommendations (e.g., 1 to 20): "))

    recommendations = recommend(user_id, train_data, similarity_matrix, top_n=3)

    if not recommendations.empty:
        print(f"\nRecommendations for User ID {user_id}:")
        print(recommendations[['id', 'name', 'preferences', 'artists']])
    else:
        print("No recommendations could be made.")
except ValueError:
    print("Invalid input. Please enter a valid user ID (integer).")