"""
Author: Rachael Thormann
Python Version: 3.6
File Name: HourlyVisualizer.py
Last Edited: 8/2/2019
File Purpose: To visualize the unprocessed data on an hourly basis.
"""

from DataPrep import *
from Statistics import *


def plotHours(df):
    df.index = pd.to_datetime(df.index)


def main():
    """
    Main Function.

    :return:
    """
    df = createDataFrame()
    df = formatDataFrame(df)

    printStatistics(df)


if __name__ == '__main__':
    main()
