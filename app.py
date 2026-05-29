import streamlit as st
import requests

st.title("SMS Spam & Phishing Detector")
st.write("Enter any SMS message below to check if it is safe or spam.")

message = st.text_area(
    "SMS Message",
    placeholder="e.g. Congratulations! You won a free iPhone. Click here to claim now!"
)

if st.button("Predict"):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        url = "https://tauheed1880-nlp-spam-app.hf.space/predict"

        response = requests.post(url, json={"message": message})

        if response.status_code == 200:
            result = response.json()
            prediction = result.get("prediction")

            if prediction == 1:
                st.error("SPAM / PHISHING This message looks malicious!")
            else:
                st.success("SAFE (HAM) This message looks legitimate.")
        else:
            st.error("Backend error. Please check API.")
