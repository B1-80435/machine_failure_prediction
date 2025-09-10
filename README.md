# ⚙️ Machine Failure Prediction  

This project focuses on predicting **machine failures** using advanced **machine learning models** and visualizing results through an interactive **Streamlit dashboard**. It combines **data preprocessing, feature engineering, model training, and risk visualization** to provide actionable insights for predictive maintenance.  

---

## 📂 Project Structure  

- **`machine_failure_prediction.py`** → Core ML pipeline  
  - Data cleaning & preprocessing  
  - Feature engineering (temperature ratios, torque-speed relations, stress index, etc.)  
  - Exploratory analysis (density plots, correlations)  
  - Model training with **RandomForest, XGBoost, LightGBM, CatBoost**  
  - Hyperparameter tuning with cross-validation  
  - Final predictions with optimized CatBoost  

- **`mfdb.py`** → Streamlit dashboard  
  - Displays KPIs (total maintenances, avg risk, high-risk machines)  
  - Risk distribution & categorization  
  - Top 5 risky machines  
  - Maintenance schedules & filters  

- **`train.csv` / `test.csv`** → Training and testing datasets  

---

## 🚀 Features  

- **Data Engineering:** Cleaning, encoding, and feature creation for better signal extraction.  
- **Imbalanced Data Handling:** Class weights and recall-focused model optimization.  
- **Modeling:** Evaluated multiple ML models, selected **CatBoost** for best recall.  
- **Visualization:** Interactive Streamlit dashboard with Plotly charts.  
- **Insights:** Identify high-risk machines, schedule maintenance, and prioritize resources.  

---

## 🛠️ Tech Stack  

- **Python** (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)  
- **Machine Learning:** XGBoost, LightGBM, CatBoost, RandomForest  
- **Visualization:** Streamlit, Plotly  
- **Data Storage:** CSV datasets  

---

## 📊 Dashboard Preview  

Run the dashboard locally:  

```bash
streamlit run mfdb.py
```

It will launch a web app showing:  
- KPIs on machine risks  
- Risk distribution & categories  
- Top risky machines  
- Maintenance schedule with filtering  

---

## 📈 Model Performance  

- Best model: **CatBoostClassifier**  
- Primary metric: **Recall** (to minimize missed failures)  
- Achieved high ROC-AUC and strong recall on validation set  

---

## ▶️ How to Run  

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/machine-failure-prediction.git
   cd machine-failure-prediction
   ```
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the ML pipeline (training & evaluation)  
   ```bash
   python machine_failure_prediction.py
   ```
4. Launch the dashboard  
   ```bash
   streamlit run mfdb.py
   ```

---

## 📌 Future Improvements  

- Deploy dashboard on **Streamlit Cloud / Docker**  
- Integrate with real-time IoT sensor streams  
- Implement alerting system for high-risk predictions  

---

## 👨‍💻 Author  

**Tanzeel Mansuri**  
- Data Engineer | Data Scientist | BI Enthusiast  
- [LinkedIn](https://linkedin.com/in/tanzeel-mansuri) | [GitHub](https://github.com/B1-80435)  
