"""
Date: 20230617

Data cleaning function
"""

import re 

from nltk.corpus import stopwords
from string import punctuation

def clean_text(text: str) -> str:
    """
    Clean the given sentence

    :params text that has to be cleaned 
    :type :str 

    :return: (str)
    """
    
    # Set to lowercase 
    clean_text = text.lower()

    # remove html tags 
    clean = re.compile('<.*?>')
    clean_text  = re.sub(clean, '', clean_text)    

    return clean_text


def remove_stopwords(sentence: str) -> str:
    """
    Remove all stop words in a sentence
    
    :params sentence to remove stopwords 
    :type :str 

    :return: (str)
    """

    stop_words     = stopwords.words('english')
    clean_sentence = ' '.join([ word for word in sentence.split() if word not in (stop_words) ])

    return clean_sentence

def remove_punct(sentence: str):
    """
    Remove Punctuation from a sentence

    :params sentence to remove stopwords 
    :type :str 

    :return: (str)    
    """
    clean_sentence = ' '.join([ token for token in sentence.split() if token not in (punctuation) ])

    return clean_sentence
