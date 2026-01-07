import streamlit as st
import joblib
import numpy as np
from scipy.sparse import hstack
from scipy.sparse import csr_matrix

# data=joblib.load("training_data.pkl")
tfidf = joblib.load("tfidf.pkl")
clf = joblib.load("final_clf.pkl")
reg = joblib.load("final_reg.pkl")

keywords = ["greedy","dp","dynamic programming","tree","graph","dfs","bfs","two pointers","binary search","bitmasks","dfs","combinatorics"]
def extra_features(text):
    return [
        len(text),
        len(text.split()),
        sum(text.count(k) for k in keywords),
        sum(1 for c in text if c in "+-*/%")
    ]



st.set_page_config(page_title="AutoJudge", layout="centered")
st.title("AutoJudge : The Difficulty Predictor 🔍")
st.write("Predict programming problem difficulty using text description")
title = st.text_input("Problem Title")
description = st.text_area("Problem Description")
input_desc = st.text_area("Input Description")
output_desc = st.text_area("Output Description")


if st.button("Predict Difficulty"):
    if description.strip() == "":
        st.warning("Please enter a problem description.")
    else:
        user_input = ("__TITLE__" + title +
        " __DESCRIPTION__" + description + 
        " __INPUT__" + input_desc +
        " __OUTPUT__" + output_desc)

        user_input.lower().strip()

        x_text = tfidf.transform([user_input])
        x_extra = extra_features(user_input)
        x_extra = csr_matrix(x_extra)
        x_final = hstack([x_text, x_extra])

        pred_class = clf.predict(x_final)[0]
        pred_score = reg.predict(x_final)[0]
        
        class_median={"easy": 2.0, "medium": 4.1, "hard":7.0}
        final_pred_score = 0.7*pred_score + 0.3*class_median[pred_class]
        
        st.success(f"Predicted Difficulty: 📈**{pred_class}**")
        st.info(f"Predicted Score: 🔢**{int(final_pred_score)}**")
