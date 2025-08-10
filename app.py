import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
model = joblib.load("airbnb_price_model.pkl")

# App title
st.title("Paris Airbnb Price Predictor 💶")
st.markdown("Enter listing details to estimate the nightly price.")

# User input
room_type = st.selectbox("Room Type", ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room'])

neighbourhood = st.selectbox("Neighbourhood", [
    'Buttes-Montmartre', 'Louvre', 'Popincourt', 'Batignolles-Monceau',
    'Vaugirard', 'Panthéon', 'Temple', 'Palais-Bourbon', 'Élysée',
    'Observatoire', 'Bourse', 'Passy', 'Gobelins', 'Reuilly', 'Opéra'
])

minimum_nights = st.number_input("Minimum Nights", min_value=1, max_value=365, value=3)
availability_365 = st.slider("Availability (days/year)", 0, 365, 200)

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        'room_type': room_type,
        'neighbourhood_cleansed': neighbourhood,
        'minimum_nights': minimum_nights,
        'availability_365': availability_365
    }])

    predicted_price = model.predict(input_df)[0]
    st.success(f"💰 Estimated Price: €{predicted_price:.2f} per night")