# -*- coding: utf-8 -*-

""" IMPORTS """

import re
from nltk.tokenize import word_tokenize

""" PREPROCESSING FUNCTIONS """

# This function tokenize a text using NLTK tools
def tokenize_text(t):
    return word_tokenize(t)

# This function clean a text by deleting symbols and punctuation, by lowercase the text
def clean_text(t):
    return re.sub('~#|[.,?;*!%^£$@&_+():-\[\]{}]', '', 
                  t.replace('"', '').replace('/', '').replace('\\', '').replace("'",'').strip().lower())

# This function put a grammatical parsing information in a common 
# form for the unigram to trigrams generation.
def clean_parse_tree(t):
    return t.replace(' ',' - - - ').replace('/',' ')