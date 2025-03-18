import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import time
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

st.title("Live Bitcoin Price Prediction")

ticker = "BTC-USD"
model = load_model("crypto_model.keras")
scaler = MinMaxScaler(feature_range=(0, 1))

def fetch_data():
    data = yf.download(ticker, period="1d", interval="1m")
    return data[['Close']].dropna()

def predict_next_price():
    data = fetch_data()
    scaled_data = scaler.fit_transform(data)
    last_60 = scaled_data[-60:].reshape(1, 60, 1)
    predicted_price = model.predict(last_60)
    return scaler.inverse_transform(predicted_price)[0, 0]

price_chart = st.line_chart([])

while True:
    next_price = predict_next_price()
    price_chart.add_rows([[next_price]])
    time.sleep(5)
