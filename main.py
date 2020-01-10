# -*- coding: utf-8 -*-

""" IMPORTS """

import pandas as pd
from sklearn.utils import shuffle
from preprocessing_tools import clean_text, clean_parse_tree
from evaluation_method import train_test_split_repeat

""" LOADING DATASET """

dataset = pd.read_csv('./data/parsed_data.csv')

""" COMMON FORM GENERATION FOR UNIGRAM TO TRIGRAMS """

dataset.insert(3,'question+parse_tree',"")

dataset['question'] = dataset['question'].apply(lambda x: clean_text(x))
dataset['parse_tree'] = dataset['parse_tree'].apply(lambda x: clean_parse_tree(x))
dataset['question+parse_tree'] = dataset[['question', 'parse_tree']].apply(lambda x: ' '.join(x), axis = 1)

""" ANALYZE """

# We shuffle the dataset on time at the begining 
dataset = shuffle(dataset)

# Variables
classifiers = ["naive_bayes", "logistic_regression", "random_forest", "linear_svc"]
vectorizers = ["tfidf","count","word2vec"]
modes = ["question", "question+parse_tree"]
n = 10

# Analyze
for mode in modes:
    for vectorizer in vectorizers:
        for classifier in classifiers:
            print("\nCase:", classifier, vectorizer, mode)
            ttsr = train_test_split_repeat(dataset, classifier, vectorizer, mode, n)
            print("\nAveraged accuracy score:", ttsr[0])
            print("\nAveraged precision score:", ttsr[1])
            print("\nAveraged recall score:", ttsr[2])
            print("\nAveraged f1 score:", ttsr[3])

            print("\nAveraged classification report:")
            avg_report = pd.DataFrame(ttsr[4])
            print(avg_report)