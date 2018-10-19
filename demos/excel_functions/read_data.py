"""
Code for reading a dataset into a Pandas DataFrame
"""
from pyxll import xl_func
import pandas as pd
import os


@xl_func("str url, dict dtypes, str[] parse_dates, bool infer_datetime_format: object")
def read_csv_data(url, dtype=None, parse_dates=None, infer_datetime_format=False):
    """Reads a csv file from a url into a pandas DataFrame"""
    return pd.read_csv(url,
                       dtype=dtype,
                       parse_dates=parse_dates,
                       infer_datetime_format=infer_datetime_format)

