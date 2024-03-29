# -*- coding: utf-8 -*-
"""NLP Exp 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jq_YqSNXaamCqEKcQ5KrrC7q7HmfP-du

# **Aim: Feature Engineering of textual data using**
##**(a)	Bag of words (BoW)**
##**(b)	Feature Extraction with TF-IDF Vectorizer**

# **Step 1** Create a new python file.
"""

pip install numpy pandas scikit-learn

!pip install nltk
!pip install spacy

#Importing Libraries
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import spacy
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')

"""# **Step2**	Read input of texts and Pre-process text data"""

# Creating Sample data
dt = {'text': ['My Name is Tanish', 'My Last Name is Vaidya', 'My Roll Number is C 115!']}

# Createing a DataFrame
df = pd.DataFrame(dt)

df

"""# **Step 3** Extract features from text data."""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
df['tokens'] = df['text'].apply(word_tokenize)
df

# Step 5: Stemming
from nltk.stem import PorterStemmer, WordNetLemmatizer
stemmer = PorterStemmer()
df['stemmed_tokens'] = df['tokens'].apply(lambda tokens: [stemmer.stem(word) for word in tokens])
df

nltk.download('wordnet')

# Step 6: Lemmatization
from nltk.tokenize import word_tokenize
lemmatizer = WordNetLemmatizer()
df['lemmatized_tokens'] = df['tokens'].apply(lambda tokens: [lemmatizer.lemmatize(word) for word in tokens])
df

# Step 7: Joining tokens back to text
df['clean_text'] = df['lemmatized_tokens'].apply(lambda tokens: ' '.join(tokens))
df

# Converting to lowercase
df['text'] = df['text'].str.lower()
df

"""# **Step 4**	Implement Bag-of-Words Algorithm with Python"""

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(df)

feature_names = vectorizer.get_feature_names_out()

dense_array = X.toarray()

bow_representations = {}
for i, document in enumerate(df):
    bow_representations[f"Document {i+1}"] = dict(zip(feature_names, dense_array[i]))

for i, (doc, bow) in enumerate(bow_representations.items()):
     print(f"Bag-of-Words Representation for Document {i+1}: {bow}\n")

"""# **Step 5**	Create BoW model with Sklearn."""

vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(df['clean_text'])

bow_df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())

print("Bag-of-Words Representation:")
print(bow_df)

"""# **Step 6**	Python code to find the similarity measures."""

cosine_similarity_bow = cosine_similarity(bow_df)
print("\nCosine Similarity (Bag-of-Words):")
print(cosine_similarity_bow)

"""# **Observation and Learning:**
### Implementing Bag-of-Words and cosine similarity with Python, NLTK, and Scikit-learn provided a seamless approach for text feature extraction and similarity measurement, offering valuable insights into efficient natural language processing workflows.

# **Conclusion:**
### This hands-on experience in implementing Bag-of-Words and cosine similarity has strengthened my proficiency in text processing, showcasing the synergy between Python, NLTK, and Scikit-learn for effective natural language understanding and analysis.
"""

from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
one_hot_encoded = encoder.fit_transform(cosine_similarity_bow)

print("One-Hot Encoded Data:")
print(one_hot_encoded)

