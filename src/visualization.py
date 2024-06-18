import matplotlib.pyplot as plt

def plot_similarity_matrix(content_similarity):
    plt.imshow(content_similarity, cmap='viridis')
    plt.colorbar()
    plt.title('Similarity Matrix between items')
    plt.xlabel('Items')
    plt.ylabel('Items')
    plt.show()

def plot_recommendations(collab_scores, content_scores, hybrid_scores, popularity_scores):
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.bar(range(len(collab_scores)), collab_scores, color='blue')
    plt.title('Collaborative Recommendations')
    plt.xlabel('Items')
    plt.ylabel('Score')
    plt.xticks(range(len(collab_scores)), ['Item ' + str(i+1) for i in range(len(collab_scores))], rotation=45)

    plt.subplot(2, 2, 2)
    plt.bar(range(len(content_scores)), content_scores, color='green')
    plt.title('Content-based Recommendations')
    plt.xlabel('Items')
    plt.ylabel('Score')
    plt.xticks(range(len(content_scores)), ['Item ' + str(i+1) for i in range(len(content_scores))], rotation=45)

    plt.subplot(2, 2, 3)
    plt.bar(range(len(hybrid_scores)), hybrid_scores, color='purple')
    plt.title('Hybrid Recommendations')
    plt.xlabel('Items')
    plt.ylabel('Score')
    plt.xticks(range(len(hybrid_scores)), ['Item ' + str(i+1) for i in range(len(hybrid_scores))], rotation=45)

    plt.subplot(2, 2, 4)
    plt.bar(range(len(popularity_scores)), popularity_scores, color='orange')
    plt.title('Popularity-based Recommendations')
    plt.xlabel('Items')
    plt.ylabel('Popularity')
    plt.xticks(range(len(popularity_scores)), ['Item ' + str(i+1) for i in range(len(popularity_scores))], rotation=45)

    plt.tight_layout()
    plt.show()
