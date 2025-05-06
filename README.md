
# 🪙 Bitcoin Price Prediction using RNN, GRU, and LSTM

This project focuses on predicting Bitcoin prices using deep learning models — RNN, GRU, and LSTM — trained on historical time-series data. The LSTM model achieved the best performance and is showing predictions via an interactive **Streamlit** web interface.

##  Project Highlights

-  Developed and compared RNN, GRU, and LSTM models.
-  LSTM achieved the lowest RMSE: **1907** vs. **2580+** (RNN/GRU).
-  Built a **Streamlit** web app to visualize LSTM predictions in real-time.
-  Captures long-term dependencies effectively for time-series forecasting.

## Tech Stack

- Python
- TensorFlow / Keras
- NumPy / Pandas / Matplotlib
- Streamlit


##  Model Evaluation

| Model | RMSE   |
|-------|--------|
| RNN   | ~2580  |
| GRU   | ~2600  |
| LSTM  | **1907** |

![bitcoin1](https://github.com/user-attachments/assets/30367208-23fb-4c7e-8b37-3cbdddbf2d28)
![bitcoin2](https://github.com/user-attachments/assets/d2449f5f-2858-4936-b92a-bb57d67fbf4b)
![bitcoin3](https://github.com/user-attachments/assets/07394acd-f05b-4ccc-9af2-bade9042abd1)



## 🛠️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/bitcoin-price-prediction.git
   cd bitcoin-price-prediction
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
