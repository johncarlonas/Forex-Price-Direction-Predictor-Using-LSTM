# Hybrid LSTM-Logistic Regression Model for Forex Forecasting

A real-time financial forecasting system predicting forex reactions to economic news using a hybrid LSTM and Logistic Regression model. Deployed using Streamlit with integration of NLP and numerical analysis.

---

## System Features

### User Interface
* **Streamlit-Powered Web App:** Features real-time prediction results.
* **Simple Input Fields:** Easily input news title, forecast value, impacted currency, and other relevant metrics.
* **Instantaneous Output:** Immediate display of predicted actual value and market direction.
* **Optimized UI:** Fast and intuitive interface designed for traders operating under time-sensitive events.

### Model Functionality
* **Hybrid Architecture:** Combines LSTM and Logistic Regression for forecasting.
* **Advanced NLP:** Utilizes NLP for financial news preprocessing and semantic embedding.
* **Directional Logic:** Features directional prediction logic based on actual vs. forecast economic values.
* **Robust Training Data:** Trained on the comprehensive ForexFactory dataset (2007–2023).
* **Feature Fusion:** Fuses text data with numerical data (including impact and surprise value).
* **Regularization & Processing:** Implements tokenization, sequence embedding, and Gaussian noise regularization.

---

## Technology Stack

| Category | Technologies |
| :--- | :--- |
| **Backend** | Python (TensorFlow, Scikit-learn, Pandas, NumPy) |
| **Frontend** | Streamlit |
| **NLP** | Natural Language Toolkit (NLTK), Tokenizers |
| **Modeling** | LSTM (Keras), Logistic Regression (Sklearn) |
| **Visualization** | Matplotlib, Seaborn |

---

## Project Structure

```text
├── app.py              # Main Streamlit app for real-time predictions
├── models/             # Trained model weights and tokenizers
├── data/               # Raw and cleaned economic news datasets
├── notebooks/          # Jupyter notebooks for EDA and training
├── utils/              # Data preprocessing, tokenizer, and scaler modules
├── results/            # Visual evaluation results (graphs, charts)
└── README.md           # Project documentation
