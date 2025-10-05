 House Price Prediction (India)

Predict house prices in India instantly using a Machine Learning model** via an **interactive Streamlit app. Enter house details and get an estimated price in real time!  

Try the live app here:[🔗 Streamlit App](https://housepriceprediction-hznrntiw7q5uagxomvpwni.streamlit.app/)

---
Features

- Predicts price based on **bedrooms, bathrooms, living area, condition, and grade**  
- Interactive Streamlit app** for instant predictions  
- Random Forest Regressor** trained with **hyperparameter tuning** for accurate results  
- Cross-platform model loading** using `cloudpickle`  
- Clean and simple **UI for easy user interaction**

---

## 📁 Project Structure
│
├─ app/ # Streamlit app code
├─ models/ # Saved trained model (HPmodel.pkl)
├─ notebooks/ # Jupyter Notebook (training & preprocessing)
├─ data/ # Dataset used for training
├─ requirements.txt # Dependencies
└─ README.md # Project documentation


---

## 🏃 How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/arcinth/HousePricePrediction.git
cd HousePricePrediction
pip install -r requirements.txt
streamlit run app/app.py
```

---
Technologies Used

Python 3.x

Pandas, NumPy, Matplotlib

Scikit-learn (Random Forest Regressor)

Cloudpickle (cross-platform model serialization)

Streamlit (web app UI)

---
Author

Arcinth Siva

GitHub: arcinth

---
License
This project is open-source and free to use under the MIT License.

