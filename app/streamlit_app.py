import streamlit as st
import joblib

# Load model and vectorizer once
model = joblib.load(r'C:\Users\iqra khan\OneDrive\Desktop\MSC\mental health classifier\mental_health_classifier.pkl')
tfidf = joblib.load(r'C:\Users\iqra khan\OneDrive\Desktop\MSC\mental health classifier\tfidf_vectorizer.pkl')

# Prediction function
def predict(text):
    x = tfidf.transform([text])
    return model.predict(x)[0]

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mental Health Chat Classifier", layout="centered", page_icon="🧠")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: white;
        }
        h1, h2, h3, h4 {
            color: #f8f9fa;
            text-align: center;
        }
        .stTextArea>div>textarea {
            background-color: #1e1e1e;
            color: white;
            border: 2px solid #d63384;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #6f42c1;
            color: white;
            border-radius: 10px;
            padding: 0.5em 2em;
            font-size: 1em;
        }
        .result {
            background-color: #198754;
            padding: 1em;
            border-radius: 10px;
            font-weight: bold;
            color: white;
            text-align: center;
            margin-top: 1em;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("ℹ️ About")
    st.markdown("""
        This app uses machine learning to classify mental health chat messages.
        
        **Model**: Logistic Regression / SVM  
        **Vectorizer**: TF-IDF  
        **Categories**: Normal, Anxious, Depressed, etc.

        Developed with ❤️ using Streamlit.
    """)

# --- MAIN APP ---
st.title("🧠 Mental Health Chat Classifier")
user_input = st.text_area("💬 Enter your chat/message:", height=150)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Predict"):
        prediction = predict(user_input)
        st.markdown(f"<div class='result'>Predicted Mental Health Status: {prediction}</div>", unsafe_allow_html=True)
