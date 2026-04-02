from statsmodels.tsa.statespace.sarimax import SARIMAX

# This will be put in modeling python files
def train_sarima(train_data, order, seasonal_order, s): 
    '''
    Note that order and seasonal_order must be tuples, train_data must be a time-series, and s an integer
    '''
    # Load SARIMA model
    model = SARIMAX(
        train_data, 
        order = (p, d, q),
        seasonal_order = (P, D, Q, s)
    )
    
    # Train the model
    model_fit = model.fit()
    return model_fit

def forecast(model_fit, test_data):
    predictions = model_fit.get_forecast(steps=test_data.size)
    return predictions.predicted_mean