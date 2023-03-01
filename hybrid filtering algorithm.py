# hybrid filtering algorithm


import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load user-item ratings data
ratings = pd.read_csv('ratings.csv')

# Create user-item matrix
user_item_matrix = ratings.pivot_table(index='user_id', columns='item_id', values='rating')

# Calculate similarity matrix using cosine similarity
item_similarity_matrix = pd.DataFrame(cosine_similarity(user_item_matrix.T), index=user_item_matrix.columns, columns=user_item_matrix.columns)

# Define hybrid recommendation function
def hybrid_recommendation(user_id, top_n=10):
    # Get user's previous ratings
    user_ratings = ratings[ratings['user_id']==user_id]
    
    # Get average rating for each item
    item_avg_ratings = ratings.groupby('item_id')['rating'].mean().reset_index()
    
    # Filter out items that user has already rated
    unrated_items = item_avg_ratings[~item_avg_ratings['item_id'].isin(user_ratings['item_id'])]['item_id']
    
    # Calculate predicted ratings using both collaborative and content-based filtering
    item_similarity = item_similarity_matrix[user_ratings['item_id']].mean(axis=1)
    item_similarity = item_similarity[item_similarity.index.isin(unrated_items)]
    content_similarity = item_avg_ratings[item_avg_ratings['item_id'].isin(unrated_items)].set_index('item_id')['rating']
    predicted_ratings = (0.5 * item_similarity) + (0.5 * content_similarity)
    
    # Sort predicted ratings in descending order and return top N recommendations
    recommended_items = predicted_ratings.sort_values(ascending=False)[:top_n].index.tolist()
    return recommended_items
