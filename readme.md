🎬 IMDB Review Sentiment Analysis

A machine learning project that analyzes text reviews and predicts whether the sentiment is Positive or Negative.

The project uses Natural Language Processing (NLP) techniques for text preprocessing and TF-IDF Vectorization to convert text into numerical features. A Logistic Regression model is then used to classify the sentiment.

📌 Project Overview

Sentiment Analysis is an NLP task used to determine the emotional tone of a piece of text.

In this project, a user can enter a movie review or any text, and the trained machine learning model predicts its sentiment.

Example
Input:
"This movie was absolutely amazing. I loved every scene."

Prediction:
Positive 😊
Input:
"The movie was boring and a complete waste of time."

Prediction:
Negative 😞
🚀 Features
Text-based sentiment prediction
NLP preprocessing
TF-IDF feature extraction
Logistic Regression classification
Streamlit web interface
Simple and user-friendly UI
Supports real-time predictions
🛠️ Technologies Used
Programming Language
Python
Libraries
Pandas
NumPy
Scikit-learn
NLTK
Streamlit
Matplotlib
Seaborn
Machine Learning
TF-IDF Vectorizer
Logistic Regression
📂 Project Structure
Sentiment-Analysis/
│
├── dataset/
│   └── sentiment_dataset.csv
│
├── model/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
└── .gitignore
🔄 Machine Learning Workflow

The project follows these major steps:

Dataset
   ↓
Data Cleaning
   ↓
Text Preprocessing
   ↓
Train/Test Split
   ↓
TF-IDF Vectorization
   ↓
Logistic Regression
   ↓
Model Evaluation
   ↓
Save Model
   ↓
Streamlit Deployment
🧹 Text Preprocessing

Before training the model, the text data is cleaned and prepared.

Typical preprocessing steps include:

Converting text to lowercase
Removing unnecessary characters
Removing punctuation
Removing stopwords
Handling extra spaces
Preparing text for vectorization

Example:

Original:
"This Movie Was AMAZING!!!"

After preprocessing:
"movie amazing"
🔢 TF-IDF Vectorization

TF-IDF stands for Term Frequency-Inverse Document Frequency.

It converts text into numerical vectors that can be understood by machine learning algorithms.

TF-IDF gives higher importance to words that are useful for distinguishing documents while reducing the importance of very common words.

Example:

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(text_data)
🤖 Model

The project uses Logistic Regression as the classification algorithm.

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

The model learns patterns from the training reviews and predicts the sentiment of new text.

📊 Model Evaluation

The model can be evaluated using metrics such as:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix

Example:

Accuracy: 86%

Replace the value above with your final test accuracy.

💾 Saving the Model

After training, the model and TF-IDF vectorizer can be saved using pickle or joblib.

Example:

import joblib

joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

These files can then be loaded during deployment.

🌐 Streamlit Application

The project includes a Streamlit interface that allows users to enter text and receive a sentiment prediction.

Run the application using:

streamlit run app.py

After running the command, Streamlit will provide a local URL where you can access the application.