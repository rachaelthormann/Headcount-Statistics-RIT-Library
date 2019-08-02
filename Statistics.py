"""
Author: Rachael Thormann
Python Version: 3.6
File Name: Statistics.py
Last Edited: 8/2/2019
File Purpose: To process data and produce statistics.
"""


def printStatistics(df):
    """
    Prints the average headcount over all days, as well as the minimum and maximum days.

    :return:
    """
    # print average across all days
    print(df.mean().mean())

    print("\n")

    # print day that has the maximum average
    print(df.mean().idxmax())
    print(df.mean().max())

    print("\n")

    # print the day that has the minimum average
    print(df.mean().idxmin())
    print(df.mean().min())

