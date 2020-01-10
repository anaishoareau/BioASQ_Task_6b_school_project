# BioASQ_Task_6b_school_project
 
This laboratory takes place in the BioAsq challenge context. This challenge is about biomedical semantic indexing and question answering (QA). It includes tasks relevant to hierarchical text classification, machine learning, information retrieval, QA from texts and structured data, multi-document summarization and many other areas.

In this laboratory case, we will focus on the task 6b, which is about biomedical semantic QA. Indeed, we will use given dataset containing questions and reference answers for the training.

In this way, the objective of this laboratory case is to write a multiclass classifier for classifying questions into one of the four question type : Factoid, list, summary and yes/no, using an adapted text preprocessing.

## Project content and indications

### Folders

* data:

Questions.xlsx : original data file

questions.csv : file generated with the original file but in CSV format 
(columns: question, question_type)

parsed_data.csv : file generated with the questions.csv content completed 
by the grammatical parsing information (colums: question,parse_tree,question_type)

* data_word2vec: 

#### WARNING : Needs to contain model for word embeddings (pre-trained on biomedical data)

Downoald https://archive.org/download/pubmed2018_w2v_200D.tar/pubmed2018_w2v_200D.tar.gz, unzip the folder and add it to the data_word2vec folder of the project 

This model was found on : http://nlp.cs.aueb.gr/software.html

This project corresponds to english word embeddings pre-trained on biomedical texts from MEDLINE®/PubMed® Baseline 2018 using the Word2Vec implementation of the gensim toolkit. It was created by AUEB's NLP group: http://nlp.cs.aueb.gr/.

* stanford-corenlp-full-2018-10-05 : 

#### WARNING : Needs to contain the StanfordCoreNLP tools

Downoald http://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip , unzip the folder and add its content to the stanford-corenlp-full-2018-10-05 folder of the project. 

This model was found on : https://stanfordnlp.github.io/CoreNLP/

### Files

* dataset_presentation.py: 

Lauch to have the presentation of the dataset

* parse_trees_extraction.py: 

Generate the parsed_data.csv file to have the grammatical parsing information of 
all the dataset

* classification.py:

Contains function for classifying text (4 different classifier are proposed)

classification(X_train, y_train, X_test, y_test, classifier)

* vectorization.py: 

Contains function for vectorizing text (3 different vectorization methods are proposed)

vectorization(X_train, X_test, vectorizer)

* word_2_vec.py:

Contains function to allow word embedding vectorization

word_averaging(wv, words)
word_averaging_list(wv, text_list)

* evaluation_method.py:

Contains function to apply our evaluation method: do n times 
the classification for all differents models and returns its averaged results

train_test_split_repeat(dataset, classifier, vectorizer, mode, n_repeat)

* preprocessing_tools.py:

Contains preprocessing fuctions to simplify vectorization

tokenize_text(text)

clean_text(text)

clean_parse_tree(text)

* main.py :

Lauch the classification and give the result of each model 
