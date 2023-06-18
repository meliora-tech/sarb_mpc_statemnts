import glob
import numpy as np
import os
import pandas as pd
import plotly.graph_objects as go 
import plotly.express as px
import PyPDF2
import sys

from nltk.tokenize import word_tokenize, sent_tokenize
from plotly.subplots import make_subplots
from tqdm import tqdm
from typing import Dict, List 


# Own modules
from constants import NEGATION_WORDS, GT_POSITIVE_MODIFIERS, GT_NEGATIVE_MODIFIERS, GT_DICTIONARY
from linguistic import calculate_flesch, calculate_flesch_kincaid, calculate_gunning_fog, calculate_smog
from read_data import read_mpc_statements
from sentiment import (get_lm_scores, get_vader_scores, get_afinn_scores, get_bing_scores, get_general_inquirer_scores,
                        get_mpqa_scores, get_nrc_scores, get_textblob_scores, get_flair_scores)
from tone import (count_tone, count_tone_sentence, create_lm_sentiment)

def plot_heatmap(df_corr: pd.DataFrame):
    """
    Plot a heatmap

    :params df_corr is a correlation dataframe
    :type :pd.DataFrame

    """
    
    fig = go.Figure()
    fig.add_trace(
        go.Heatmap(
            x = df_corr.columns,
            y = df_corr.index,
            z = np.array(df_corr),
            colorscale=px.colors.diverging.RdBu,
            text=df_corr.values,
            texttemplate='%{text:.2f}'
        )
    )
    
    fig.update_layout(title="Correlation Matrix: Sentiment Indices for SARB MPC statements (2000 - 2023)")

    fig.show()


def plot_sentiment_indices(df: pd.DataFrame):
    """
    Plot Sentiment Indices

    :params df
    :type :pd.DataFrame    
    """

    sentiment_names = ["tone_GT_entire", "tone_GT", "flair_fast_scores", "flair_scores", "blob_scores", "bing_scores",
                        "gi_scores", "mpqa_scores", "nrc_scores", "lm_scores", "compound_scores", "afinn_scores"]
    names           = ("GT Tone Index - Entire", "GT Tone Index - SA", "Flair Fast Sentiment Index", "Flair Transformer Sentiment Index",
                        "BlobText Sentiment Index", "Bing Sentiment Index", "General Inquirer Sentiment Index", "MPQA Subjectivity Sentiment Index",
                        "NRC Emotions Sentiment Index", "Loughran and MacDonald Sentiment Index", "VADER Sentiment Index", "AFINN Sentiment Index" )

    total_rows = int(len(sentiment_names)/2) 
    total_cols  = 2

    cols  = [1,2]*total_rows
    rows  = [1,1,2,2,3,3,4,4,5,5,6,6]
    fig = make_subplots(rows=total_rows, cols=total_cols,
                subplot_titles=names)

    for i, values in enumerate(zip(sentiment_names, cols, rows)):
        fig.append_trace(go.Scatter(
                x=df["MPC Date"],
                y=df[values[0]],
            ), row=values[2], col=values[1])

    fig.update_layout(height=900, width=1200, title_text="Sentiment Indices for SARB MPC statements (2000 - 2023)", showlegend=False)
    fig.show()


def plot_readability_scores(df: pd.DataFrame):
    """
    Plot the Readability scores

    :params df
    :type :pd.DataFrame
    """

    columns = list(df.columns)
    fig     = make_subplots(rows=len(columns), cols=1,
                  subplot_titles=columns)


    for idx, column in enumerate(columns):

        fig.append_trace(go.Scatter(
                x=df.index,
                y=df[column]
        ), row=idx+1, col=1)


    fig.update_layout(height=1080, width=1800, title_text="Readability Scores for SARB MPC statements (2000 - 2023)", showlegend=False)
    fig.show() 


