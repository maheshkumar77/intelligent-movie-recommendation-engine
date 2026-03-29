# 🎬 Movie Recommender System (TF-IDF + SVD)

An intelligent content-based movie recommendation system built using Machine Learning techniques like **TF-IDF vectorization** and **cosine similarity**, optimized with **dimensionality reduction (SVD)**.

---

## 🚀 Features

* Recommend similar movies based on content (tags)
* Uses **TF-IDF** for better feature representation
* Optimized using **Truncated SVD**
* Fast similarity search
* Clean and scalable architecture
* Ready for deployment with Flask API

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Flask (for API)
* TF-IDF Vectorizer
* Cosine Similarity
* Truncated SVD

---

## 📂 Dataset

* MovieLens Dataset
* genome_scores.csv
* genome_tags.csv
* movies.csv

---

## ⚙️ How It Works

1. Data cleaning and preprocessing
2. Tag relevance filtering
3. Feature engineering using TF-IDF
4. Dimensionality reduction using SVD
5. Cosine similarity computation
6. Recommendation generation

---

## 📊 Example

Input:
Movie: Toy Story (1995)

Output:

* Toy Story 2 (1999)
* A Bug's Life (1998)
* Monsters, Inc. (2001)

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/movie-recommender-tfidf-svd.git
cd movie-recommender-tfidf-svd
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
python app.py
```

---

## 📡 API Usage

```bash
GET /recommend?movie=Toy Story (1995)
```

---

## 📈 Future Improvements

* Add collaborative filtering (hybrid system)
* Integrate TMDB API for posters
* Deploy on cloud (AWS / Render)
* Add user-based personalization

---

## 👨‍💻 Author

Mahesh Kumar Sahu

---

## ⭐ Why This Project?

This project demonstrates:

* Strong ML fundamentals
* Feature engineering skills
* Optimization techniques
* Real-world deployment capability
