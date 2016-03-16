import nltk
from nltk.corpus import wordnet as wn
import numpy as np
from gensim import corpora, models, similarities, matutils

def get_stopwords():
    """Returns a list of stop words. Currently uses a list of words in
    a text file

    """
    return read_data("englishstopwords-jc.txt")

def ideas_to_bow(raw_ideas):
    """Given text of ideas, convert to bag of words ("stems") representation
    """
    # draw from gensim, nltk
    # import all ideas, convert to "bag of words"
    # use porter stemming
    # apply stop words
    # apply frequency filter (in Toubia, f >= 5 for ideas, and f >= 10 for Google results)
    return None;