# US Bikeshare Data Explorer

A simple command-line tool to explore bikeshare data for three US cities using Python and pandas.

## Datasets

Place the following CSV files in the **same directory** as the script:

- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

These files should include columns such as:
- `Start Time`, `End Time`, `Trip Duration`
- `Start Station`, `End Station`
- `User Type`
- (Chicago & NYC typically) `Gender`, `Birth Year`

> Note: The Washington dataset usually does **not** have `Gender` and `Birth Year`.

## Requirements

- Python 3.8+
- `pandas`

Install dependencies:
```bash
pip install pandas
