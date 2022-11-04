"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Renal Disease Predictor")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Kidney failure is a condition in which one or both of your kidneys no longer work on their own. Causes include diabetes, high blood pressure and acute kidney injuries. Symptoms include fatigue, nausea and vomiting, swelling, changes in how often you go to the bathroom and brain fog. Treatment includes dialysis or a kidney transplant.Dialysis or a kidney transplant can help you continue to live a long life. Your treatment plan may also include taking medications and following a special diet. Be sure to go to all of your appointments. Talk to a healthcare provider if you have any questions or concerns about your treatments, medications, lifestyle change or any other part of your treatment plan.
        </p>
    """, unsafe_allow_html=True)