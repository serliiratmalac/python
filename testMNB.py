from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

newsgroups_train = fetch_20newsgroups(subset='train')
categories = ['alt.atheism', 'talk.religion.misc',
              'comp.graphics', 'sci.space']

newsgroups_train = fetch_20newsgroups(subset='train',
                                      categories=categories)
vectorizer = TfidfVectorizer()
# the following will be the training data
vectors = vectorizer.fit_transform(newsgroups_train.data)
vectors.shape

newsgroups_test = fetch_20newsgroups(subset='test',
                                     categories=categories)
# this is the test data
vectors_test = vectorizer.transform(newsgroups_test.data)

clf = MultinomialNB(alpha=.01)

# the fitting is done using the TRAINING data
# Check the shapes before fitting
vectors.shape
#(2034, 34118)
newsgroups_train.target.shape
#(2034,)

# fit the model using the TRAINING data
clf.fit(vectors, newsgroups_train.target)

# the PREDICTION is done using the TEST data
pred = clf.predict(vectors_test)