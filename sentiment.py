"""
All the sentiment functions
Date: 2023-06-17
"""

import json 
import numpy as np
import pandas as pd 

from afinn import Afinn
from flair.models import TextClassifier
from flair.nn import Classifier
from flair.data import Sentence
from nltk import tokenize
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from progress.bar import Bar
from textblob import TextBlob
from tqdm import tqdm
from typing import List 

# Own modules
from cleaning import clean_text



def get_flair_scores(df: pd.DataFrame, fast: bool=False) -> pd.DataFrame:
    """
    Calculate the Flair scores

    :params df is the dataframe
    :type :pd.DataFrame

    :params fast is boolean for which model to use 
    :type :bool 

    :return: (pd.DataFrame)     
    """
    scores         = [] 

    # Load the classifier 
    if fast:
         classifier     = Classifier.load('sentiment-fast')
    else:
        classifier     = TextClassifier.load('en-sentiment')
    
    # Tokenize docs to sentences 
    doc_sentences  =  [ sent_tokenize(doc)  for doc in df['Content']]

    # Calculate the scores 
    if fast:
        bar    = Bar("Calculating Flair Fast sentiment scores...", max=len(doc_sentences))
    else:
        bar    = Bar("Calculating Flair sentiment scores...", max=len(doc_sentences))

        
    for sentences in doc_sentences:
        pos_score = []
        neg_score = []
        for s in sentences:
            sentence = Sentence(s)
            classifier.predict(sentence)
            pred_value = sentence.get_label().value.lower()

            if pred_value == "negative":
                neg_score.append(1)
            elif pred_value == "positive":
                pos_score.append(1)


        score = (sum(pos_score) - sum(neg_score))/(sum(pos_score) + sum(neg_score))
        scores.append(score)
        bar.next()
    bar.finish()

    if fast:
        df['flair_fast_scores'] = scores
    else:
        df['flair_scores'] = scores 

    return df 

def get_textblob_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the scores using Textblob

    :params df is the dataframe
    :type :pd.DataFrame

    :return: (pd.DataFrame) 
    """

    scores            = [ TextBlob(review).sentiment.polarity for review in tqdm(df['Content'], desc="Calculating TextBlob scores...")] 
    df['blob_scores'] = scores

    return df     

def calculate_scores(doc_words: List[List[str]], positive: List[str], negative: List[str], bar: Bar) -> List[float]:
    """
    Calculate the scores based on the positive and negative word list 

    :params doc_words is a List of List that has words for each document
    :type :List[List[str]]

    :params positive is a word list of positive words 
    :type :List[str]

    :params negative is a word list of negative words
    :type :List[str]

    :params bar is the progress bar object
    :type :Bar

    :return: (List[float]) 
    """
    scores = []
    for words in doc_words:
        pos_score = []
        neg_score = []
        for word in words:
            if word.lower() in positive:
                pos_score.append(1)
            elif word.lower() in negative:
                neg_score.append(1)

        score = (sum(pos_score) - sum(neg_score))/(sum(pos_score) + sum(neg_score))
        scores.append(score)
        bar.next()
    bar.finish()

    return scores 

def get_bing_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the Bing scores 

    :params df is the dataframe
    :type :pd.DataFrame

    :return: (pd.DataFrame)   
    """

    positive = pd.read_csv("data/bing_positive.csv")['Positive'].tolist()
    negative = pd.read_csv("data/bing_negative.csv")['Negative'].tolist()

    # Tokenize each document
    doc_words = [ word_tokenize(doc)  for doc in df['Content']]  

    # Calculate the scores
    bar    = Bar("Calculating Bing scores...", max=len(df))
    scores = calculate_scores(doc_words, positive, negative, bar)
    df["bing_scores"] = scores 
    return df 


