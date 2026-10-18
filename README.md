
<div align="center">

<h1>Forex Price Direction Predictor LSTM</h1>

<p>
  A machine learning application that analyzes economic news headlines and numerical indicators to estimate forex market direction using a Bidirectional LSTM regression model.
</p>

<p>
  Developed as a machine learning project exploring natural language processing, time-sensitive economic events, and financial market prediction.
</p>

<p>
  <img src="https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/TENSORFLOW-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow" />
  <img src="https://img.shields.io/badge/KERAS-D00000?style=for-the-badge&logo=keras&logoColor=white" alt="Keras" />
  <img src="https://img.shields.io/badge/STREAMLIT-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/SCIKIT--LEARN-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn" />
  <img src="https://img.shields.io/badge/PANDAS-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/NUMPY-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/JUPYTER-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter" />
</p>

<p>
  <a href="https://github.com/johncarlonas/Forex-Price-Direction-Predictor-Using-LSTM">Source Code</a>
</p>

</div>

---

## Overview

**Forex Price Direction Predictor Using LSTM** is a machine learning project designed to analyze economic news events and estimate how currency pairs might react to economic data releases.

The system combines natural language processing with numerical economic indicators to predict the actual value of an economic release. It then compares the predicted value against the forecast to generate a directional market indication.

The project integrates a trained Bidirectional Long Short-Term Memory (BiLSTM) neural network with a Streamlit web interface, allowing users to enter economic news information and generate predictions locally.

It explores the application of deep learning to financial information, particularly how economic headlines and quantitative indicators can be processed together.

## Features

### Economic News Analysis

- Processes economic news headlines using text preprocessing and tokenization.
- Converts textual information into numerical sequences for neural network input.
- Uses learned word embeddings to represent economic event descriptions.
- Supports financial headlines and economic indicators in a single prediction workflow.

### Machine Learning Predictions

- Uses a trained Bidirectional LSTM regression model.
- Combines textual features with numerical economic indicators.
- Estimates the actual percentage value of an economic release.
- Compares predicted actual values against forecast values.
- Generates directional indications based on the predicted economic surprise.

### Interactive Web Application

- Streamlit-powered prediction interface.
- Input fields for economic news and forecast values.
- Currency and trading pair selection.
- Impact classification using High, Medium, and Low categories.
- Displays predicted actual values and directional indications.
- Provides explanations based on the selected currency pair's base and quote positions.

## Tech Stack

| Technology | Purpose |
| --- | --- |
| Python | Data preprocessing, model training, and application logic |
| TensorFlow | Deep learning computation and model execution |
| Keras | Neural network architecture and model training |
| Bidirectional LSTM | Learning contextual patterns from tokenized news headlines |
| Scikit-learn | Data scaling, train-test splitting, and evaluation |
| Pandas | Dataset loading and preprocessing |
| NumPy | Numerical operations and model input preparation |
| Streamlit | Interactive web application |
| Matplotlib | Training and evaluation visualizations |
| Joblib | Serialization of preprocessing objects |
| Jupyter Notebook | Model experimentation, training, and evaluation |

## Machine Learning Methodology

The project uses a multi-input regression model combining textual and numerical economic information.

### 1. Dataset Preparation

Historical economic news records are loaded from:

`data/forex_news.xlsx`

The dataset is prepared by:

1. Removing completely empty records.
2. Excluding holiday events.
3. Parsing actual and forecast percentage values.
4. Removing records with missing required numerical values.
5. Mapping economic impact categories into numerical scores.
6. Normalizing news headlines.
7. Removing duplicate observations.

The cleaned dataset provides the features used during model training.

### 2. Feature Engineering

The model accepts two groups of input features.

**Textual Features**

Economic event headlines are converted into lowercase text and normalized by removing punctuation.

The headlines are tokenized using the Keras Tokenizer with:

| Parameter | Value |
| --- | --- |
| Vocabulary limit | 20,000 words |
| Sequence length | 80 tokens |
| Padding | Post-padding |
| Out-of-vocabulary token | `<OOV>` |

**Numerical Features**

The model uses two numerical inputs:

| Feature | Description |
| --- | --- |
| Forecast | Expected percentage value of an economic release |
| Impact Score | Economic event importance represented numerically |