def main(do_analysis: bool=True, read_ability=True):
    """
    Main function to run the analysis

    :params do_analysis or do plots based on sentiment scores
    :type :bool
    """

    if not do_analysis:

        #=================================
        # Sentiment Indices
        #=================================

        sentiment_scores = pd.read_csv("results/sentiment_scores.csv")
    
        # Plot the correlation matrix
        sentiment_scores.set_index("MPC Date", inplace=True)

        # Find the correlation 
        df_corr = sentiment_scores.corr()
        
        # Plot the heatmap
        keep    = np.triu(np.ones(df_corr.shape)).astype('bool')
        df_corr = df_corr.where(keep)
        plot_heatmap(df_corr)
        
        # Plot the sentiment indices
        sentiment_scores.reset_index(inplace=True)
        sentiment_scores["MPC Date"] = pd.to_datetime(sentiment_scores["MPC Date"], format="%Y%m%d")
        plot_sentiment_indices(sentiment_scores)

        #=================================
        # Readability scores
        #=================================

        readability_df = pd.read_csv("results/readability.csv")
        readability_df["MPC Date"] = pd.to_datetime(readability_df["MPC Date"], format="%Y%m%d")
        readability_df.set_index("MPC Date", inplace=True)
        
        # Plot the scores 
        plot_readability_scores(readability_df)

    if do_analysis:
        # Read in the cleaned Loughran and MacDonald Dictionary
        eng_sentiment = pd.read_csv("data/english_dictionary.csv")

        # Read in all MPC Statements  
        mpc_df = read_mpc_statements()

        if read_ability:

           # Readability names
           names = ['Flesch', 'Flesch and Kincaid', 'Gunning Fog', 'Smog']
           
           # Readability functions 
           readability_functions = [calculate_flesch, calculate_flesch_kincaid, calculate_gunning_fog, calculate_smog]  

           # Placeholders for results 
           readability_scores  = {}
           readability_years   = {}

           readability_scores["MPC Date"] = mpc_df["MPC Date"]
           readability_years["MPC Date"]  = mpc_df["MPC Date"]

           for func, name in zip(readability_functions,names):
                 scores = []
                 years  = []
                 for mpc in tqdm(mpc_df['Content'], desc=f"Calculating {name} Readability scores..."):
                
                    readability_result= func(mpc)
                    score             = readability_result[0]
                    year              = readability_result[1][0]

                    scores.append(score)
                    years.append(year)
                
                 readability_scores[name] = scores 
                 readability_years[name]  = years 

           readability_df         = pd.DataFrame.from_dict(readability_scores)
        #    readability_years_df   = pd.DataFrame.from_dict(readability_years)
          
           # Save the readability dataframe
           readability_df.to_csv("results/readability.csv", index=False)
        #    readability_years_df.to_csv("results/readability_years.csv", index=False)
         

        # Calculate sentiment using Flair
        mpc_df = get_flair_scores(mpc_df)
    
        # Calculate the sentiment using the Flair Fast model
        mpc_df = get_flair_scores(mpc_df, fast=True)
    
        # Calculate sentiment using Textblob
        mpc_df = get_textblob_scores(mpc_df)
        
        # Calculate the NRC Lexicon scores
        mpc_df = get_nrc_scores(mpc_df)

        # Calculate the LM scores for each statement
        mpc_df = get_lm_scores(mpc_df)
        
        # Calculate the Vader scores
        mpc_df = get_vader_scores(mpc_df)

        # Calculate the Afinn scores
        mpc_df = get_afinn_scores(mpc_df)
        
        # Calculate the Bing scores
        mpc_df = get_bing_scores(mpc_df)

        # Calculate the General Inquirer scores
        mpc_df = get_general_inquirer_scores(mpc_df)
    
        # Calculate the MPQA Subjectivity Lexicon scores
        mpc_df = get_mpqa_scores(mpc_df)
    
        # Create a dict of the negative and positive words of LM 
        sentiment_dict = create_lm_sentiment(eng_sentiment)

        #==================================================
        # Count the tone using the LM dictionary
        #==================================================
        results = [count_tone(sentiment_dict, text) for text in tqdm(mpc_df['Content'], desc="Calculating LM negation adjusted scores...")]
        columns = ['tone_LM', 'word_count', 'n_pos_words', 'n_neg_words', 'net_sent', 'pos_words', 'neg_words']
        df      = pd.DataFrame(results, columns=columns)

        mpc_df = pd.merge(mpc_df,df, left_index= True, right_index=True)



        # =======================================================================
        # Count tone using the GT modifiers and a SPECIFIC dictionary list
        #========================================================================

        lmdict     = {'hawkish': GT_DICTIONARY["hawkish"]["zaf"], 'dovish': GT_DICTIONARY["dovish"]["zaf"], 'positive': GT_POSITIVE_MODIFIERS, 'negative': GT_NEGATIVE_MODIFIERS}
        results_gt = [count_tone_sentence(lmdict, text) for text in tqdm(mpc_df['Content'], desc="Calculating GT South Africa specific scores...")]
        columns    = ['tone_GT', 'sentence_count', 'word_count', 'haw_words', 'dov_words', 'pos_modifiers', 'neg_modifiers']
        df         = pd.DataFrame(results_gt, columns=columns)

        mpc_df   = pd.merge(mpc_df, df, left_index=True, right_index=True)


        #============================================================================
        # Count tone using the GT modifiers and the ENTIRE dictionary list
        #=============================================================================

        # Create the the GT dictionary list
        hawkish_keys  = list(GT_DICTIONARY["hawkish"].keys())
        dovish_keys   = list(GT_DICTIONARY["dovish"].keys())

        hawkish_gt    = []
        dovish_gt     = []

        for hk, dk in zip(hawkish_keys, dovish_keys):
            arr_hk  = GT_DICTIONARY["hawkish"][hk]
            arr_dk  = GT_DICTIONARY["dovish"][dk]
            hawkish_gt.extend(arr_hk)
            dovish_gt.extend(arr_dk)

        lmdict     = {'hawkish': hawkish_gt, 'dovish': dovish_gt, 'positive': GT_POSITIVE_MODIFIERS, 'negative': GT_NEGATIVE_MODIFIERS}
        results_gt = [count_tone_sentence(lmdict, text) for text in tqdm(mpc_df['Content'], desc="Calculating GT entire scores...")]
        columns    = ['tone_GT_entire', 'sentence_count', 'word_count', 'haw_words', 'dov_words', 'pos_modifiers', 'neg_modifiers']
        df         = pd.DataFrame(results_gt, columns=columns)

        mpc_df   = pd.merge(mpc_df, df, left_index=True, right_index=True)


        # =======================================
        # Get the sentiment scores
        # =======================================
        sentiment_df = mpc_df[["MPC Date","tone_GT_entire", "tone_GT", "flair_fast_scores", "flair_scores", "blob_scores", "bing_scores",
                "gi_scores", "mpqa_scores", "nrc_scores", "lm_scores", "compound_scores", "afinn_scores"]]


        sentiment_df.to_csv("results/sentiment_scores.csv", index=False)

if __name__ == "__main__":
    main(do_analysis=False)

    