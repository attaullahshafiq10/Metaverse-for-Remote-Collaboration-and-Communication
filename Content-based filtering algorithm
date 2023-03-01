# Content-based filtering algorithm


# Import libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load item data
item_data = pd.read_csv('items.csv')

# Compute item-item similarity matrix
tfidf = TfidfVectorizer(stop_words='english')
item_data['Item_Description'] = item_data['Item_Description'].fillna('')
tfidf_matrix = tfidf.fit_transform(item_data['Item_Description'])
item_similarity = cosine_similarity(tfidf_matrix)

# Generate recommendations for a user
def generate_recommendations(user_id):
    user_items = ratings_data.loc[ratings_data['User_ID'] == user_id, 'Item_ID']
    item_similarities = np.zeros(item_similarity.shape[0])
    for item in user_items:
        item_similarities += item_similarity[item-1]
    item_similarities = pd.Series(item_similarities, index=item_data.index)
    item_similarities = item_similarities.sort_values(ascending=False)
    top_items = item_similarities.head(10).index.tolist()
    return top_items

# Generate recommendations for user 1
generate_recommendations(1)
