"""
This script read a Cordis CSV file (from url, or local) and
tries to Rank the R2M company w.r.t. the EC contribution value.
It preprocesses the CSV first, calculates the overall R2M budget,
and it then ranks the single R2M branches, and R2M globally
"""
import sys
from settings import printerlog
from data_tools import (
    get_cordis_data, r2m_filter, rename_df_columns,
    groupby_sort, calculate_r2m_budget, get_r2m_ranking)


def rank_r2m():
    """
    Print a dataframe populated with the R2M-data only.
    Output example:
       Rank                 Branch Country  EC Contribution
    0   264       R2M SOLUTION SRL      IT       6106138.88
    1   819           R2M SOLUTION      FR       2726124.69
    2  2825  R2M SOLUTION SPAIN SL      ES       1209711.38
    3  9799       R2M SOLUTION LTD      UK        248675.00
    :return: None
    """
    try:
        df = get_cordis_data()
        df_grouped = groupby_sort(df)
        df_rank = r2m_filter(df_grouped)
        df_r2m = rename_df_columns(df_rank)
        printerlog.info("Printing single-branch ranking...\n{}".format(df_r2m))
        r2m_budget = calculate_r2m_budget(df)
        r2m_ranking = get_r2m_ranking(df_grouped, r2m_budget)
        printerlog.info("Overall R2M budget: {}".format(r2m_budget))
        n_companies = df_grouped.shape[0]
        msg = "R2M Ranking: {} out of {}".format(r2m_ranking, n_companies)
        printerlog.info(msg)
    except Exception as e:
        printerlog.error("{}".format(e))
        printerlog.error("Quitting")
        sys.exit(0)


if __name__ == "__main__":
    rank_r2m()
