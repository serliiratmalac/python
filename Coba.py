import pandas as pd
import numpy as np
import Preprocessing as p
from sklearn.feature_extraction.text import CountVectorizer

print("-----PROSES READ DATA-----")
data_fileName = "./DataReview100.csv"
data = pd.read_csv(data_fileName,'r',delimiter=";")
review_array = np.array(data.Review)
print(data)

print("-----PROSES PREPROCESSING-----")
i = 0
clean_array=[]
clean_remove_stop_token_array = []

while i <= len(review_array)-1:
    clean_ = p.clean_text(review_array[i])
    clean_remove = p.remove_punctuation(clean_)
    clean_remove_stop = p.stopword_removal(clean_remove)
    clean_remove_stop_token = p.tokenize(clean_remove_stop)
    
#    clean_remove_stop_array = np.append(clean_remove_stop_array,clean_token)
    clean_remove_stop_token_array.append(clean_remove_stop_token)
    
    clean_remove_stop_token_lemma = p.lemmatization(clean_remove_stop)
    clean_token_lemma = p.tokenize(clean_remove_stop_token_lemma)
    
#    clean_array = np.append(clean_array, clean_token_lemma)
    clean_array.append(clean_token_lemma)
    i = i + 1
    print(clean_remove_stop_token_array)
    print(clean_array)

 
print("-----PROSES FITUR EXTRACTION-----")

corpus = ['find', 'store', 'skin', 'fair', 'use', 'white', 'conceler', 'highlight', 'perfect']

 
 
vectorizer = CountVectorizer()
print( vectorizer.fit_transform(corpus).todense() )
print( vectorizer.vocabulary_ )


