HYBRID LSTM-LOGISTIC REGRESSION MODEL FOR FOREX FORECASTING  
A real-time financial forecasting system predicting forex reactions to economic news using a hybrid LSTM and Logistic Regression model.  
Deployed using Streamlit with integration of NLP and numerical analysis.

🔍 SYSTEM FEATURES

👤 USER INTERFACE  
• Streamlit-powered web app with real-time prediction results  
• Simple input fields: news title, forecast value, impacted currency, etc.  
• Immediate output of predicted actual value and market direction  
• Fast and intuitive interface for traders under time-sensitive events  

🛠 MODEL FUNCTIONALITY  
• Hybrid LSTM + Logistic Regression forecasting model  
• NLP for financial news preprocessing and semantic embedding  
• Directional prediction logic based on actual vs. forecast economic values  
• Trained on ForexFactory dataset (2007–2023)  
• Feature fusion: text + numerical data (impact, surprise value)  
• Tokenization, sequence embedding, Gaussian noise regularization  

🛠 TECHNOLOGY STACK  
Backend:     Python (TensorFlow, Scikit-learn, Pandas, NumPy)  
Frontend:    Streamlit  
NLP:         Natural Language Toolkit (NLTK), Tokenizers  
Modeling:    LSTM (Keras), Logistic Regression (Sklearn)  
Visualization: Matplotlib, Seaborn  

📁 PROJECT STRUCTURE

Key Files & Folders:  
• app.py                     - Main Streamlit app for real-time predictions  
• model/                    - Trained model weights and tokenizers  
• data/                     - Raw and cleaned economic news datasets  
• notebooks/                - Jupyter notebooks for EDA and training  
• utils/                    - Data preprocessing, tokenizer, scaler modules  
• results/                  - Visual evaluation results (graphs, charts)  
• requirements.txt          - All required dependencies  
• README.txt                - You are reading it 😉  

⚙️ SETUP & RUN

Python version required: 3.8+

1. Create and activate virtual environment (optional but recommended):
   python -m venv venv  
   source venv/bin/activate  (Linux/Mac)  
   .\venv\Scripts\activate   (Windows)

2. Install dependencies:  
   pip install -r requirements.txt

3. Run the application:  
   streamlit run app.py

4. Use the interface to input economic news and see predictions instantly.

⚠️ LIMITATIONS  
• Model assumes historical patterns will repeat—forex is inherently volatile  
• Forecasts are directional, not full price predictions  
• Predictions may vary for currencies with low representation in dataset  
• No trading automation or broker integration included  

🚀 FUTURE IMPROVEMENTS  
• Integrate real-time news scraping via APIs  
• Add sentiment analysis from social media and headlines  
• Implement Transformer-based alternatives (e.g., FinBERT)  
• Extend to regression-based price prediction with actual pip ranges  
• Deploy in trading environments for live testing and improvement  

👨‍💻 DEVELOPER  
John Carlo E. Nas  
📧 jonas@my.cspc.edu.ph  
