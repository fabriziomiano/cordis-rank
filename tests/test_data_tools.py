import numpy as np
from constants import (
    DEFAULT_LOCAL_DATA_PATH, DEFAULT_URL, INTERESTING_COLUMNS, COLUMNS_MAP
)
from data_tools import (
    get_cordis_data, groupby_sort, r2m_filter, calculate_r2m_budget,
    rename_df_columns, preprocess_df, get_r2m_ranking
)


def test_get_cordis_data():
    """Test data_tools.get_cordis_data using default url and datapath"""
    df_local = get_cordis_data(data_path=DEFAULT_LOCAL_DATA_PATH)
    df_url = get_cordis_data(url=DEFAULT_URL)
    assert not df_local.empty
    assert not df_url.empty


"""
Once the test_get_cordis_data() has passed get the local and remote
data frame to speed up testing time, as these are used in every fixture
"""
DF_LOCAL = get_cordis_data(data_path=DEFAULT_LOCAL_DATA_PATH)
DF_URL = get_cordis_data(url=DEFAULT_URL)


def test_preprocess_df():
    """Test data_tools.preprocess_df() using the default url and data path"""
    df_local = preprocess_df(DF_LOCAL, apply_filter=True)
    df_url = preprocess_df(DF_URL, apply_filter=True)
    assert list(df_local.columns) == INTERESTING_COLUMNS
    assert list(df_url.columns) == INTERESTING_COLUMNS
    df_local_test = df_local[df_local.activityType == "PRC"]
    df_url_test = df_url[df_url.activityType == "PRC"]
    assert not df_local_test.empty
    assert not df_url_test.empty


# TODO: Think about a more robust test
def test_groupby_sort():
    """Test data_tools.groupby_sort()"""
    df_grouped = groupby_sort(DF_LOCAL)
    assert df_grouped.shape[0] <= DF_LOCAL.shape[0]
    df_grouped = groupby_sort(DF_URL)
    assert df_grouped.shape[0] <= DF_URL.shape[0]


def test_r2m_filter():
    """Test data_tools.r2m_filter()"""
    df_r2m = r2m_filter(DF_LOCAL)
    assert not df_r2m.empty
    df_r2m = r2m_filter(DF_URL)
    assert not df_r2m.empty


def test_rename_df_columns():
    """Test data_tools.rename_df_columns()"""
    df_local = groupby_sort(DF_LOCAL)
    df_url = groupby_sort(DF_URL)
    df_local = r2m_filter(df_local)
    df_url = r2m_filter(df_url)
    assert list(df_local.columns) == list(COLUMNS_MAP.keys())
    assert list(df_url.columns) == list(COLUMNS_MAP.keys())
    df_local_renamed = rename_df_columns(df_local)
    df_url_renamed = rename_df_columns(df_url)
    assert list(df_local_renamed.columns) == list(COLUMNS_MAP.values())
    assert list(df_url_renamed.columns) == list(COLUMNS_MAP.values())


def test_calculate_r2m_budget():
    """Test data_tools.calculate_r2m_budget()"""
    assert type(calculate_r2m_budget(DF_LOCAL)) == np.float64
    assert calculate_r2m_budget(DF_LOCAL) != 0
    assert type(calculate_r2m_budget(DF_URL)) == np.float64
    assert calculate_r2m_budget(DF_URL) != 0


def test_get_r2m_ranking():
    """Terst data_tools.get_r2m_ranking()"""
    df_local_grouped = groupby_sort(DF_LOCAL)
    df_url_grouped = groupby_sort(DF_URL)
    r2m_budget_local = calculate_r2m_budget(DF_LOCAL)
    r2m_budget_url = calculate_r2m_budget(DF_URL)
    assert type(r2m_budget_local) == np.float64
    assert r2m_budget_local != 0
    assert type(r2m_budget_url) == np.float64
    assert r2m_budget_url != 0
    r2m_ranking_local = get_r2m_ranking(df_local_grouped, r2m_budget_local)
    r2m_ranking_url = get_r2m_ranking(df_url_grouped, r2m_budget_url)
    assert type(r2m_ranking_local) == int
    assert type(r2m_ranking_url) == int