def get_general_inquirer_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the General Inquirer scores

    :params df is the dataframe
    :type :pd.DataFrame

    :return: (pd.DataFrame)
    """

    # Read in the General Inquirer Dictionary
    gi = pd.read_csv("data/general_inquirer.csv")

    # Keep only the entry, positive and negative columns 
    gi = gi[["Entry","Positiv","Negativ"]]

    # Set entry to lowercase
    gi["Entry"] = gi["Entry"].apply(lambda x: x.lower())

    # Get the positive and negative word lists
    positive    = gi.loc[gi["Positiv"]=="Positiv", "Entry"].tolist()
    negative    = gi.loc[gi["Negativ"]=="Negativ", "Entry"].tolist()
   
     # Tokenize each document
    doc_words = [ word_tokenize(doc)  for doc in df['Content']]  

    # Calculate the scores
    bar    = Bar("Calculating General Inquirer scores...", max=len(df))
    scores = calculate_scores(doc_words, positive, negative, bar)
    df["gi_scores"] = scores 
    return df    


def get_mpqa_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the MPQA Subjectivity scores

    :params df is the dataframe
    :type :pd.DataFrame

    :return: (pd.DataFrame)
    """

    mpqa     = pd.read_csv("data/lexicon_easy.csv")
    positive = mpqa.loc[mpqa["sign"]==1, "word"].tolist()
    negative = mpqa.loc[mpqa["sign"]==-1, "word"].tolist()
    
    # Tokenize each document
    doc_words = [ word_tokenize(doc)  for doc in df['Content']]  

    # Calculate the scores
    bar    = Bar("Calculating MPQA Subjectivity scores...", max=len(df))
    scores = calculate_scores(doc_words, positive, negative, bar)
    df["mpqa_scores"] = scores 
    return df       

def get_nrc_scores(df: pd.DataFrame) -> pd.DataFrame:
    """"
    Calculate the NRC Emotions Lexicon scores

    :params df is the dataframe
    :type :pd.DataFrame

    :return: (pd.DataFrame)   
    """

    # Read in the NRC Emotions Lexicon    
    with open("data/nrc_en.json", 'r') as f:
        nrc = json.load(f)

    # Get the negative and positive words
    positive = []
    negative = [] 

    for key, value in nrc.items():
        if 'positive' in value:
            positive.append(key)
        elif 'negative' in value:
            negative.append(key)

    # Tokenize each document
    doc_words = [ word_tokenize(doc)  for doc in df['Content']]  

    # Calculate the scores
    bar    = Bar("Calculating NRC Lexicon scores...", max=len(df))
    scores = calculate_scores(doc_words, positive, negative, bar)
    df["nrc_scores"] = scores 
    return df  


def get_lm_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the Loughran and MacDonald Scores 

    :params df is the dataframe
    :type :pd.DataFrame

    :return: (pd.DataFrame)
    """

    # Read in the cleaned Loughran and MacDonald Dictionary
    eng_sentiment = pd.read_csv("data/english_dictionary.csv")

    # Make the sentiment words to lowercase 
    eng_sentiment['Word'] = eng_sentiment['Word'].apply(lambda x: x.lower())
    
    # Create the positive and negative lists 
    positive  = eng_sentiment.loc[eng_sentiment['Sentiment'] == 'positive', 'Word'].tolist()
    negative  = eng_sentiment.loc[eng_sentiment['Sentiment'] == 'negative', 'Word'].tolist()

    # Tokenize each document
    doc_words = [ word_tokenize(doc)  for doc in df['Content']]  

    # Calculate the scores
    bar    = Bar("Calculating Loughran and MacDonald scores...", max=len(df))
    scores = calculate_scores(doc_words, positive, negative, bar)
    df["lm_scores"] = scores 
    return df 
 

def get_vader_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the VADER compound scores 

    :params df is the dataframe
    :type :pd.DataFrame

    :return: (pd.DataFrame)
    """

    review_compound_scores = []

    bar = Bar("Calculating VADER compound scores...", max=len(df))
    for i in range(len(df)):
        sentences             = tokenize.sent_tokenize(df['Content'][i])
        sid                   = SentimentIntensityAnalyzer()
        compound_scores       = [ sid.polarity_scores(s)['compound']  for s in sentences]
        final_compound_score  = round(sum(compound_scores)/len(compound_scores),2)

        review_compound_scores.append(final_compound_score)
        bar.next()
    bar.finish()

    
    df["compound_scores"] = review_compound_scores 

    return df 



def get_afinn_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the AFINN scores 

    :params df 
    :type :pd.DataFrame 

    :return: (pd.DataFrame)
    """

    afinn = Afinn()

    # Calculate the sentiment scores
    bar = Bar("Calculating Afinn scores...", max=len(df))
    sentiment_scores       = [ afinn.score(clean_text(review)) for review in tqdm(df['Content'], desc="Calculating Afinn scores...")]
    bar.finish()

    df['afinn_scores']     = sentiment_scores
    
    return df 