#Collaborative filtering algorithm

# Import libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load user-item ratings data
ratings_data = pd.read_csv('ratings.csv')

# Compute user-user similarity matrix
user_similarity = cosine_similarity(ratings_data)

# Identify top similar users for each user
n_users = ratings_data.shape[0]
top_similar_users = {}
for i in range(n_users):
    top_similar_users[i] = np.argsort(-user_similarity[i])[1:10]
    
# Generate recommendations for a user
def generate_recommendations(user_id):
    user_ratings = ratings_data.loc[ratings_data['User_ID'] == user_id]
    similar_users = top_similar_users[user_id]
    similar_users_ratings = ratings_data[ratings_data['User_ID'].isin(similar_users)]
    similar_users_ratings = similar_users_ratings.groupby('Item_ID').agg({'Rating': np.mean})
    similar_users_ratings = similar_users_ratings.reset_index()
    user_ratings = user_ratings[['Item_ID', 'Rating']]
    user_ratings.columns = ['Item_ID', 'User_Rating']
    merged_ratings = pd.merge(user_ratings, similar_users_ratings, on='Item_ID')
    merged_ratings['Similarity'] = merged_ratings.apply(lambda row: user_similarity[user_id][row['User_ID']-1], axis=1)
    merged_ratings['Weighted_Rating'] = merged_ratings.apply(lambda row: row['Rating']*row['Similarity'], axis=1)
    grouped_ratings = merged_ratings.groupby('Item_ID').agg({'Weighted_Rating': np.sum, 'Similarity': np.sum})
    grouped_ratings['Weighted_Rating'] = grouped_ratings.apply(lambda row: row['Weighted_Rating']/row['Similarity'], axis=1)
    grouped_ratings = grouped_ratings.reset_index()
    recommendations = pd.merge(grouped_ratings, ratings_data, on='Item_ID')
    recommendations = recommendations.loc[recommendations['User_ID'] != user_id]
    recommendations = recommendations.drop_duplicates(subset=['Item_ID'], keep='last')
    recommendations = recommendations.sort_values(by='Weighted_Rating', ascending=False)
    return recommendations.head(10)['Item_ID'].tolist()

# Generate recommendations for user 1
generate_recommendations(1)
