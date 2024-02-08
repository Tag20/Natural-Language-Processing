# -*- coding: utf-8 -*-
"""C106_NLP_Exp1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KTu5I_EehM_5HXX-pilko2rUbI8nVJd0


# **Question 1: Study of SpaCy and NLTK**

# NLTK:

NLTK: Natural Language Toolkit
Overview: Comprehensive NLP library in Python.
Features: Tokenization, stemming, lemmatization, part-of-speech tagging.
Usage: Common in education, research, and basic NLP tasks.
Strengths: Versatile, rich corpora for linguistic research.


# spaCy:

Overview: Modern, fast, efficient NLP library.
Features: Speed, pre-trained models, advanced tasks (NER, dependency parsing).
Usage: Ideal for production, high-performance environments.
Strengths: Exceptional tokenization, named entity recognition.
Choosing:

NLTK: Education, basic tasks.
spaCy: Production, speed, complex NLP tasks.
Conclusion:

NLTK for versatility and education.
spaCy for speed, efficiency, and advanced tasks.

# **Question 2:	Download and install SpaCy for Jupyter notebook**
"""

!pip install spacy

"""# **Question 3:	Web scrapping for text data using beautiful soup**"""

from bs4 import BeautifulSoup
#import libraries
import requests

"""## From URL getting the HTML content and extracting all the images"""

# website url to get the HTML content
url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"

result = requests.get(url_link).text
doc = BeautifulSoup(result, "html.parser")

for item in doc.find_all('img'):
  print(item['src'])

# extracting the whole content from the website
res = doc.find(id = "content")
print(res)

heading = res.find(class_ = "firstHeading")
print(heading)

print(heading.text)

"""##Extracting the list of countries and their population from the table


"""

my_table=doc.find("table", class_= "wikitable sortable plainrowheaders")

th_tags = my_table.find_all('th')
names = []
for elem in th_tags:
  #finding the <a> tag
  a_links = elem.find_all("a")
# getting the text insid the <a> tag
  for i in a_links:
    names.append(i.string)
print(names)

"""##Creating a final list of countries and their population"""

final_list = names[9: ]
states = []
for str in final_list:
  if len(str) > 3:
    states.append(str)
print(states)

divs = my_table.find_all("div")
population = []
for i in divs:
  population.append(i.string)
print(population)

pop_final = []
for i in population:
  if len(i) > 3:
    pop_final.append(i)

print(pop_final)

"""##Using pandas library for showcasing the list of countries and population"""

import pandas as pd

#read from html using pd
df = pd.DataFrame()

df['state'] = states

df['population'] = pop_final

print(df)
