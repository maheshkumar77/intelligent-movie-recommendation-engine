import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
movies = pd.read_csv("/movie.csv")
tags = pd.read_csv("/genome_tags.csv")
scores = pd.read_csv("/genome_scores.csv")
print(movies.shape, tags.shape, scores.shape)
scores.drop_duplicates(inplace=True)
movies.drop_duplicates(inplace=True)
print(scores.isnull().sum())
scores.dropna(inplace=True)
scores = scores[scores['relevance'] > 0.2]
scores = scores.merge(tags, on='tagId')
tag_data = scores.groupby('movieId')['tag'].apply(lambda x: " ".join(x))

tfidf = TfidfVectorizer(
    max_features=5000,   # tuning parameter
    stop_words='english'
)

tfidf_matrix = tfidf.fit_transform(tag_data)
svd = TruncatedSVD(n_components=100)  # tuning parameter
reduced_matrix = svd.fit_transform(tfidf_matrix)
similarity = cosine_similarity(reduced_matrix)
movie_ids = tag_data.index.tolist()
movie_index = {id: i for i, id in enumerate(movie_ids)}

def recommend(movie_id, top_n=5):
    idx = movie_index[movie_id]

    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_movies = sim_scores[1:top_n+1]

    return [movie_ids[i[0]] for i in top_movies]
    def recommend_by_name(movie_name):
    match = movies[movies['title'].str.contains(movie_name, case=False)]

    if match.empty:
        return "Movie not found. Please check the name."

    movie_id = match.iloc[0]['movieId']

    rec_ids = recommend(movie_id)

    return movies[movies['movieId'].isin(rec_ids)]['title']
    recommend_by_name("father bride")