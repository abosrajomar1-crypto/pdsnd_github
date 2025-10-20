

Date: 2025-10-20
Title: US Bikeshare Data Explorer

Description

This project is a command-line tool that explores US bikeshare data for Chicago, New York City, and Washington.
It interactively asks the user to filter by city, month (Jan–Jun or all), and day of week (Mon–Sun or all), then computes and prints:

Most common month, day, and start hour

Most popular start and end stations and the most frequent trip combination

Total and average trip durations (nicely formatted as Hh Mm Ss)

User statistics (user types, gender breakdown, and birth year stats when available)

Optional paging through raw rows in 5-row increments

The script includes friendly validation, handles missing city columns (e.g., Washington lacks gender/birth year), and catches missing data files gracefully.

Files used

bikeshare.py — the main Python program (your script below)

chicago.csv, new_york_city.csv, washington.csv — input datasets (not tracked if ignored)

.gitignore — include patterns like *.csv if you don’t want datasets pushed to GitHub

If your repository has more/other files, list them here.

How to run
1) Requirements

Python 3.8+

Packages: pandas (and Python’s built-in time)

Install dependencies:

pip install pandas

2) Project structure (example)
.
├─ bikeshare.py
├─ .gitignore
├─ chicago.csv
├─ new_york_city.csv
└─ washington.csv


If you prefer not to commit CSV files, add *.csv to .gitignore.

3) Run the program

From the project folder:

python bikeshare.py


Follow the prompts:

City: chicago | new york city | washington

Month: all or one of january … june

Day: all or one of monday … sunday

Type yes when asked to view raw data (shown 5 rows at a time). Type no to stop.
At the end, choose whether to restart with new filters.

Explanation of the Python file (bikeshare.py)
import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}


Maps each supported city to its CSV file name.

get_filters()

Interactively asks for city, month, and day with input validation.

Accepts only supported values and keeps prompting until valid.

Returns (city, month, day) in lowercase.

load_data(city, month, day)

Loads the selected city’s CSV into a pandas DataFrame.

Parses Start Time into datetime and derives helper columns:

month (full month name, lowercase)

day_of_week (full day name, lowercase)

hour (0–23)

Applies filters if month/day are not all.

Returns the filtered DataFrame.

time_stats(df)

Prints the most common month, day of week, and start hour for the filtered data.

Skips gracefully if the DataFrame is empty.

station_stats(df)

Prints the most common start station, end station, and most frequent (Start Station → End Station) trip pair.

trip_duration_stats(df)

Computes total and mean travel time from Trip Duration (in seconds).

Formats them as human-readable strings like 2h 15m 07s.

user_stats(df)

Prints counts of User Type (always present).

Prints Gender counts and Birth Year stats (earliest, most recent, most common) if those columns exist for the city.

For Washington (which lacks these), it states that the data is unavailable.

display_raw_data(df)

Offers to show raw rows in blocks of 5, with an option to continue showing the next 5 each time.

main()

Orchestrates the program flow:

Gets filters

Loads data (with FileNotFoundError handling if a CSV is missing)

Runs all stats functions

Offers raw data view

Asks whether to restart

Running the script directly (python bikeshare.py) calls main().

Example .gitignore

If you don’t want CSVs or notebook caches committed:

# data
*.csv

# python
__pycache__/
*.pyc

# jupyter
.ipynb_checkpoints/

Credits

Udacity’s Bikeshare project specification and starter resources

Official pandas documentation for data wrangling

