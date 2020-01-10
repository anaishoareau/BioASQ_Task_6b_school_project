# -*- coding: utf-8 -*-

""" IMPORTS"""

from sklearn.preprocessing import normalize
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

""" CLASSIFICATION DEFINITION """

"""
The function classification takes in argument: X_train, y_train, X_test, y_test to train, classifier 
which are data to train and test a classifier with is name given with the 
classifier argument (a string in : "naive_bayes", "logistic_regression", 
"random_forest", "linear_svc"). 

This function returns the accuracy score, the precision score, 
the recall score, the f1-score and the classification report for the chosen classifier.
"""
            
def classification(X_train, y_train, X_test, y_test, classifier):
    
    if classifier == "naive_bayes":
        # Learning
        clf_naive_bayes = BernoulliNB()
        clf_naive_bayes = clf_naive_bayes.fit(X_train,y_train)
        
        # Prediction
        predicted = clf_naive_bayes.predict(X_test)

    elif classifier == "logistic_regression":
        # Learning
        clf_logistic_regression = LogisticRegression(solver = 'lbfgs', multi_class="multinomial", max_iter = 100000)
        clf_logistic_regression = clf_logistic_regression.fit(X_train,y_train)
        
        # Prediction
        predicted = clf_logistic_regression.predict(X_test)
        
    elif classifier == "random_forest":
        # Learning 
        classifier = RandomForestClassifier(n_estimators=1000, random_state=42)
        classifier.fit(X_train, y_train) 
        
        # Prediction
        predicted = classifier.predict(X_test)

    elif classifier == "linear_svc":
        #Normalization 
        X_train = normalize(X_train)
        X_test = normalize(X_test)
        
        param_grid_linear = {'C': [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30] }
        
        # Learning
        clf_svc_linear = GridSearchCV(LinearSVC(multi_class="crammer_singer", class_weight='balanced',  max_iter = 100000), param_grid_linear, iid=False, cv = 3)
        clf_svc_linear = clf_svc_linear.fit(X_train, y_train)
        
        # Prediction
        predicted = clf_svc_linear.predict(X_test)

    else:
        print("Classifier not found")
        return
    
    return (accuracy_score(y_test,predicted),
            precision_score(y_test,predicted, average = 'weighted'),
            recall_score(y_test,predicted, average = 'weighted'),
            f1_score(y_test,predicted, average = 'weighted'),
            classification_report(y_test,predicted, output_dict=True))
    

        
