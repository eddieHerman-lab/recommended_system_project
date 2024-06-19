import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity_matrices(rating_matrix, item_features):
    content_similarity = cosine_similarity(item_features)
    user_similarity = cosine_similarity(rating_matrix)
    return content_similarity, user_similarity

def recommend_items_collaborative(user_index, rating_matrix, user_similarity, num_recommendations=3):
    similar_users = user_similarity[user_index]
    weighted_sum = np.dot(similar_users, rating_matrix)
    sum_of_weights = np.abs(similar_users).sum()
    scores = weighted_sum / sum_of_weights
    already_rated = rating_matrix[user_index] > 0
    scores[already_rated] = -1
    recommended_items = np.argsort(scores)[::-1][:num_recommendations]
    return scores, recommended_items

def recommend_items_content(user_index, rating_matrix, content_similarity, num_recommendations=3):
    user_ratings = rating_matrix[user_index]
    scores = np.dot(content_similarity, user_ratings)
    already_rated = rating_matrix[user_index] > 0
    scores[already_rated] = -1
    recommended_items = np.argsort(scores)[::-1][:num_recommendations]
    return scores, recommended_items

def recommend_items_hybrid(user_index, rating_matrix, user_similarity, content_similarity, num_recommendations=3, alpha=0.5):
    collab_scores, _ = recommend_items_collaborative(user_index, rating_matrix, user_similarity, num_recommendations)
    content_scores, _ = recommend_items_content(user_index, rating_matrix, content_similarity, num_recommendations)
    hybrid_scores = alpha * collab_scores + (1 - alpha) * content_scores
    recommended_items = np.argsort(hybrid_scores)[::-1][:num_recommendations]
    return hybrid_scores, recommended_items

def recommend_items_popularity(rating_matrix, num_recommendations=3):
    item_popularity = np.sum(rating_matrix > 0, axis=0)
    popular_items = np.argsort(item_popularity)[::-1][:num_recommendations]
    return item_popularity, popular_items
