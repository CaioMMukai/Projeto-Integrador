# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:32:05 2020

@author: caio.mukai
"""
import datetime
import pandas as pd
import numpy as np
import os
import sys
import pandas as pd
import json

def save_as_csv(df, path):
    df.to_csv(path, sep=';', decimal=',', index=False, encoding='utf-8-sig')

def read_csv(path):
    return pd.read_csv(path, sep=';', decimal=',')

def read_json(path):
    return pd.read_json(path)