Impact categories are encoded as:

| Impact | Encoded Value |
| --- | --- |
| Low | 1 |
| Medium | 2 |
| High | 3 |

The numerical features are standardized using Scikit-learn's `StandardScaler`.

### 3. Model Architecture

The project implements a multi-input Bidirectional LSTM regression network using TensorFlow and Keras.

The text-processing branch consists of:

- Embedding layer with 128-dimensional representations.
- Gaussian noise regularization.
- Bidirectional LSTM with 128 units.
- Dropout regularization.

The numerical branch receives the standardized forecast and impact score, with Gaussian noise applied during training.

Both branches are concatenated and passed through fully connected layers.

| Component | Configuration |
| --- | --- |
| Embedding | 20,000 vocabulary size, 128 dimensions |
| Recurrent Layer | Bidirectional LSTM, 128 units |
| LSTM Dropout | 0.2 |
| Recurrent Dropout | 0.2 |
| Dense Hidden Layer | 128 units, ReLU activation |
| L2 Regularization | 0.001 |
| Batch Normalization | Enabled |
| Output Layer | 1 neuron, linear activation |
| Optimizer | Adam |
| Learning Rate | 0.0005 |
| Loss Function | Mean Squared Error |
| Training Metric | Mean Absolute Error |

The model predicts a numerical economic release value rather than directly generating a currency price.

### 4. Training Configuration

The training notebook uses the following configuration:

| Parameter | Value |
| --- | --- |
| Train-test split | 80% / 20% |
| Split method | GroupShuffleSplit |
| Grouping feature | Economic headline |
| Validation split | 20% of training partition |
| Maximum epochs | 30 |
| Batch size | 16 |
| Early stopping patience | 5 |
| Early stopping monitor | Validation loss |

The grouped split separates matching headlines between the training and test partitions.

Early stopping monitors validation performance and restores the best recorded model weights.

### 5. Model Evaluation

The training notebook reports the following regression evaluation results:

| Metric | Recorded Result |
| --- | ---: |
| Mean Absolute Error (MAE) | 1.5128 |
| Root Mean Squared Error (RMSE) | 2.0708 |

These values are taken from the saved notebook's held-out test evaluation.

They measure the regression model's prediction error for economic release values. They do not represent forex trading profitability, trading accuracy, or independently validated market-direction accuracy.

## Market Direction Logic

The application derives its directional indication by comparing the model's predicted actual value with the entered forecast.

```python id="urfp16"
movement = int(actual_pred > forecast_val)
```

The comparison is interpreted as:

| Condition | Directional Indication |
| --- | --- |
| Predicted actual > Forecast | Positive economic surprise |
| Predicted actual <= Forecast | Non-positive economic surprise |

The interface then adjusts its displayed pair-direction indication based on whether the affected currency is the base or quote currency.

For example, for a positive indication:

- If the affected currency is the base currency, the interface suggests upward pair movement.
- If the affected currency is the quote currency, the interface suggests downward pair movement.

This is a simplified directional heuristic. Economic indicators can have different interpretations, so a higher actual value does not universally imply currency appreciation.

The application does not calculate a future exchange rate or use a live market-price feed.

## Project Structure

```text id="acw2mo"
Forex-Price-Direction-Predictor-Using-LSTM/
├── data/
│   └── forex_news.xlsx
├── models/
│   └── regression_forex_price.h5
├── notebooks/
│   └── FP_Nas_BSCS2A.ipynb
├── utils/
│   ├── scaler.pkl
│   └── tokenizer.pkl
├── app.py
└── README.md
```

### Directory Descriptions

- **`data/`** contains the economic news dataset used during model development.
- **`models/`** contains the saved trained Keras regression model.
- **`notebooks/`** contains the notebook used for data preprocessing, training, evaluation, and visualization.
- **`utils/`** contains the serialized tokenizer and numerical scaler.
- **`app.py`** provides the Streamlit application and prediction interface.

## Getting Started

Follow the steps below to run the prediction application locally.

### Prerequisites

Install the following:

