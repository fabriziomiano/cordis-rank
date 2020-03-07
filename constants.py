import datetime as dt

ACCEPTED_ANSWERS = ("y", "n")
INTERESTING_COLUMNS = ["name", "activityType", "ecContribution", "country"]
DEFAULT_LOCAL_DATA_PATH = "cordis-h2020organizations.csv"
YEAR = dt.datetime.now().year
DEFAULT_URL = "https://cordis.europa.eu/data/cordis-h2020organizations.csv"
COLUMNS_REMAP = {
    "index": "Rank",
    "name": "Branch",
    "country": "Country",
    "ecContribution": "EC Contribution"
}
