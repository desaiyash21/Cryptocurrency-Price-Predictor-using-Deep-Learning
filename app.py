import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from datetime import datetime

# Load the saved GRU model
model = load_model("crypto_model.keras")

# Define the time_step (number of past days to use for prediction)
time_step = 60  # You can adjust this value as needed

# Function to fetch Bitcoin data using yfinance
def fetch_data():
    ticker = "BTC-USD"
    end = datetime.now()
    start = datetime(end.year - 15, end.month, end.day)  # 15 years ago

    # Fetch Bitcoin data
    data = yf.download(ticker, start=start, end=end)

    if data.empty:
        raise ValueError("No data fetched from Yahoo Finance. Check the ticker symbol or your internet connection.")

    # Fix for MultiIndex issue: Flatten the column names
    data.columns = [col[0] for col in data.columns]

    # Use only the 'Close' column
    data = data[['Close']].dropna()
    return data

# Function to preprocess data
def preprocess_data(data, time_step=60):
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data)
    return scaler, data_scaled

# Function to predict future prices
def predict_future(model, last_data, scaler, future_days=30):
    future_predictions = []
    input_seq = last_data[-time_step:].reshape(1, time_step, 1)

    for _ in range(future_days):
        pred = model.predict(input_seq)[0][0]
        future_predictions.append(pred)
        new_input = np.append(input_seq[:, 1:, :], [[[pred]]], axis=1)
        input_seq = new_input

    return scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))

# Streamlit app
def main():
    st.set_page_config(page_title="Bitcoin Price Prediction", page_icon="📈", layout="wide")

    st.title("📈 Bitcoin Price Prediction")
    st.write("Predict future Bitcoin prices using a **LSTM model** trained on historical data.")

    # Sidebar for user input
    st.sidebar.title("Settings")
    future_days = st.sidebar.slider("Select number of days to predict:", 1, 60, 30)

    if st.sidebar.button("Predict Future Prices"):
        with st.spinner("Fetching data and making predictions..."):
            try:
                # Fetch and preprocess data
                data = fetch_data()
                scaler, data_scaled = preprocess_data(data, time_step)

                # Predict future prices
                future_predictions = predict_future(model, data_scaled, scaler, future_days)
                future_dates = pd.date_range(start=data.index[-1], periods=future_days + 1, freq='D')[1:]
                predictions_df = pd.DataFrame({'Date': future_dates, 'Predicted Price': future_predictions.flatten()})

                # Display historical data
                st.subheader("📜 Historical Bitcoin Prices")
                st.line_chart(data)

                # Display predictions
                st.subheader("📅 Future Price Predictions")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Predicted Price on Start Date", f"${predictions_df.iloc[0]['Predicted Price']:.2f}")
                with col2:
                    st.metric("Predicted Price on End Date", f"${predictions_df.iloc[-1]['Predicted Price']:.2f}")

                # Plot predictions
                st.subheader("📊 Prediction Chart")
                st.line_chart(predictions_df.set_index('Date'))

                # Show predictions table
                st.subheader("📝 Predictions Table")
                st.dataframe(predictions_df)

            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()