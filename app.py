import streamlit as st
import requests

st.title("SMS Spam & Phishing Detector")
st.write("Enter any SMS message below to check if it is safe or spam.")

message = st.text_area("SMS Message", placeholder="e.g. Congratulations! You won a free iPhone. Click here to claim now!")

if st.button("Predict"):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        data = {"message": message}
        response = requests.post("https://tauheed1880-nlp-spam-app.hf.space", params=data)
        result = response.json()

        if result["prediction"] == 1:
            st.error("SPAM / PHISHING This message looks malicious!")
        else:
            st.success("SAFE (HAM) This message looks legitimate.")
