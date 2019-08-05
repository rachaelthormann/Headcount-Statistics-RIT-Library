"""
Author: Rachael Thormann
Python Version: 3.6
File Name: Statistics.py
Last Edited: 8/4/2019
File Purpose: To process data and produce statistics.
"""

import pandas as pd
import numpy as np
from DataPrep import *


def printStatistics(df):
    """
    Prints the average headcount over all days, as well as the minimum and maximum days.

    :return:
    """
    overallAverage(df)
    getMax(df)
    getMin(df)
    averageByMonth(df)


def overallAverage(df):
    """

    :param df:
    :return:
    """
    # print average across all days
    print(df.mean().mean())

    print("\n")


def getMax(df):
    """

    :param df:
    :return:
    """
    # print day that has the maximum average
    print(df.mean().idxmax())
    print(df.mean().max())

    print("\n")


def getMin(df):
    """

    :param df:
    :return:
    """
    # print the day that has the minimum average
    print(df.mean().idxmin())
    print(df.mean().min())


def averageByMonth(df):
    """

    :param df:
    :return:
    """
    # transpose so that date is functioning as index
    dfT = transposeDataFrame(df)

    print("\n")

    months = dfT.groupby(pd.Grouper(freq="M")).mean().index
    month_counter = 0

    # print each month with its associated average
    for x in dfT.groupby(pd.Grouper(freq="M")).mean().values:
        print(str(months[month_counter].strftime('%B %Y')) + ":  " + str(np.nanmean(x).round(2)))
        month_counter += 1


"""
def averageByWeek():

    # transpose so that date is functioning as index
    dfT = transposeDataFrame()

    print("\n")

    months = dfT.groupby(pd.Grouper(freq="W")).mean().index
    print(months.key)
    month_counter = 0

    # print each month with its associated average
    for x in dfT.groupby(pd.Grouper(freq="M")).mean().values:
        print(str(months[month_counter].strftime('%B %Y')) + ":  " + str(np.nanmean(x).round(2)))
        month_counter += 1
"""




