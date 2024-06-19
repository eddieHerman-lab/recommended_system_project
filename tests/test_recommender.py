import unittest
import numpy as np
from src.recommender import calculate_similarity_matrices, recommend_items_collaborative, recommend_items_content, \
    recommend_items_hybrid, recommend_items_popularity


class TestRecommender(unittest.TestCase):

    def setUp(self):
        self.rating_matrix = np.array([
            [4, 0, 0, 5, 1, 0, 0],
            [5, 5, 4, 0, 0, 0, 0],
            [0, 0, 0, 2, 4, 5, 0],
            [0, 3, 0, 0, 0, 0, 3],
        ])

        self.item_features = np.array([
            [1, 0, 0, 1],
            [0, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [1, 1, 1, 1],
        ])

        self.content_similarity, self.user_similarity = calculate_similarity_matrices(self.rating_matrix,
                                                                                      self.item_features)

    def test_recommend_items_collaborative(self):
        scores, recommended_items = recommend_items_collaborative(0, self.rating_matrix, self.user_similarity)
        self.assertEqual(len(recommended_items), 3)

    def test_recommend_items_content(self):
        scores, recommended_items = recommend_items_content(0, self.rating_matrix, self.content_similarity)
        self.assertEqual(len(recommended_items), 3)

    def test_recommend_items_hybrid(self):
        scores, recommended_items = recommend_items_hybrid(0, self.rating_matrix, self.user_similarity,
                                                           self.content_similarity)
        self.assertEqual(len(recommended_items), 3)

    def test_recommend_items_popularity(self):
        item_popularity, popular_items = recommend_items_popularity(self.rating_matrix)
        self.assertEqual(len(popular_items), 3)


if __name__ == '__main__':
    unittest.main()
