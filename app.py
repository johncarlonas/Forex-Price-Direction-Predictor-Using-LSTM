import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# --- Load real model and preprocessing objects ---
model = load_model("models/regression_forex_price.h5")
tokenizer = joblib.load("models/tokenizer.pkl")
scaler = joblib.load("models/scaler.pkl")

# --- Streamlit UI ---
st.set_page_config(page_title="Forex News Impact Prediction", layout="centered")
st.title("📰 Forex News Price Direction Predictor")

# --- Inputs ---
news_title = st.text_input("News Title")
currency = st.selectbox("Affected Currency", ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "NZD"])
impact = st.selectbox("Impact Type", ["High", "Medium", "Low"])
impact_score = {"Low": 1, "Medium": 2, "High": 3}[impact]
forecast = st.text_input("Forecast Value (%)", help="Enter numeric percentage (e.g., 0.5 for 0.5%)")

def generate_pairs(base):
    others = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "NZD"]
    others.remove(base)
    return [f"{base}/{o}" for o in others] + [f"{o}/{base}" for o in others]

pairs = generate_pairs(currency)
selected_pair = st.selectbox("Pair You Want to Trade", pairs)
current_price = st.text_input("Current Price", help="Enter the current price of the selected pair")

# --- Prediction Logic ---
if st.button("Predict Direction"):
    if not news_title or not forecast or not current_price:
        st.warning("Please fill in all fields.")
    else:
        try:
            forecast_val = float(forecast)
            current_price_val = float(current_price)
        except ValueError:
            st.error("Forecast and Current Price must be numeric.")
        else:
            # --- Clean and tokenize news title ---
            clean_title = news_title.lower().strip()
            clean_title = ''.join(c if c.isalnum() or c.isspace() else '' for c in clean_title)
            seq = tokenizer.texts_to_sequences([clean_title])
            padded = pad_sequences(seq, maxlen=80, padding='post')

            # --- Predict actual value ---
            numeric_input = np.array([[forecast_val, impact_score]])
            numeric_scaled = scaler.transform(numeric_input)
            actual_pred = model.predict([padded, numeric_scaled])[0][0]

            # --- Determine direction ---
            movement = int(actual_pred > forecast_val)

            st.success(f"📈 Predicted Actual Value: {actual_pred:.2f}%")

            if movement == 1:
                direction = "⬆️ UP (Price Likely to Rise)"
            else:
                direction = "⬇️ DOWN (Price Likely to Drop)"
            st.info(f"Predicted Market Reaction: {direction}")

            # --- Trading pair advice ---
            if f"{currency}/" in selected_pair:
                st.write("Since the currency is on the **left** side of the pair:")
                if movement == 1:
                    st.success("💹 Suggestion: Price may go UP")
                else:
                    st.error("📉 Suggestion: Price may go DOWN")
            else:
                st.write("Since the currency is on the **right** side of the pair:")
                if movement == 1:
                    st.error("📉 Suggestion: Price may go DOWN")
                else:
                    st.success("💹 Suggestion: Price may go UP")
