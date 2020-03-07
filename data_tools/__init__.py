import time

import pandas as pd

from settings import datalog
from constants import (
    DEFAULT_LOCAL_DATA_PATH, DEFAULT_URL, ACCEPTED_ANSWERS,
    INTERESTING_COLUMNS, COLUMNS_REMAP)


def get_cordis_data():
    """
    Return a pandas.DataFrame object either built from  a local CSV file
    or downloaded from a cordis URL
    :return: pandas.DataFrame
    """
    read_from_url = False
    while read_from_url not in ACCEPTED_ANSWERS:
        msg = "Read Cordis data_tools from URL? [y/n]: "
        read_from_url = input(msg)
    read_from_url = read_from_url == "y"
    if read_from_url:
        url = input("Please provide url (default: {}): ".format(DEFAULT_URL))
        if not url:
            url = DEFAULT_URL
        datalog.info("Trying to read data_tools from {}".format(url))
        start = time.time()
        df = pd.read_csv(url, delimiter=";", decimal=",", low_memory=False)
    else:
        msg = "Data file path (default: {}): ".format(DEFAULT_LOCAL_DATA_PATH)
        data_path = input(msg) or DEFAULT_LOCAL_DATA_PATH
        datalog.info("Reading data_tools from {}".format(data_path))
        start = time.time()
        df = pd.read_csv(data_path, delimiter=";", decimal=",", low_memory=False)
    elapsed_time = round((time.time() - start), 1)
    datalog.info("Data frame loaded in {} seconds".format(elapsed_time))
    df = preprocess_df(df)
    return df


def preprocess_df(df):
    """
    Return a df where activityType = "PRC"
    :param df: pandas.DataFrame
    :return: df: pandas.DataFrame
    """
    do_prc_only = False
    while do_prc_only not in ACCEPTED_ANSWERS:
        msg = "Consider companies only? (activityType = \"PRC\") [y/n]: "
        do_prc_only = input(msg)
    do_prc_only = do_prc_only == "y"
    if do_prc_only:
        df = df[df.activityType == "PRC"]  # Select companies only
    df = df[INTERESTING_COLUMNS].dropna()  # drop useless columns and rows containing "n/a"
    return df


def rename_df_columns(df):
    """Rename the given df's columns"""
    df_r2m = df.rename(columns=COLUMNS_REMAP)
    return df_r2m


def groupby_sort(df):
    """
    Return a data_tools frame grouped by columns "name" and "country"
    with descending values sorted by EC contribution "ecContribution"
    :param df:
    :return:
    """
    df = df.groupby(["name", "country"], as_index=False).sum()
    df = df.sort_values(by="ecContribution", ascending=False).reset_index(drop=True)
    return df


def r2m_filter(df):
    """
    Return a data_tools frame filtered by selecting
    only rows containing the string "R2M"
    :param df: pandas.DataFrame object
    :return: pandas.DataFrame object
    """
    df = df[df.name.str.contains("R2M")]
    df.reset_index(inplace=True)
    return df


def calculate_r2m_budget(df):
    """
    Print the total R2M EC contribution calculated
    by summing the column "ecContribution" of all
    the rows containing the string "R2M"
    :param df: pandas.DataFrame object
    :return: None
    """
    return df[df.name.str.contains("R2M")].ecContribution.sum()