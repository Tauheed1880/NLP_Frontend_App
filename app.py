import streamlit as st
import requests

st.title("SMS Spam Detector")

message = st.text_area("Enter SMS")

if st.button("Predict"):
    url = "https://tauheed1880-nlp-spam-app.hf.space/predict"

    response = requests.post(
        url,
        params={"message": message}
    )

    if response.status_code == 200:
        result = response.json()
        prediction = result.get("prediction")

        if prediction == 1:
            st.error("SPAM")
        else:
            st.success("HAM")
    else:
        st.error("Backend error")
