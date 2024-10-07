import pandas as pd
import streamlit as st
import pickle

cars_df = pd.read_csv("./cars24-car-price.csv")

st.write(
    """
     # Cars24 Used Car Price Prediction
    """
)
st.dataframe(cars_df.head())

## Encoding Categorical features
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select the fuel type",
                           ["Diesel", "Petrol", "CNG", "LPG", "Electric"])

engine = col1.slider("Set the Engine Power",
                     500, 5000, step=100)

transmission_type = col2.selectbox("Select the transmission type",
                                   ["Manual", "Automatic"])

seats = col2.selectbox("Enter the number of seats",
                       [4,5,7,9,11])

def model_pred(encoded_fuel_type,encoded_transmission_type, engine, seats):
    with open ("car_pred_model", 'rb') as file:
        loaded_model = pickle.load(file)

        input_features = [[2012.0,2,120000,encoded_fuel_type,encoded_transmission_type,19.7,engine,46.3,seats]]

        return loaded_model.predict(input_features)

if st.button("Predict Price"):
    encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
    encoded_transmission_type = encode_dict['transmission_type'][transmission_type]

    price = model_pred(encoded_fuel_type,encoded_transmission_type, engine, seats)

    st.header("Predicted Price is: "+str(price))

#series of columns within with my model will accept input
#[2012.0,Individual,120000,Petrol,Manual,19.7,796.0,46.3,5.0]

#encoded_accepted_format
#[2012.0,2,120000,encoded_fuel_type,encoded_transmission_type,19.7,engine,46.3,seats]


