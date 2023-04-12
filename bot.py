import nltk
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Read the data from text file
data = pd.read_csv('data.txt', sep='\t', header=None, names=['query', 'response'])

# Step 2: Clean the data
data = data.drop_duplicates()
data = data.dropna()

# Create an instance of CountVectorizer
vectorizer = CountVectorizer(stop_words='english')

# Fit and transform the data
X = vectorizer.fit_transform(data['query']) 

# Step 3: Preprocess the data
nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('english'))
vectorizer = CountVectorizer(stop_words=stop_words)
X = vectorizer.fit_transform(data['query'])
y = data['response']


# Step 4: Train the chatbot
model = MultinomialNB()
model.fit(X, y)

# Step 5: Test the chatbot
query = "What is your name?"
X_test = vectorizer.transform([query])
response = model.predict(X_test)
print(response)

# Step 6: Iterate and improve the chatbot
# This could involve adding more data, experimenting with different preprocessing techniques, or trying out different machine learning algorithms.
