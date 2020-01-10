# -*- coding: utf-8 -*-

""" IMPORTS """

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from gensim.models import KeyedVectors
from word_2_vec import word_averaging_list
from preprocessing_tools import tokenize_text

""" VECTORIZATION DEFINITION """

""" 
The function vectorization takes in arguments:
    - X_train, X_test from a dataset
    - the name of a vectorization method in "tfidf","count","word2vec"
    
This function returns:
    - X_train vectorized
    - X_test vectorized       
"""

def vectorization(X_train, X_test, vectorizer):
    if vectorizer == "tfidf":
    # tfidfVectorizer
        tfidf = TfidfVectorizer(use_idf=True, ngram_range=(1, 3))
        X_train = tfidf.fit_transform(X_train)
        X_test = tfidf.transform(X_test)
    # countVectorizer
    elif vectorizer == "count":
        count = CountVectorizer(ngram_range=(1, 3))
        X_train = count.fit_transform(X_train)
        X_test = count.transform(X_test)
    # Word2vec
    elif vectorizer == "word2vec":
        
        wv = KeyedVectors.load_word2vec_format('./data_word2vec/pubmed2018_w2v_200D/pubmed2018_w2v_200D.bin', binary=True)
        
        wv.init_sims(replace=True)
        X_test = X_test.apply(lambda r: tokenize_text(r))
        X_train = X_train.apply(lambda r: tokenize_text(r))
        X_train = word_averaging_list(wv,X_train)
        X_test = word_averaging_list(wv,X_test)
    else:
        print("Vectorizer not found")
        return
    return(X_train, X_test)
