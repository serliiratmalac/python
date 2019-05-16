import re
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer

def tokenize_sentences(sentences):
     words = []
     for sentence in sentences:
         w = extract_words(sentence)
         words.extend(w)
         
     words = sorted(list(set(words)))
     return words
 
def extract_words(sentence):
     ignore_words = ['a']
     words = re.sub("[^\w]", " ",  sentence).split() #nltk.word_tokenize(sentence)
     words_cleaned = [w.lower() for w in words if w not in ignore_words]
     return words_cleaned    
     
def bagofwords(sentence, words):
     sentence_words = extract_words(sentence)
     # frequency word count
     bag = np.zeros(len(words))
     for sw in sentence_words:
         for i,word in enumerate(words):
             if word == sw: 
                 bag[i] += 1
                 
     return np.array(bag)

 
sentences = ["Machine learning is great","Natural Language Processing is a complex field","Natural Language Processing is used in machine learning"]
vocabulary = tokenize_sentences(sentences)
bagofwords("Machine learning is great", vocabulary)
 
vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, max_features = 5000) 
train_data_features = vectorizer.fit_transform(sentences)
vectorizer.transform(["Machine learning is great"]).toarray()
