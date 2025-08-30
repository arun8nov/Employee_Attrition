# Employee Attrition and Performance Prediction Dashboard  

## 📌 Project Overview  
This project analyzes employee attrition trends and predicts both **Attrition likelihood** and **Performance Rating** using machine learning models. It also includes an interactive **Streamlit dashboard** to visualize insights and make predictions at both **individual** and **batch (file upload)** levels.  

The main goals of this project are:  
- Clean and preprocess employee HR datasets  
- Analyze attrition patterns with visualizations (gender, department, education, job roles, etc.)  
- Build ML models for:  
  - **Attrition Prediction** (Random Forest, Logistic Regression, Decision Tree with class imbalance handling)  
  - **Performance Rating Prediction** (Logistic Regression)  
- Provide an **interactive dashboard** for HR teams to:  
  - Explore attrition factors  
  - Predict attrition risk for employees  
  - Predict performance ratings  

---

## 📂 Project Structure  

```
├── __pycache__/  
├── .venv/  
├── Analyze.ipynb                 # EDA & initial analysis  
├── app.py                        # Main Streamlit app  
├── Att_Model.pkl                 # Trained Attrition model  
├── Att_Preprocess.pkl            # Attrition preprocessing pipeline  
├── Att_Predi.ipynb               # Notebook for Attrition model training  
├── PR_Model.pkl                  # Performance Rating model  
├── PR_Preprocess.pkl             # Performance preprocessing pipeline  
├── Perfo_Predi.ipynb             # Notebook for Performance model training  
├── dash.py                       # Plotly charts (visualization class)  
├── Fun.py                        # Data cleaning & selection class  
├── Dash_Report.md                # Dashboard analysis notes/report  
├── Employee_Attrition.pdf        # Dataset reference/documentation  
├── requirements.txt              # Python dependencies  
├── README.md                     # Project documentation  
└── icon.png                      # App icon/logo  
```

---

## ⚙️ Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/employee-attrition-prediction.git
cd employee-attrition-prediction
```

### 2️⃣ Create Virtual Environment & Install Dependencies  
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App  
```bash
streamlit run app.py
```

---

## 🛠️ Features  

✅ **Data Cleaning** – Handles duplicates, standardizes column names, and prepares data subsets  
✅ **Exploratory Data Analysis (EDA)** – Visualizations for attrition trends (department, education, job role, etc.)  
✅ **Attrition Prediction Model** – Random Forest with class imbalance handling  
✅ **Performance Rating Model** – Logistic Regression model for predicting ratings (1–4)  
✅ **Interactive Dashboard** – Built with **Streamlit + Plotly**  
✅ **File Upload Support** – Predict attrition or performance for a batch of employees from CSV  

---

## 📊 Dashboard Pages  

- **🏠 Home** – Overview with filters and employee stats  
- **📈 Analyse** – Visual EDA (gender, department, education, job role, attrition trends)  
- **📊 Dashboard Report** – Predefined analysis summary  
- **⚠️ Attrition Prediction** – Form & file upload for attrition prediction  
- **⭐ Performance Rating Prediction** – Form & file upload for performance rating prediction  

---

## 📦 Models  

- **Attrition Prediction**  
  - Preprocessing: `Att_Preprocess.pkl`  
  - Model: `Att_Model.pkl` (Random Forest)  

- **Performance Rating Prediction**  
  - Preprocessing: `PR_Preprocess.pkl`  
  - Model: `PR_Model.pkl` (Logistic Regression)  

---

## 📌 Requirements  

Main Python Libraries:  
- `pandas`, `numpy`  
- `matplotlib`, `seaborn`, `plotly`  
- `scikit-learn`, `imbalanced-learn`  
- `streamlit`  
- `nbformat`  

Install using:  
```bash
pip install -r requirements.txt
```



## 👨‍💻 Author  
Developed by **[Arunprakash B]** ✨  
For HR analytics and workforce management solutions.  
