# 📊 Multivariate Forecasting of Scotland’s Monthly Birth Rates

This repository contains a complete machine learning pipeline for forecasting Scotland’s monthly birth rates using multivariate time series data derived from health, education, and economic indicators. The project involves data preprocessing, feature engineering, multiple model implementations, and performance evaluation using MAE and RMSE.

---

## 📁 Dataset

- The data was collected and merged from multiple domains.
- Contains monthly features along with historical birth records.
- Stored as `final_merged_dataset.csv`.

---

## 🧠 Models Implemented

- VAR (Vector Autoregression)
- Random Forest Regressor
- XGBoost Regressor
- LightGBM Regressor
- LSTM (Long Short-Term Memory)
- GRU (Gated Recurrent Units)
- TCN (Temporal Convolutional Network)

---

## 🏆 Best Model

After extensive evaluation:

> ✅ **GRU (Gated Recurrent Unit)** achieved the best results with the **lowest Mean Absolute Error (MAE)** and **Root Mean Square Error (RMSE)**.

This makes GRU the optimal choice for forecasting Scotland's monthly birth rates among the tested models.

---

## 📈 Evaluation Metrics

Each model was evaluated using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)

These metrics were used to generate a comparative performance table and visualizations.

---

## 📊 Visualizations

- Forecast vs Actual plots for each model
- Comparative bar charts of MAE and RMSE

---

---

🚀 Deployment

Current Deployment

Platform: Streamlit

Status: ✅ Live

URL: https://4uhzuxtxjzezgxhqtzjchn.streamlit.app/

Auto-deploy: Manual updates (redeploy when new code or dataset is pushed)

---

## 🛠️ Tools & Libraries

- **Python** (Pandas, NumPy, Seaborn, Matplotlib)
- **Machine Learning**: Scikit-learn, XGBoost, LightGBM
- **Deep Learning**: TensorFlow (LSTM, GRU, TCN)
- **Notebook Platform**: Google Colab

---

## 🔧 How to Use

1. Clone this repository
2. Open the notebook in [Google Colab](https://colab.research.google.com/)
3. Upload the `final_merged_dataset.csv` or generate your own dataset
4. Run the notebook cells to train and evaluate models

---

## 📬 Contact

For questions or collaborations, feel free to reach out via GitHub Issues or Pull Requests.

