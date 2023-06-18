
"""
Functions to calculate Tone using GT modifiers and dictionary list
Functions also to calculate the LM adjusted for negation

Date: 2023-06-17
"""


import glob
import os
import pandas as pd 
import PyPDF2


from nltk.tokenize import word_tokenize, sent_tokenize
from tqdm import tqdm
from typing import Dict, List 

# Own modules
from constants import NEGATION_WORDS



def count_tone_sentence(dict, doc):
    tone_score_list = []
    words_count_list = []
    haw_words = []
    dov_words = []
    pos_words = []
    neg_words = []

    sentences = sent_tokenize(doc.lower())
    sentences_count = len(sentences)

    for sentence in sentences:
        sentence_score = 0
        haw_count = 0
        dov_count = 0
        pos_count = 0
        neg_count = 0


        input_words = word_tokenize(sentence)
        input_words = [ w.lower() for w in input_words]

        words_count = len(input_words)

        words_count_list.append(words_count)

        for i in range(0, words_count):
            if input_words[i] in dict['hawkish']:
                haw_count += 1
                haw_words.append(input_words[i])
            if input_words[i] in dict['dovish']:
                dov_count += 1
                dov_words.append(input_words[i])
            if input_words[i] in dict['positive']:
                pos_count += 1
                pos_words.append(input_words[i])
            if input_words[i] in dict['negative']:
                neg_count += 1
                neg_words.append(input_words[i])

        if (words_count > 0): #and (haw_count != 0 and dov_count != 0):
            if haw_count > dov_count:
                if pos_count > neg_count:
                    sentence_score = 1
                    tone_score_list.append(sentence_score)
                elif pos_count == neg_count:
                    sentence_score = 0
                    tone_score_list.append(sentence_score)
                elif pos_count < neg_count:
                    sentence_score = -1
                    tone_score_list.append(sentence_score)
            elif haw_count == dov_count:
                if pos_count > neg_count:
                    sentence_score = 1
                    tone_score_list.append(sentence_score)
                elif pos_count == neg_count:
                    sentence_score = 0
                    tone_score_list.append(sentence_score)
                elif pos_count < neg_count:
                    sentence_score = -1
                    tone_score_list.append(sentence_score)
            elif haw_count < dov_count:
                if pos_count > neg_count:
                    sentence_score = -1
                    tone_score_list.append(sentence_score)
                elif pos_count == neg_count:
                    sentence_score = 0
                    tone_score_list.append(sentence_score)
                elif pos_count < neg_count:
                    sentence_score = 1
                    tone_score_list.append(sentence_score)
        else:
            sentence_score = 0
            tone_score_list.append(sentence_score)
        
    results = [100*sum(tone_score_list)/sentences_count, sentences_count, sum(words_count_list), haw_words, dov_words, pos_words, neg_words]
    return results




def check_negation(word: str) -> bool:
    """
    Check if the `word` is a negation

    :params word
    :type :str

    :return: (bool)
    """

    if word.lower() in NEGATION_WORDS:
        return True
    else:
        return False


def create_loughran_macdonald_dictionary(file: str) -> None:
    """
    Create the LM dictionary sentiment

    :params file is the path to the Loughran-McDonald Master Dictionary csv file
    :type :str
    """

    # Read file 
    lm = pd.read_csv(file)

    # Remove rows for words that don't appear
    lm.drop(lm[lm["Word Count"] <= 1 ].index, inplace=True)

    # Create a sentiment column
    lm['Sentiment'] = lm.apply(lambda row: 'negative' if row['Negative'] != 0 else ('positive' if row['Positive'] != 0 else 0), axis=1)

    # Drop words that have no sentiment
    lm.drop(lm[lm["Sentiment"] == 0].index, inplace=True)
    lm.reset_index(inplace=True)
    
    # Only keep `Word` and `Sentiment`
    lm_final = lm[['Word', 'Sentiment']]

    # Save the dictionary
    lm_final.to_csv("data/english_dictionary.csv", index=False)



def count_tone(sentiment: Dict[str, List[str]], content: str, negation_check: bool = True) -> List:
    """
    Count the tone in the content

    :params sentiment is the LM dictionary
    :type :Dict[str, List[str]]

    :params content 
    :type :str

    :params negation_check is if negation should be checked 
    :type :bool 

    :return: (List)
    """

    pos_count  = 0
    neg_count  = 0
    tone_score = 0
    net_sent   = 0

    pos_words  = []
    neg_words  = []

    input_words = word_tokenize(content)
    input_words = [ w.lower() for w in input_words]

    word_count = len(input_words)

    for i in range(0, word_count):
        if input_words[i] in sentiment['negative']:
            neg_count += 1
            neg_words.append(input_words[i])
        if input_words[i] in sentiment['positive']:
            if i >= 3:
                if check_negation(input_words[i - 1]) or check_negation(input_words[i - 2]) or check_negation(input_words[i - 3]):
                    neg_count += 1
                    neg_words.append(input_words[i] + ' (with negation)')
                else:
                    pos_count += 1
                    pos_words.append(input_words[i])
            elif i == 2:
                if check_negation(input_words[i - 1]) or check_negation(input_words[i - 2]):
                    neg_count += 1
                    neg_words.append(input_words[i] + ' (with negation)')
                else:
                    pos_count += 1
                    pos_words.append(input_words[i])
            elif i == 1:
                if check_negation(input_words[i - 1]):
                    neg_count += 1
                    neg_words.append(input_words[i] + ' (with negation)')
                else:
                    pos_count += 1
                    pos_words.append(input_words[i])
            elif i == 0:
                pos_count += 1
                pos_words.append(input_words[i])
 
    if word_count > 0:
        tone_score = 100 * (pos_count - neg_count) / word_count
        net_sent = pos_count - neg_count
    else:
        tone_score = 0
    
    results = [tone_score, word_count, pos_count, neg_count, net_sent, pos_words, neg_words]
 
    return results


def create_lm_sentiment(eng_sentiment: pd.DataFrame) -> Dict[str, List[str]]:
    """
    Create the Loughran and MacDonald sentiment dictionary

    :params eng_sentiment
    :type :pd.DataFrame

    :return: (Dict[str, List[str]])
    """

    eng_sentiment['Word'] = eng_sentiment['Word'].str.lower()
    sentiments            = eng_sentiment['Sentiment'].unique()

    return { s: eng_sentiment.loc[eng_sentiment['Sentiment']==s]['Word'].values.tolist() \
                        for s in sentiments}    
