import streamlit as st
import pandas as pd

st.title(" E-commerce Recommendation System")

# input
product = st.text_input("Enter product name")

if st.button("Recommend"):
    
    recommendations = ["Product A", "Product B", "Product C"]

    st.subheader("Recommended Products:")
    for r in recommendations:
        st.write("👉", r)