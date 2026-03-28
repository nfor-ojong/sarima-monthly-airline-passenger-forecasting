# **Time-Series Forecasting of Monthly Passenger Counts with Full Residual Diagnostics**
## **Project Overview**
This project demonstrates the use of **SARIMA (Seasonal ARIMA)** to forecast monthly airline passenger counts using the classical publicly available **Airline Passenger Dataset**. The project covers data cleaning, visualization, stationarity analysis, model fitting, and forecast with evaluation.
## **Problem Description**
This project aims to forecast monthly airline passenger counts using statistical time-series models. The dataset shows a clear seasonal pattern and an upward trend, making it suitable for SARIMA modeling. We aim to analyze the data, handle non-stationarity, and generate reliable forecasts that capture both trend and seasonality, demonstrating the effectiveness of SARIMA in time-series forecasting.  
## **Dataset**
Name: Airline Passenger Dataset  
Source: https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv  
Frequency: Monthly  
### **Description**
Records the number of passengers travelling each month from **1949** to **1960**  
Exhibits trend and seasonality (Periodicity of 12 months)  

## **Project Goals**
1. Perform data preprocessing and make it ready for exploratory data analysis (EDA)  
2. Explore and visualize the time-series  
3. Perform stationarity checks and apply differencing if needed  
4. Fit a **SARIMA model** to capture trend and seasonality  
5. Forecast future passenger counts for the next **15 months**  
6. Compare predictions with actual values and evaluate model performance using metrics such as **RMSE, MAE, MSE, and MAPE**  
7. Perform residual analysis to validate reliability of forecasts  
## **Methodology**
The analysis followed a structured time-series workflow in which the dataset was first prepared and indexed by time. Stationarity was then assessed using visual inspection and statistical tests such as the augemented Dickey-Fuller test. Log-transformation was applied to remove heteroskedasticity (variance changing with time), and differencing was also applied to make the time-series stationary in the mean.  

The model parameters were indentified through autocorrelation (ACF) and partial autocorrelation (PACF) analysis, after which a SARIMA model fitted to capture the underlying dynamics (trend and seasonality). The trained model was used to forecast the number of airline passengers for the next **15 months**. The model was validated using residual diagnostics, and its performance was evaluated using root mean squared error (RMSE), mean absolute error (MAE), mean squared error (MSE), and mean absolute percentage error (MAPE). 
## **Results (Performance Metrics)**
The model demonstrated good performance with the following performance metrics: 

1. RMSE: 12.73
2. MAE: 9.33
3. MSE: 162.0
4. MAPE: 0.02
5. Residual mean: 0.02  
6. Residual variance: 0.22  
## **Key Insights**
The model was able to capture the overall dynamics of the time-series, producing stable and consistent forecasts. Residual diagnostics indicated that most of the autocorrelations were removed, suggesting a good model fit. Overall, the results demonstrate that SARIMA is well-suited for modeling time-series with clear seasonal patterns and trend components.  
## **Limitations**
Despite the overall good performance, residual analysis showed a remaining correlation at lag 12, indicating that the model did not fully the seasonal component. Consequently, the distribution of the residuals did not match that of white noise excellently. This suggests that the chosen SARIMA configuration, although guided by ACF and PACF analysis, may not perfectly model all seasonal dependencies in the data. Additionally, SARIMA assumes linear relationships and may struggle with more complex or nonlinear patterns. Further improvements could involve refining hyperparameters, incorporating additional seasonal structures, or exploring alternative models like **Prophet** for better performance. 