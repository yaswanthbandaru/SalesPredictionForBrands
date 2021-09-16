# SalesPredictionForBrands
Prediction day wise sales of Six brands

## Data
---
Data consists of 3 columns **'Transaction_date','Brand Name', 'Sales Value'**

## Data Manipulation

## Model Selection
There are many ways to model a time series in order to make predictions. We are going use following models:

* moving average
* exponential smoothing
* ARIMA
## Exponential smooting

$y=\alpha x_t + (1-\alpha) y_{t-1}, t>0$

## Double exponential smoothing

*Mathematically:*

$y=\alpha x_t + (1 - \alpha) (y_{t-1} + b_{t-1})$

$b_t=\beta (y_t - y_{t-1})  + (1 - \beta)b_{t-1}$


