import pandas as pd
import math
import numpy as np 
import re
import csv
import FSelection
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

data = pd.read_csv('Review1100Data.csv','r',delimiter=";")
#print(data)

review_array = np.array(data.Review)
#print (review_array)


#review_array = np.column_stack(data.Review)
#label_array = np.column_stack(data.Label)
#label_array = data_array[:,0]
#text = str(review_array[0])
##data_array.shape

#print (data_array[1])
#test = data_array[:,1]
#print (test)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"\'scuse", " excuse ", text)
    text = re.sub('\W', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip(' ')
    return text

def remove_punctuation(string): #fungsi remove punctuation
    punctuations = '''!()-[]{};:'+"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in string:
        if char not in punctuations:
            no_punct = no_punct + char #sudah bersih dari punctuation
    no_punct = re.sub(' +', ' ', no_punct)
    no_punct = no_punct.lstrip()
    return no_punct

def stopword_removal(string): #fungsi stopword
    stop_words = set(stopwords.words('english')) #menggunakan bahasa inggris

    # query = string
    #
    # querywords = query.split()
    #
    # resultwords = [word for word in querywords if word.lower() not in stop_words] #jika bukan stopword masukkan ke array resultwords
    # result = ' '.join(resultwords) #dari array menjadi kata utuh
    #
    # string = result

    # token
    word_tokens = word_tokenize(string)

    # define variable
    filtered_sentence = []
    filtered_string = ""

    # delete stopwords
    for w in word_tokens:
        if w not in stop_words: #jika bukan stopword masuk ke filtered sentence/kalimat sudah bersih dari stopword
            filtered_sentence.append(w)

    # assign set of non-stopword to string
    for subsets in filtered_sentence:
        filtered_string = filtered_string + " " + subsets #dari token berbentuk array menjadi kalimat utuh
    # delete first space
    filtered_string = filtered_string.lstrip()

    return filtered_string

def lemmatization(string): #fungsi lemmatization
    # assign input to local variable
    data = string

    # berupa token
    token = data.rsplit()

    # instance output variable
    lemma = ""

    # lemmatize
    lemmatizer = WordNetLemmatizer()
    for w in token:
        lemma = lemma + " " + lemmatizer.lemmatize(w) #fitur/kata dijadikan lemma
    lemma = re.sub(' +', ' ', lemma)
    lemma = lemma.lstrip() #dijadikan satu kalimat utuh bukan array of kata
    
def lemma(string):
    word_data = string
    nltk_tokens = nltk.word_tokenize(word_data)
#    for w in nltk_tokens:
#        print "Actual: %s  Lemma: %s"  % (w,wordnet_lemmatizer.lemmatize(w))
    return nltk_tokens
    
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

def func1(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total
    
#def tokenize_sentences(sentences):
#    words = []
#    w = sentences.split(" ")
#    words.extend(w)
#        
##    words = sorted(list(set(words)))
#    return words
#
#def bagofwords(sentence, words):
#    sentence_words = sentence.split()
#    bag = np.zeros(len(words))
#    for sw in sentence_words:
#        for i, word in enumerate(words):
#            if word == sw:
#                bag[i] += 1
#                
#    return np.array(bag)

i = 0
clean_array=[]
vocabulary=[]

while i <= len(review_array)-1:
    clean_ = clean_text(review_array[i])
    clean_remove = remove_punctuation(clean_)
#    print(clean_remove)
    clean_remove_stop = stopword_removal(clean_remove)
#    print(clean_remove_stop)
    clean_remove_stop_lemma = lemma(clean_remove_stop)
#    clean_remove_stop_lemma = lemmatization(clean_remove_stop)
#    print(clean_remove_stop_lemma)
    clean_array = np.append(clean_array, clean_remove_stop_lemma)
#    print(clean_array)
#    print (str(i) +" " + str(clean_text))
    i = i + 1
sentences = clean_array
vocabulary = tokenize_sentences(sentences)
# =============================================================================
# z = 0
# list_bow = list()
# while z < len(vocabulary): 
#     bow = bagofwords(vocabulary[z], clean_array)
#     
#     bow_min = -bow
#     bow_max = bow
#     bounds = list()
#     w = 0
#     #print(len(bow))
#     
#     while w < len(bow): 
#         bounds.append((bow_min[w], bow_max[w]))
#         #print(bounds)
#         w = w + 1
#     #print(len(bounds))
#     #bounds=[(-10,10),(-10,10),(-10,10)]
#     optim = FSelection.PSO.calculate('calculate',func1, bow, bounds, num_particles=15, maxiter=30, verbose=True)
#     nilai_pso = sum(optim)
#     list_bow.append(nilai_pso)
# #    with open('optim.csv', 'w') as writeFile:
# #        writer = csv.writer(writeFile)
# #        writer.writerows(list_bow)
#     z = z+1
# =============================================================================
# =============================================================================
# print (vocabulary)
# print (str(clean_array[10]) + " " + str(bow))
# print(list_bow)
# =============================================================================


