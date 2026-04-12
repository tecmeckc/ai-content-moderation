import streamlit as st
import pickle

# Load model
model = pickle.load(open('model.pkl','rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))

labels = ['toxic','obscene','threat','insult','identity_hate']

# 🔴 Category-wise harmful words
insult_words = [
    "asshole", "idiot", "stupid", "dumb", "moron",
    "loser", "shut up", "fuck", "fuck off",
    "bitch", "bastard"
]

threat_words = [
    "kill you", "i will kill", "hurt you",
    "i will hurt", "destroy you", "i will destroy"
]

# 🟢 Safe words
safe_words = [
    "cutiepie", "love", "cute", "sweet",
    "nice", "beautiful", "good", "great"
]


# 🧠 Interpret result
def interpret_result(pred):
    detected = [label for label, val in zip(labels, pred) if val == 1]
    
    if not detected:
        return "✅ This comment is SAFE"
    
    if 'threat' in detected or 'identity_hate' in detected:
        return f"🚨 HIGH RISK: Contains {', '.join(detected)}"
    
    return f"⚠️ WARNING: This comment may be {', '.join(detected)}"


# 🔥 Keyword override
def keyword_override(text, prediction):
    text = text.lower()
    
    for word in insult_words:
        if word in text:
            prediction[3] = 1   # insult
            prediction[0] = 1   # toxic
    
    for word in threat_words:
        if word in text:
            prediction[2] = 1   # threat
            prediction[0] = 1   # toxic
    
    return prediction


# 🟢 Safe override
def safe_override(text, prediction):
    text = text.lower()
    
    for word in safe_words:
        if word in text:
            return [0, 0, 0, 0, 0]
    
    return prediction


# ⭐ Severity
def severity_level(pred):
    score = sum(pred)
    
    if score == 0:
        return "Low"
    elif score <= 2:
        return "Medium"
    else:
        return "High"


# 🎨 UI
st.set_page_config(page_title="AI Content Moderation", page_icon="🛡️")

st.title("🛡️ AI Content Moderation System")
st.write("Enter a comment below to analyze its toxicity level.")

text = st.text_area("💬 Enter your comment:")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter a comment.")
    else:
        vec = tfidf.transform([text])
        probs = model.predict_proba(vec)

        threshold = 0.3
        prediction = [1 if p > threshold else 0 for p in probs[0]]

        prediction = keyword_override(text, prediction)
        prediction = safe_override(text, prediction)

        result = interpret_result(prediction)
        severity = severity_level(prediction)

        # 🎨 Colored Output
        if "SAFE" in result:
            st.success(result)
        elif "WARNING" in result:
            st.warning(result)
        else:
            st.error(result)

        st.subheader(f"Severity Level: {severity}")