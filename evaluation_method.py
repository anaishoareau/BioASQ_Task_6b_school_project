# -*- coding: utf-8 -*-

""" IMPORTS """

from sklearn.model_selection import train_test_split
from classification import classification
from vectorization import vectorization

""" EVALUATION METHODS """

"""
The function train_test_split_repeat takes in argument:
    - a dataset
    - a classifier name in "naive_bayes", "logistic_regression", "random_forest", "linear_svc"
    - a vectorizer name in "tfidf","count","word2vec"
    - a mode name in "question", "question+parse_tree"
    - a repetition number

This function returns:
    -an averaged accuracy score over all the repetitions
    -an averaged precision score over all the repetitions
    -an averaged recall score over all the repetitions
    -an averaged f1-score score over all the repetitions
    -an averaged classification report over all the repetitions

It uses the classification fonction from classification.py and the 
vectorization function from vectorization.py to generate the results 
of the chosen classifier over the provided data.

"""

def train_test_split_repeat(dataset, classifier, vectorizer, mode, n_repeat):
    
    X_train, X_test, y_train, y_test = train_test_split(dataset[mode], 
                                                        dataset["question_type"], 
                                                        test_size=0.2, shuffle = True, 
                                                        stratify = dataset["question_type"])
    accuracy_scores = []
    precision_scores = []
    recall_scores = []
    f1_scores = []
    reports = []
    
    for k in range(n_repeat):
        
        X_train, X_test, y_train, y_test = train_test_split(dataset[mode], 
                                                        dataset["question_type"], 
                                                        test_size=0.2, shuffle = True, 
                                                        stratify = dataset["question_type"])

        X_train, X_test = vectorization(X_train, X_test, vectorizer)
        acc, precision, recall, f1, classification_report = classification(X_train, y_train, X_test, y_test, classifier)
        reports.append(classification_report)
        accuracy_scores.append(acc)
        precision_scores.append(precision)
        recall_scores.append(recall)
        f1_scores.append(f1)
        
    accuracy_score = sum(accuracy_scores)/len(accuracy_scores)
    precision_score = sum(precision_scores)/len(precision_scores)
    recall_score = sum(recall_scores)/len(recall_scores)
    f1_score = sum(f1_scores)/len(f1_scores)
    avg_report = avg_classification_report(reports)
    
    return accuracy_score, precision_score, recall_score,f1_score, avg_report


""" The function avg_classification_report generate an averaged classification 
report from a list of classification reports.  
"""

def avg_classification_report(reports):
    avg = {"factoid":{},"list":{},"summary":{},"yesno":{}}
    labels = ["factoid","list","summary","yesno"]
    ind = ['precision','recall','f1-score','support']
    for l in labels:
        for i in ind:
            total = 0
            for report in reports:
                total += report[l][i]
            total = total / len(reports)
            avg[l][i] = total
    return avg
            
