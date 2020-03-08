import numpy as np
from constants import (
    DEFAULT_LOCAL_DATA_PATH, DEFAULT_URL, INTERESTING_COLUMNS, COLUMNS_MAP,
    ACTIVITY_TYPE_FILTER
)
from data_tools import (
    get_cordis_data, groupby_sort, company_filter, calculate_company_budget,
    rename_df_columns, preprocess_df, get_company_ranking
)


def test_get_cordis_data():
    """Test data_tools.get_cordis_data using default url and datapath"""
    df_local = get_cordis_data(data_path=DEFAULT_LOCAL_DATA_PATH, test=True)
    df_url = get_cordis_data(url=DEFAULT_URL, test=True)
    assert not df_local.empty
    assert not df_url.empty


"""
Once the test_get_cordis_data() has passed get the local and remote
data frame to speed up testing time, as these are used in every fixture
"""
DF_LOCAL = get_cordis_data(data_path=DEFAULT_LOCAL_DATA_PATH, test=True)
DF_URL = get_cordis_data(url=DEFAULT_URL, test=True)


def test_preprocess_df():
    """Test data_tools.preprocess_df() using the default url and data path"""
    df_local = preprocess_df(DF_LOCAL, apply_filter=True)
    df_url = preprocess_df(DF_URL, apply_filter=True)
    assert list(df_local.columns) == INTERESTING_COLUMNS
    assert list(df_url.columns) == INTERESTING_COLUMNS
    df_local_test = df_local[df_local.activityType == ACTIVITY_TYPE_FILTER]
    df_url_test = df_url[df_url.activityType == ACTIVITY_TYPE_FILTER]
    assert not df_local_test.empty
    assert not df_url_test.empty


# TODO: Think about a more robust test
def test_groupby_sort():
    """Test data_tools.groupby_sort()"""
    df_grouped = groupby_sort(DF_LOCAL)
    assert df_grouped.shape[0] <= DF_LOCAL.shape[0]
    df_grouped = groupby_sort(DF_URL)
    assert df_grouped.shape[0] <= DF_URL.shape[0]


def test_company_filter():
    """Test data_tools.company_filter()"""
    df_company = company_filter(DF_LOCAL)
    assert not df_company.empty
    df_company = company_filter(DF_URL)
    assert not df_company.empty


def test_rename_df_columns():
    """Test data_tools.rename_df_columns()"""
    df_local = groupby_sort(DF_LOCAL)
    df_url = groupby_sort(DF_URL)
    df_local = company_filter(df_local)
    df_url = company_filter(df_url)
    assert list(df_local.columns) == list(COLUMNS_MAP.keys())
    assert list(df_url.columns) == list(COLUMNS_MAP.keys())
    df_local_renamed = rename_df_columns(df_local)
    df_url_renamed = rename_df_columns(df_url)
    assert list(df_local_renamed.columns) == list(COLUMNS_MAP.values())
    assert list(df_url_renamed.columns) == list(COLUMNS_MAP.values())


def test_calculate_company_budget():
    """Test data_tools.calculate_company_budget()"""
    assert type(calculate_company_budget(DF_LOCAL)) == np.float64
    assert calculate_company_budget(DF_LOCAL) != 0
    assert type(calculate_company_budget(DF_URL)) == np.float64
    assert calculate_company_budget(DF_URL) != 0


def test_get_company_ranking():
    """Terst data_tools.get_company_ranking()"""
    df_local_grouped = groupby_sort(DF_LOCAL)
    df_url_grouped = groupby_sort(DF_URL)
    company_budget_local = calculate_company_budget(DF_LOCAL)
    company_budget_url = calculate_company_budget(DF_URL)
    assert type(company_budget_local) == np.float64
    assert company_budget_local != 0
    assert type(company_budget_url) == np.float64
    assert company_budget_url != 0
    company_ranking_local = get_company_ranking(
        df_local_grouped, company_budget_local)
    company_ranking_url = get_company_ranking(
        df_url_grouped, company_budget_url)
    assert type(company_ranking_local) == int
    assert type(company_ranking_url) == int
