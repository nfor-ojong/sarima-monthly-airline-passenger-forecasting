import pandas as pd
import numpy as np
import warnings
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import root_mean_squared_error, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import matplotlib.pyplot as plt
import seaborn as sns
import os

def is_stationary(data):
    result = adfuller(data)
    p_value = result[1]
    return p_value < 0.05

def plot_rolling_mean_variance(data, window, title, path_to_save):
    rolling_mean = data.rolling(window).mean()
    rolling_variance = data.rolling(window).var()
    plt.figure(figsize=(8, 6))
    plt.plot(rolling_mean, color="red", label="rolling mean")
    plt.plot(rolling_variance, color="orange", label="rolling variance")
    plt.title(title)
    plt.legend(loc="upper right")
    plt.savefig(path_to_save)
    plt.show()