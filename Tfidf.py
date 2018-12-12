from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
#' And document first Is one second third this',
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(corpus)

print "get_feature_names:", vectorizer.get_feature_names()

print "len:", len(vectorizer.get_feature_names())

print "get_stop_words:", vectorizer.get_stop_words()

print "get_params:", vectorizer.get_params()

print x.shape

print "vocabulary:", vectorizer.vocabulary_

print "idf:", vectorizer.idf_

print x