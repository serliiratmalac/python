import re
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

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
    text = re.sub('[0-9]+',' ',text)
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
        verb = lemmatizer.lemmatize(w,pos='v')
        adj = lemmatizer.lemmatize(w,pos='a')
        noun = lemmatizer.lemmatize(w,pos='n')
        adv = lemmatizer.lemmatize(w,pos='r')
        
        if w != verb:
            lemma = lemma + " " + verb
        elif w != adj:
            lemma =  lemma + " " + adj
        elif w != noun:
            lemma = lemma + " " + noun
        elif w != adv:
            lemma = lemma + " " + adv
        else:
            lemma = lemma + " " + w
            
        
    lemma = re.sub(' +', ' ', lemma)
    lemma = lemma.lstrip() #dijadikan satu kalimat utuh bukan array of kata

    return lemma

def tokenize(string):
    word_tokens = word_tokenize(string)
    return word_tokens  



