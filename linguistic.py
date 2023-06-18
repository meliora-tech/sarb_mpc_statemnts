"""
This file has different meassures of readability

Date: 2023-06-16
"""


import numpy as np
from readability import Readability 
from typing import List, Union

def calculate_flesch(text: str) -> List[Union[float, str, int]]:
    """
    Calculate the Flesch Reading Ease score

    :params text is the content
    :type :str

    :return: (List[Union[float, str, int]])
    """

    r      = Readability(text)
    flesch = r.flesch()

    score   = flesch.score 
    ease    = flesch.ease 
    grade_levels = flesch.grade_levels

    return [score, grade_levels]


def calculate_flesch_kincaid(text: str) -> List[Union[float, str, int]]:
    """
    Calculate the Flesch-Kincaid Grade Level 

    :params text is the content
    :type :str 

    :return: (List[Union[float, str, int]])
    """
    r           = Readability(text)
    fk          = r.flesch_kincaid()
    score       = fk.score 
    grade_level = fk.grade_level

    return [score, grade_level]


def calculate_gunning_fog(text: str) -> List[Union[float, str, int]]:
    """
    Calcaulate the Gunning Fog readability measure

    :params text is for the content
    :type :str 

    :return: (List[Union[float, str, int]])
    """

    r           = Readability(text)
    gf          = r.gunning_fog()
    score       = gf.score
    grade_level = gf.grade_level

    return [score, grade_level]


def calculate_smog(text: str) -> List[Union[float, str, int]]:
    """
    Calculate the Simple Measure of Gobbledygook i.e. SMOG

    :params text 
    :type :str 

    :return: (List[Union[float, str, int]])
    """

    r           = Readability(text)
    try:
        smog        = r.smog(all_sentences=True)
        score       = smog.score 
        grade_level = smog.grade_level
    except:
        score       = np.nan 
        grade_level = [np.nan]

    return [score, grade_level]