- [Python](https://www.python.org/downloads/) with a TensorFlow-compatible version
- [Git](https://git-scm.com/)

Python 3.11 is a reasonable starting point for creating a compatible environment.

### 1. Clone the Repository

```bash id="xjl8ym"
git clone https://github.com/johncarlonas/Forex-Price-Direction-Predictor-Using-LSTM.git
```

Navigate into the project:

```bash id="yx4mvi"
cd Forex-Price-Direction-Predictor-Using-LSTM
```

### 2. Create a Virtual Environment

**Windows (PowerShell)**

```powershell id="7p5707"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash id="3qylke"
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

The repository does not currently contain a `requirements.txt` file.

Install the packages required by the Streamlit application:

```bash id="ga5ds0"
python -m pip install --upgrade pip
python -m pip install streamlit numpy tensorflow scikit-learn joblib
```

The included `.h5` file uses the legacy Keras HDF5 model format. Loading it may require a compatible TensorFlow/Keras version.

### 4. Run the Application

Start the Streamlit application:

```bash id="2w7csh"
python -m streamlit run app.py
```

Open the local address displayed in the terminal, typically:

```text id="u2m1p0"
http://localhost:8501
```

The application loads the trained model and preprocessing objects from the repository's `models/` and `utils/` directories.

## How to Use

1. Enter an economic news headline in the **News Title** field.
2. Select the **Affected Currency**.
3. Choose the economic event's **Impact Type**.
4. Enter the expected **Forecast Value (%)**.
5. Select the currency pair you want to analyze.
6. Enter the **Current Price**.
7. Click **Predict Direction**.

The application displays:

- The model's predicted actual economic release value.
- A directional market reaction indication.
- A pair-specific suggestion based on the affected currency's position.

The current price is collected by the interface but is not used as a model input in the current prediction implementation.

## Model Training and Experimentation

The model development notebook is located at:

`notebooks/FP_Nas_BSCS2A.ipynb`

To explore it locally, install the additional notebook dependencies:

```bash id="eg0vb9"
python -m pip install jupyterlab pandas openpyxl matplotlib
```

Start JupyterLab:

```bash id="ws8eib"
python -m jupyter lab
```

Open the notebook from the `notebooks/` directory.

The notebook includes:

- Dataset loading and cleaning.
- Feature engineering and text normalization.
- Tokenization and numerical scaling.
- Training and test partitioning.
- Model architecture configuration.
- Neural network training.
- Regression evaluation.
- Training and validation visualizations.
- Model serialization.

**Reproduction note:** The notebook currently loads the dataset using an absolute Windows file path. Update that path to point to the repository's `data/forex_news.xlsx` before rerunning the training pipeline.

The notebook saves the generated model and preprocessing files in its execution directory. Move or save them to the corresponding `models/` and `utils/` directories if you want to use newly trained artifacts with `app.py`.

## Project Limitations

This project is an experimental financial machine learning application.

Its current limitations include:

- Predictions are based on historical economic event patterns, not live forex exchange-rate data.
- The system predicts economic release values and derives directional indications using a simplified comparison rule.
- The model does not directly forecast future exchange-rate prices.
- The application does not calculate trading profitability, position size, or risk exposure.
- The saved evaluation metrics measure regression error, not trading performance.
- Predictions can be affected by economic events, volatility, and changing market conditions.
- The training notebook fits preprocessing objects before the train-test split, which should be revised for stricter evaluation.

The application is intended for educational and experimental use, not as an automated trading or financial advisory system.

## Future Improvements

Potential improvements include:

- Real-time financial news and market data integration.
- More extensive directional classification and evaluation.
- Indicator-aware economic surprise interpretation.
- Chronological validation for financial forecasting.
- Improved preprocessing and training reproducibility.
- Model comparison with alternative neural networks and machine learning methods.
- Automated dependency management and reproducible environments.
- More comprehensive backtesting and model monitoring.

## Project Background

This project was developed as part of my exploration of machine learning and financial forecasting.

I wanted to investigate how natural language processing and deep learning could be combined to analyze economic information and produce interpretable predictions.

Through this project, I gained experience in:

- Preparing real-world structured datasets.
- Processing textual and numerical data for machine learning.
- Building multi-input neural network architectures.
- Training and evaluating LSTM regression models.
- Saving and loading machine learning models.
- Integrating trained models into an interactive web application.

---

<div align="center">

**Forex Price Direction Predictor Using LSTM**

A machine learning and financial forecasting project.

</div>
