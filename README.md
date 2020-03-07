# Rank R2M 

A tool to carry out a very basic analysis to rank R2M using Cordis data. 

## Requirements
The tool has been tested on Ubuntu 18.04.
* Python 3.7+ 

Then simply `pip install -r requirements.txt`

## How to run 
Just give

```python rank_r2m.py```

and provide the requested inputs.

## Sample
It has been tested with the CSV file in the repo (H2020).

### Sample output

```
Read Cordis data_tools from URL? [y/n]: n
Data file path (default: cordis-h2020organizations.csv): 
data_tools - [INFO] - Reading data_tools from cordis-h2020organizations.csv
data_tools - [INFO] - Data frame loaded in 0.5 seconds
Consider companies only? (activityType = "PRC") [y/n]: y
printer - [INFO] - Printing single-branch ranking...
   Rank                 Branch Country  EC Contribution
0   264       R2M SOLUTION SRL      IT       6106138.88
1   819           R2M SOLUTION      FR       2726124.69
2  2825  R2M SOLUTION SPAIN SL      ES       1209711.38
3  9799       R2M SOLUTION LTD      UK        248675.00
printer - [INFO] - Overall R2M budget: 10290649.95
printer - [INFO] - R2M Ranking: 130 out of 19097
```
