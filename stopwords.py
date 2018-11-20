import nltk
from nltk.corpus import stopwords

#nltk.download()
sw = stopwords.words("english")

print sw[0]

print sw[10]

print len(sw)

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

print stemmer.stem("responsiveness")

print stemmer.stem("responsivity")

print stemmer.stem("unresponsive")