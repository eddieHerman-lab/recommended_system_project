import numpy as np
from src.recommender import calculate_similarity_matrices, recommend_items_collaborative, recommend_items_content, recommend_items_hybrid, recommend_items_popularity
from src.visualization import plot_similarity_matrix, plot_recommendations

# Exemplo de matrizes
rating_matrix = np.array([
    [4, 0, 0, 5, 1, 0, 0],
    [5, 5, 4, 0, 0, 0, 0],
    [0, 0, 0, 2, 4, 5, 0],
    [0, 3, 0, 0, 0, 0, 3],
])

item_features = np.array([
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1],
])

# Calcular similaridades
content_similarity, user_similarity = calculate_similarity_matrices(rating_matrix, item_features)

# Recomendação para o usuário de índice 0
user_index = 0

collab_scores, recommended_items_collab = recommend_items_collaborative(user_index, rating_matrix, user_similarity)
content_scores, recommended_items_content = recommend_items_content(user_index, rating_matrix, content_similarity)
hybrid_scores, recommended_items_hybrid = recommend_items_hybrid(user_index, rating_matrix, user_similarity, content_similarity)
popularity_scores, recommended_items_popularity = recommend_items_popularity(rating_matrix)

# Imprimir recomendações híbridas e populares
print('Hybrid Recommendations for user:', recommended_items_hybrid)
print('Popularity-based Recommendations:', recommended_items_popularity)

# Plotar visualizações
plot_similarity_matrix(content_similarity)
plot_recommendations(collab_scores, content_scores, hybrid_scores, popularity_scores)
