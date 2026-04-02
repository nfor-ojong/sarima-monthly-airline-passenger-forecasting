import pandas as pd
import numpy as np
import os

# Put this notebook in the python file
def load_data(path_to_data):
    data = pd.read_csv(path_to_data)
    return data

def clean_data(data):
    '''
    This function takes the loaded dataset and applies necessary cleaning techniques to it and
    returns a new dataset
    '''
    # Sort values by time
    data = data.sort_values(by="Month") # Sort values by time
    # Verify if time steps are consistent
    data["time"] = pd.to_datetime(data["Month"], errors="coerce")
    time_diffs = data["time"].diff(1)
    month_diffs = np.round(time_diffs.dt.days / 30)
    # If time steps are consistent, then the maximum and minimum values of month_diffs must be one
    is_time_consistent = month_diffs.min() == month_diffs.max() == 1
    print("Is time consistent: ", is_time_consistent)
    
    # Remove outliers from data
    clean_data = remove_outliers(data["Passengers"])
    #print("Clean data shape: ", clean_data.shape)
    
    clean_data = pd.DataFrame(
        {
            "time": data["time"],
            "Passengers": clean_data
        }
    )
    # Set time column as index
    clean_data = clean_data.set_index("time")
    clean_data.describe()
    
    print("Shape of clean data: ", clean_data.shape)
    # Save clean data
    clean_data.to_csv(os.path.join(r"C:\Users\pad market\Desktop\airline-passenger-forecasting\data", "cleaned_data.csv"))
    return clean_data
    
def remove_outliers(data):
    data = data.copy() # Do not modify the= original time-series
    mean = data.mean()
    std = data.std()
    z_scores = (data - mean) / std
    data.loc[np.abs(z_scores) >=3] = data.median()
    return data
