# 🛡️ AI Content Moderation System

## 📌 Overview
The AI Content Moderation System is a machine learning-based web application that detects and classifies toxic, abusive, and harmful comments.  

It uses a hybrid approach combining:
- Machine Learning (TF-IDF + Logistic Regression)
- Rule-based keyword detection  

The system provides clear outputs:
- ✅ SAFE  
- ⚠️ WARNING  
- 🚨 HIGH RISK  

---

## 🚀 Features

- Detects multiple categories:
  - Toxic
  - Obscene
  - Threat
  - Insult
  - Identity Hate  

- Machine Learning Model:
  - TF-IDF Vectorization  
  - Logistic Regression (One-vs-Rest)

- Hybrid Approach:
  - ML predictions + keyword-based overrides  

- Interactive UI:
  - Built using Streamlit  
  - Color-coded outputs  

- Severity Level:
  - Low / Medium / High  

---

## 🛠️ Tech Stack

- Python  
- Scikit-learn  
- NLTK  
- Pandas  
- Streamlit  

---

## 📂 Project Structure
AI-Content-Moderation/
│
├── app.py
├── model.pkl
├── tfidf.pkl
├── requirements.txt
└── README.md
---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/your-username/ai-content-moderation.git

cd ai-content-moderation

### 2. Install dependencies

pip install -r requirements.txt

### 3. Download NLTK data

import nltk
nltk.download('stopwords')


### 4. Run the application

streamlit run app.py


---

## 🌐 Deployment

The application is deployed using Streamlit Cloud.

Live Link: (Add your deployed link here)

---

## 🧪 Example Outputs

| Input                | Output |
|---------------------|--------|
| Hello friend        | ✅ SAFE |
| You are an idiot    | ⚠️ WARNING |
| I will kill you     | 🚨 HIGH RISK |

---

## 💡 How It Works

1. User enters a comment  
2. Text is processed using TF-IDF  
3. Logistic Regression predicts probabilities  
4. Thresholding converts probabilities into labels  
5. Rule-based overrides improve detection  
6. Final result and severity level are displayed  

---

## ⚠️ Limitations

- Does not fully understand context  
- May produce false positives/negatives  
- Limited handling of sarcasm  

---

## 🔮 Future Improvements

- Use advanced models like BERT  
- Add multilingual support  
- Improve dataset quality  
- Real-time moderation system  

---

## 👩‍💻 Author

Khyati Choudhary  
B.Tech CSE | Web Development & AI Enthusiast  

---

## ⭐ Conclusion

This project demonstrates how machine learning and rule-based systems can be combined to build a practical and user-friendly content moderation tool.
