import re
import time
import logging
import pandas as pd

from settings import datalog
from constants import (
    DEFAULT_LOCAL_DATA_PATH, DEFAULT_URL, ACCEPTED_ANSWERS, INTERESTING_COLUMNS,
    COLUMNS_MAP, COMPANY_NAME, COMPANY_COLUMN_NAME, COUNTRY_COLUMN_NAME,
    APPLY_ACTIVITY_FILTER, ACTIVITY_TYPE_FILTER, ACTIVITY_COLUMN_NAME,
    BUDGET_COLUMN_NAME
)


def get_cordis_data(url=None, data_path=None, test=False):
    """
    Return a pandas.DataFrame object either built from  a local CSV file
    or downloaded from a cordis URL
    :param url: str: url of the CSV file
    :param data_path: str: path of the local CSV
    :param test: bool: if True set log level to ERROR
    :return: pandas.DataFrame
    """
    if test:
        datalog.setLevel(logging.ERROR)
    df = None
    if url is None and data_path is None:
        read_from_url = False
        while read_from_url not in ACCEPTED_ANSWERS:
            msg = "Read Cordis data from URL? [y/n]: "
            read_from_url = input(msg).lower()
        read_from_url = read_from_url == "y"
        if read_from_url:
            url = input("Please provide url (default: {}): ".format(DEFAULT_URL))
            if not url:
                url = DEFAULT_URL
            datalog.info("Trying to read data from {}".format(url))
            start = time.time()
            df = pd.read_csv(url, delimiter=";", decimal=",")
        else:
            msg = "Data file path (default: {}): ".format(DEFAULT_LOCAL_DATA_PATH)
            data_path = input(msg) or DEFAULT_LOCAL_DATA_PATH
            datalog.info("Reading data from {}".format(data_path))
            start = time.time()
            df = pd.read_csv(data_path, delimiter=";", decimal=",")
    else:
        start = time.time()
        if url is not None:
            datalog.info("Trying to read data from {}".format(url))
            df = pd.read_csv(url, delimiter=";", decimal=",")
        if data_path is not None:
            df = pd.read_csv(data_path, delimiter=";", decimal=",")
    elapsed_time = round((time.time() - start), 1)
    datalog.info("Data frame loaded in {} seconds".format(elapsed_time))
    if df is not None:
        if APPLY_ACTIVITY_FILTER:
            datalog.info(
                "Considering only activityType = {}".format(
                    ACTIVITY_TYPE_FILTER)
            )
        df = preprocess_df(df, apply_filter=APPLY_ACTIVITY_FILTER)
    else:
        msg = "Empty data frame. Please check data source"
        datalog.error(msg)
    return df


def preprocess_df(df, apply_filter=False):
    """
    Return a df containing only columns in INTERESTING_COLUMNS
    and where ACTIVITY_TYPE_COLUMN = ACTIVITY_TYPE_FILTER if apply_filter is True
    :param df: pandas.DataFrame
    :param apply_filter: bool:
    :return: df: pandas.DataFrame
    """
    if apply_filter:
        df = df[df[ACTIVITY_COLUMN_NAME] == ACTIVITY_TYPE_FILTER]
    df = df[INTERESTING_COLUMNS].dropna()
    return df


def rename_df_columns(df):
    """Rename the given df's columns"""
    df_company = df.rename(columns=COLUMNS_MAP)
    return df_company


def groupby_sort(df):
    """
    Return a data frame grouped by columns
    COMPANY_NAME_COLUMN and COUNTRY_COLUMN
    with descending values sorted by BUDGET_COLUMN_NAME
    :param df:
    :return:
    """
    list_columns_group_by = [COMPANY_COLUMN_NAME, COUNTRY_COLUMN_NAME]
    df = df.groupby(list_columns_group_by, as_index=False).sum()
    df = df.sort_values(
        by=BUDGET_COLUMN_NAME, ascending=False).reset_index(drop=True)
    return df


def company_filter(df):
    """
    Return a data frame filtered by selecting
    only rows containing the string COMPANY_NAME
    :param df: pandas.DataFrame object
    :return: pandas.DataFrame object
    """
    mask = df[COMPANY_COLUMN_NAME].str.contains(COMPANY_NAME, flags=re.IGNORECASE)
    df = df[mask]
    df.reset_index(inplace=True)
    return df


def calculate_company_budget(df):
    """
    Print the total COMPANY_NAME EC contribution calculated
    by summing the column BUDGET_COLUMN_NAME of all
    the rows containing the string COMPANY_NAME
    :param df: pandas.DataFrame object
    :return: None
    """
    mask = df[COMPANY_COLUMN_NAME].str.contains(COMPANY_NAME, flags=re.IGNORECASE)
    return df[mask][BUDGET_COLUMN_NAME].sum()


def get_company_ranking(df_grouped, budget):
    """
    Return the lowest df index of the row whose 
    BUDGET_COLUMN_NAME is >= a given budget
    :param df_grouped: pandas.DataFrame
    :param budget: float
    :return: int
    """
    ranking_mask = df_grouped[BUDGET_COLUMN_NAME] >= budget
    try:
        ranking = df_grouped.index[ranking_mask].tolist()[-1] + 1
    except IndexError:
        ranking = 1
    return ranking
