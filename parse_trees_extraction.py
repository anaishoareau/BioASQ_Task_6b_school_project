# -*- coding: utf-8 -*-

""" IMPORTS """

import os
import pandas as pd
from nltk.parse.stanford import StanfordParser

""" StanfordParser LOADING """

java_path = r'C:\Program Files\Java\jdk-13.0.1\bin\java.exe'
os.environ['JAVAHOME'] = java_path

scp = StanfordParser(path_to_jar='./stanford-corenlp-full-2018-10-05/stanford-corenlp-3.9.2.jar',
                     path_to_models_jar='./stanford-corenlp-full-2018-10-05/stanford-corenlp-3.9.2-models.jar')
    
""" DATASET LOADING """

dataset = pd.read_csv('./data/questions.csv')
dataset.insert(2,'parse_tree',"")

""" GRAMMATICAL PARSING INFORMATION EXTRACTION """

#This fuction delete symbols from a sentence (except end-sentence punctuation)
def delete_symbols(sentence):
    no_symbol = ""
    for char in sentence:
       if char not in '''"()-[]{};:\,<>/@#$%^&*_~''': 
           no_symbol += char
    return(no_symbol)

# This fuction generate grammatical parsing information from a sentence
# and return it in a string format like ths one: "SQ VBZ/NP/NP/. NNP/NN NP/CC/NP DT/NN DT/JJ/NN"
def parse_tree_generator(sentence):          
    parse_tree = list(scp.raw_parse(delete_symbols(sentence)))
    t = parse_tree[0]
    clean_parse = []
    for k in range(len(t.productions())):
        for p in range(len(str(t.productions()[k]))):
            if str(t.productions()[k])[p] == '>' and str(t.productions()[k])[p+2] != "'":
                clean_parse.append(str(t.productions()[k])[p+2::].replace(" ","/"))
                break
    return " ".join(clean_parse)

""" NEW INFORMATION WRITING """

# Apply the parse_tree_generator to our dataset
dataset['parse_tree'] = dataset['question'].apply(lambda x: parse_tree_generator(x))

# Save the result
dataset.to_csv('./data/parsed_data.csv', index = False)
