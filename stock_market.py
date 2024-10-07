import streamlit as st
import yfinance as yf
import datetime


ticker_symbol = st.text_input("Please enter the ticker", "AAPL")
ticker_data = yf.Ticker(ticker_symbol)

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Please enter the starting date", datetime.date(2022, 1, 1))

with col2:
    end_date = st.date_input("Please enter the ending date", datetime.date(2023, 1, 1))



ticker_df = ticker_data.history(period="1d", start=start_date,
                                end=end_date)

st.title("Stock Price Analyzer!")
st.write("Here's the raw day wise stock movement: ")
st.dataframe(ticker_df)

st.write("Price Movement over Time")
st.line_chart(ticker_df['Close'])

st.write("Volume Movement over Time")
st.line_chart(ticker_df['Volume'])
