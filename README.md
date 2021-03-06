# Cordis Rank 
A tool to rank a company/institute based on EC contributions using 
[Cordis](https://cordis.europa.eu/data) dataset.


## Requirements
The tool has been tested on Ubuntu 18.04, Windows 10, and mac OS Catalina.
It requires
* Python 3.6+ 
* pandas
* pytest

## Setup
It's a typical python3 setup. Once you installed Python 3.6+ , 
open a terminal, e.g. in your `$HOME` directory and follow these steps

#### Clone the repo
```
git clone https://github.com/fabriziomiano/cordis-rank.git
```
#### Install `virtualenv`
##### Ubuntu 18.04:
```
sudo apt install -y python3-venv
```

##### mac OS Catalina:
```
xcode-select --install
sudo easy_insall virtualenv
```

##### Windows 10

`virtualenv` is shipped with the Python3.6+ installation setup 

Then, let's create a new directory in e.g. `$HOME/.envs/cordis-rank`
```
mkdir -p ~/.envs/cordis-rank
```


#### Create and activate the virtual environment
Assuming you're still in a terminal in your `$HOME` directory
##### Ubuntu & mac OS
```
python3 -m venv ~/.envs/cordis-rank
source ~/.envs/cordis-rank/bin/activate
```
##### Windows
```
python3 -m venv cordis-rank
cordis-rank\Scripts\activate.bat
```
Check that now you have `(cordis-rank)` at the beginning of your command line

Update `pip` and install the requirements in `requirements.txt`
```
pip install --upgrade pip
pip install -r requirements.txt
```

You're now ready to run it

## Configuration
Although the tool accepts user input parameters, the file `constants.py`
contains a number of constans that can be modified according to the type 
of data to use or analysis to carry out. 
In particular, here are some of the parameters:

* COMPANY_NAME: the name of the company to rank
* ACTIVITY_TYPE_FILTER: e.g. "PRC" to consider only companies
* APPLY_PRC_FILTER: boolean: apply the activity-type filter if True
* BUDGET_COLUMN_NAME: name of the budget / EC contribution column, e.g. "ecContribution"
* INTERESTING_COLUMNS: the list of columns to filter the raw Cordis dataset with
* DEFAULT_LOCAL_DATA_PATH: the default path of the Cordis dataset in this repo
* DEFAULT_URL: the default URL used to get the Cordis 2020 CSV file
* COLUMNS_MAP: a dict to rename the processed data frame to pretty print ranking results

## How to run 
* Navigate to the working copy of the repo you previously cloned
```
cd cordis-rank
```

* Run the tool by giving
```
python rank.py
```
An initialization output should show up, saying
```
config - [INFO] - --------------------------------------------------
config - [INFO] - Initializing with the following configuration
config - [INFO] - Check constants.py to change any of the following
config - [INFO] - --------------------------------------------------
config - [INFO] - COMPANY_NAME: THE UNIVERSITY OF SUSSEX
config - [INFO] - ACTIVITY_TYPE_FILTER: HES
config - [INFO] - APPLY_ACTIVITY_FILTER: True
config - [INFO] - --------------------------------------------------
config - [INFO] - Assuming an input dataset with the following features
config - [INFO] - --------------------------------------------------
config - [INFO] - BUDGET_COLUMN_NAME: ecContribution
config - [INFO] - COMPANY_COLUMN_NAME: name
config - [INFO] - ACTIVITY_COLUMN_NAME: activityType
config - [INFO] - COUNTRY_COLUMN_NAME: country
config - [INFO] - --------------------------------------------------
config - [INFO] - Fallback data sources
config - [INFO] - --------------------------------------------------
config - [INFO] - DEFAULT_URL: https://cordis.europa.eu/data/cordis-h2020organizations.csv
config - [INFO] - DEFAULT_LOCAL_DATA_PATH: cordis-h2020organizations.csv
config - [INFO] - --------------------------------------------------
```
at the end of which you will be prompted to whether download the data or 
run on a local CSV file
```
Read Cordis data_tools from URL? [y/n]: n
```
in this example the cordis-h2020organizations.csv file within this repo (leave blank)
```
Data file path (default: cordis-h2020organizations.csv): 
```
and you should get the following output
```
data_tools - [INFO] - Reading data_tools from cordis-h2020organizations.csv
data_tools - [INFO] - Data frame loaded in 0.5 seconds
```
then, if you set the activity-type filter to true in `constants.py`, 
you'll get a message informing you about the filter being applied
```
data_tools - [INFO] - Considering only activityType = HES
```
lastly, you should get the following results 
```
printer - [INFO] - --------------------------------------------------
printer - [INFO] - Ranking:
   Rank       Company / Institute Country  EC Contribution
0   124  THE UNIVERSITY OF SUSSEX      UK      43154405.56
printer - [INFO] - --------------------------------------------------
printer - [INFO] - Overall company budget: 43154405.56
printer - [INFO] - Company Ranking: 124 out of 1753
printer - [INFO] - Done
```

**Note:** if you choose to read the data from the default 2020 Cordis URL:

https://cordis.europa.eu/data/cordis-h2020organizations.csv

the process may take a while as pandas need to download the data. 
Furthermore, the final results may vary, as the CSV file might 
have been updated with respect to the one in this repo.

That's it!

## Tests
To run the tests from the home of the repo, e.g. `$HOME/cordis-rank`, simply run 
```
pytest
```
Tests may take a while as the data have to be downloaded twice to run the various 
fixtures. 

**Do not forget** to rerun the test if you change any of  configuration parameters in 
`constants.py`
