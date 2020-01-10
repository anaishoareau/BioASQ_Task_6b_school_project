# BioASQ_Task_6b_school_project
 
FOLDERS:

* data:

- Questions.xlsx : original data file
- questions.csv : file generated with the original file but in CSV format 
(columns: question, question_type)
- parsed_data.csv : file generated with the questions.csv content completed 
by the grammatical parsing information (colums: question,parse_tree,question_type)

* data_word2vec: 

Contains biomedical data for training the neural network of the word embedding

* stanford-corenlp-full-2018-10-05 : 

StanfordCoreNLP tools provide by 
https://stanfordnlp.github.io/CoreNLP/


FILES:

* dataset_presentation.py: 

Lauch to have the presentation of the dataset

* parse_trees_extraction.py: 

Generate the parsed_data.csv file to have the grammatical parsing information of 
all the dataset

* classification.py:

Contains function for classifying text (4 different classifier are proposed)
- classification(X_train, y_train, X_test, y_test, classifier)

* vectorization.py: 

Contains function for vectorizing text (3 different vectorization methods are proposed)
- vectorization(X_train, X_test, vectorizer)

* word_2_vec.py:

Contains function to allow word embedding vectorization
- word_averaging(wv, words)
- word_averaging_list(wv, text_list)

* evaluation_method.py:

Contains function to apply our evaluation method: do n times 
the classification for all differents models and returns its averaged results
- train_test_split_repeat(dataset, classifier, vectorizer, mode, n_repeat)

* preprocessing_tools.py:

Contains preprocessing fuctions to simplify vectorization
- tokenize_text(t)
- clean_text(t)
- clean_parse_tree(t)

* main.py :

Lauch the classification and give the result of each model 
