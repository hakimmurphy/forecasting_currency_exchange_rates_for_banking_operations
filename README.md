# 💹 Forecasting Currency Exchange Rates for Banking Operations

## Project Overview
This project forecasts **SGD/USD** and **CNY/USD** exchange rates to support banking operations. It compares several time series and machine learning models for forecasting accuracy:

## Dataset
  - Missing values handled (forward/backward fill)
  - Renamed columns for clarity
  - Converted data types for analysis

## Methodology
1. **Exploratory Data Analysis (EDA):**
   - Visualize trends, volatility, and co-movement
   - Stationarity tests (ADF, KPSS)
   - ACF/PACF analysis
2. **Modeling:**
   - Baseline: Naïve and ARIMA models
   - Advanced: XGBoost, LSTM, TFT (with calendar covariates)
3. **Evaluation:**
   - Metrics: RMSE, MAE, MAPE
   - Visual comparison of predictions vs actuals

## Results

## How to Run
1. **Install dependencies:**
   - Run the first notebook cell to install required packages:
     ```bash
     pip install darts
     ```
2. **Open and run the notebook:**
   - `forecasting_currency_exchange_rates_for_banking_operations.ipynb`
   - Follow the cells sequentially for data analysis, modeling, and results.

## File Structure

## References

Feel free to fork, use, or extend this project for your own forecasting and analytics needs!

# 💹 Forecasting Currency Exchange Rates for Banking Operations

## Project Overview

This project forecasts **SGD/USD** and **CNY/USD** exchange rates to support banking operations. It compares several time series and machine learning models for forecasting accuracy:

- **ARIMA** (statistical baseline)
- **XGBoost** (feature-based ML)
- **LSTM** (deep learning sequence model)
- **TFT** (Transformer-based deep learning model)

## Dataset

- **Source:** `Foreign_Exchange_Rates.csv`
- **Features:** Daily exchange rates for SGD/USD and CNY/USD
- **Preprocessing:**
  - Missing values handled (forward/backward fill)
  - Renamed columns for clarity
  - Converted data types for analysis

## Methodology

1. **Exploratory Data Analysis (EDA):**
   - Visualize trends, volatility, and co-movement
   - Stationarity tests (ADF, KPSS)
   - ACF/PACF analysis

2. **Modeling:**
   - Baseline: Naïve and ARIMA models
   - Advanced: XGBoost, LSTM, TFT (with calendar covariates)

3. **Evaluation:**
   - Metrics: RMSE, MAE, MAPE
   - Visual comparison of predictions vs actuals

## Results

- ARIMA with drift outperforms naïve baseline for both SGD/USD and CNY/USD.
- Advanced models (XGBoost, LSTM, TFT) are explored for richer dynamics and improved accuracy.

## How to Run

1. **Install dependencies:**

   - Run the first notebook cell to install required packages:

     ```bash
     pip install darts
     ```

2. **Open and run the notebook:**

   - `forecasting_currency_exchange_rates_for_banking_operations.ipynb`
   - Follow the cells sequentially for data analysis, modeling, and results.

## File Structure

- `forecasting_currency_exchange_rates_for_banking_operations.ipynb`: Main analysis and modeling notebook
- `Foreign_Exchange_Rates.csv`: Dataset
- `xgb_best_cny.darts`, `xgb_best_sgd.darts`: Saved model files

## References

- [Darts Time Series Library](https://github.com/unit8co/darts)
- [Optuna Hyperparameter Optimization](https://optuna.org/)

---

## 📄 License
MIT

---

## 🗣️ Author
Hakim Murphy
