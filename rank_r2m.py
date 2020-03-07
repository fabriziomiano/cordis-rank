import sys
from settings import printerlog
from data_tools import (
    get_cordis_data, r2m_filter, rename_df_columns,
    groupby_sort, calculate_r2m_budget)


def rank_r2m():
    """
    Print a data_tools frame populated with the R2M-data_tools only where,
    the first column is the R2M ranking
    the second column is the R2M branch
    the third column is the branch country
    the fourth column is the EC contribution
    :return: None
    """
    try:
        df = get_cordis_data()
        df_grouped = groupby_sort(df)
        df_rank = r2m_filter(df_grouped)
        df_r2m = rename_df_columns(df_rank)
        printerlog.info("Printing single-branch ranking...\n{}".format(df_r2m))
        r2m_budget = calculate_r2m_budget(df)
        ranking_mask = df_grouped['ecContribution'] >= r2m_budget
        r2m_ranking = df_grouped.index[ranking_mask].tolist()[-1] + 1
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
