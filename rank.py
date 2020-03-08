"""
This script read a Cordis CSV file (from url, or local) and
tries to Rank a given company w.r.t. the EC contribution value.
It preprocesses the CSV first, calculates the overall budget,
and it then ranks the single company branches (if can be grouped) or the company
"""
import sys
from settings import printerlog, print_configuration
from data_tools import (
    get_cordis_data, company_filter, rename_df_columns,
    groupby_sort, calculate_company_budget, get_company_ranking)


def rank():
    """
    Print a dataframe populated with the company data only.

    Output example with COMPANY_NAME = "R2M":

       Rank                 Branch Country  EC Contribution
    0   264       R2M SOLUTION SRL      IT       6106138.88
    1   819           R2M SOLUTION      FR       2726124.69
    2  2825  R2M SOLUTION SPAIN SL      ES       1209711.38
    3  9799       R2M SOLUTION LTD      UK        248675.00

    """
    print_configuration()
    try:
        df = get_cordis_data()
        df_grouped = groupby_sort(df)
        df_rank = company_filter(df_grouped)
        df_company = rename_df_columns(df_rank)
        printerlog.info("-" * 50)
        printerlog.info("Ranking:\n{}".format(df_company))
        printerlog.info("-" * 50)
        budget = calculate_company_budget(df)
        ranking = get_company_ranking(df_grouped, budget)
        printerlog.info("Overall company budget: {}".format(budget))
        n_companies = df_grouped.shape[0]
        msg = "Company Ranking: {} out of {}".format(ranking, n_companies)
        printerlog.info(msg)
        printerlog.info("Done")
    except Exception as e:
        printerlog.error("{}".format(e))
        printerlog.error("Quitting")
        sys.exit(0)


if __name__ == "__main__":
    rank()
