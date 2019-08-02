"""
Author: Rachael Thormann
Python Version: 3.6
File Name: DataPrep.py
Last Edited: 8/1/2019
File Purpose: To prep the data so that it can be efficiently processed and visualized.
"""

import pandas as pd
import numpy as np


def createDataFrame():
    """
    Read in both CSV files and place in one data frame.

    :return: data frame containing headcount data for entire year
    """

    # first CSV spans time frame 7/1/18 - 3/11/19
    # second CSV spans time frame 3/12/19 - 6/30/19
    library_stats1 = pd.read_csv("library_stats_page1.csv", nrows=24)
    library_stats2 = pd.read_csv("library_stats_page2.csv")

    frames = [library_stats1, library_stats2]
    df = pd.concat(frames, axis=1)

    del df['Time']

    return df


def formatDataFrame(df):
    """
    Convert columns to integers and replace missing values with NA.

    :return:
    """
    # convert columns to integers and replace missing values with NA
    df = df.replace("Missed", np.nan)
    df = df.replace('0', np.nan)
    df = df.apply(pd.to_numeric)

    return df
