from sklearn.metrics import root_mean_squared_error, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error

def evaluate_model(test_data, predictions):
    '''
    This function calculates and returns RMSE, MSE, MAE, and MAPE
    The function returns a dictionary
    '''
    rmse = root_mean_squared_error(test_data, predictions)
    mse = mean_squared_error(test_data, predictions)
    mae = mean_absolute_error(test_data, predictions)
    mape = mean_absolute_percentage_error(test_data, predictions)
    metrics =  {
        "rmse": rmse, 
        "mse": mse,
        "mae": mae, 
        "mape": mape
    }
    return metrics

def residuals(model_fit):
    return model_fit.resid