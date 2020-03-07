# Rank R2M 

A tool to carry out a very basic analysis to rank R2M using Cordis data and in particular
the EC contribution to the various companies / institutions.

## Requirements
The tool has been tested on Ubuntu 18.04 and it requires
* Python 3.7+ 
* pandas
* pytest

In principle, it should work also on Windows and mac OS

## Setup
It's a typical python3 setup:

* Open a terminal, e.g. in your `$HOME` directory
* Clone the repo using SSH (your SSH key has to be added to GitLab first)
```
git clone git@gitlab.com:r2mdev/r2m-rank.git
```
otherwise use HTTPS authentication
```
git clone https://gitlab.com/r2mdev/r2m-rank.git
```
* Install `virtualenv`:
```
pip3 install virtualenv
```
* Create a directory to host the virtual environment, e.g. in `$HOME/.envs/cordis`
```
mkdir -p ~/.envs/cordis
```
* Create the virtual environment and activate it
```
virtualenv -p python3 ~/.envs/cordis
source ~/.envs/cordis/bin/activate
```
Check that now you have `(cordis)` at the beginning of your command line
* install the requirements in `requirements.txt`
```
pip install -r requirements.txt
```
You're now ready to run it

## Configuration
Although the tool accepts user input parameters, the file `constants.py`
contains a number of constans that can be modified according to the type 
of data to use or analysis to carry out. 
In particular, the following parameters are defined:

* INTERESTING_COLUMNS: the list of columns to filter the raw Cordis dataset with
* DEFAULT_LOCAL_DATA_PATH: the default path of the Cordis dataset in this repo
* DEFAULT_URL: the default URL used to get the Cordis 2020 CSV file
* APPLY_PRC_FILTER: a boolean to select companies only or all types
* COLUMNS_MAP: a dict to rename the processed data frame to pretty print ranking results

## How to run 
* Navigate to the working copy of the repo you previously cloned
```
cd $HOME/r2m-rank
```
* Run the tool by giving
```
python rank_r2m.py
```
Provide the requested inputs when prompted, e.g. run on a local CSV file
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
then specify whether you want to select only companies, i.e. `activityType == "PRC"`
```
Consider companies only? (activityType = "PRC") [y/n]: y
```
and you should get the following results 
```
printer - [INFO] - Printing single-branch ranking...
   Rank                 Branch Country  EC Contribution
0   264       R2M SOLUTION SRL      IT       6106138.88
1   819           R2M SOLUTION      FR       2726124.69
2  2825  R2M SOLUTION SPAIN SL      ES       1209711.38
3  9799       R2M SOLUTION LTD      UK        248675.00
printer - [INFO] - Overall R2M budget: 10290649.95
printer - [INFO] - R2M Ranking: 130 out of 19097
```

**Note:** if you choose to read the data from the default 2020 Cordis URL:

https://cordis.europa.eu/data/cordis-h2020organizations.csv

the process may take a while as pandas need to download the data. 
Furthermore, the final results may vary, as the CSV file might 
have been updated with respect to the one in this repo.

That's it!

## Tests
To run the tests from the home of the repo, e.g. `$HOME/cordis`, simply run 
```
pytest
```
Tests may take a while as the various fixtures refer  both local and remote data

**Do not forget** to rerun the test if you change the configuration parameters in 
`constants.py`
