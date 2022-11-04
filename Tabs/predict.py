"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Renal Disease Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    bp = st.slider("Blood Pressure", int(df["Bp"].min()), int(df["Bp"].max()))
    al = st.slider("Albumin", int(df["Al"].min()), int(df["Al"].max()))
    sc = st.slider("Sugar Content", float(df["Su"].min()), float(df["Su"].max()))
    rbc = st.slider("Red Blood Cells", float(df["Rbc"].min()), float(df["Rbc"].max()))
    pc = st.slider("Pus Cell", int(df["Bu"].min()), int(df["Bu"].max()))
    pcc = st.slider("Pus Cell Clumps", int(df["Sc"].min()), int(df["Sc"].max()))
    bc = st.slider("Bacteria Count", int(df["Sod"].min()), int(df["Sod"].max()))
    pot = st.slider("Blood Glucose Potential", int(df["Pot"].min()), int(df["Pot"].max()))
    hl = st.slider("Haemoglobin Level", int(df["Hemo"].min()), int(df["Hemo"].max()))
    wbcc = st.slider("White Blood Cell Count", int(df["Wbcc"].min()), int(df["Wbcc"].max()))
    rbcc = st.slider("Red Blood Cell Count", int(df["Rbcc"].min()), int(df["Rbcc"].max()))
    hr = st.slider("Hypertension Rating", int(df["Htn"].min()), int(df["Htn"].max()))

    # Create a list to store all the features
    features = [bp,al,sc,rbc,pc,pcc,bc,pot,hl,wbcc,rbcc,hr]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get renal disease!!")
        else:
            st.success("The person is relatively safe from renal disease")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
