import streamlit as st
import pandas as pd
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

def main():
    st.title('Predict Credit Card Default')

    # Input fields for each variable
    LIMIT_BAL = st.number_input('LIMIT_BAL')
    SEX = st.number_input('SEX')
    EDUCATION = st.number_input('EDUCATION')
    MARRIAGE = st.number_input('MARRIAGE')
    AGE = st.number_input('AGE')
    PAY_0 = st.number_input('PAY_0')
    PAY_2 = st.number_input('PAY_2')
    PAY_3 = st.number_input('PAY_3')
    PAY_4 = st.number_input('PAY_4')
    PAY_5 = st.number_input('PAY_5')
    PAY_6 = st.number_input('PAY_6')
    BILL_AMT1 = st.number_input('BILL_AMT1')
    BILL_AMT2 = st.number_input('BILL_AMT2')
    BILL_AMT3 = st.number_input('BILL_AMT3')
    BILL_AMT4 = st.number_input('BILL_AMT4')
    BILL_AMT5 = st.number_input('BILL_AMT5')
    BILL_AMT6 = st.number_input('BILL_AMT6')
    PAY_AMT1 = st.number_input('PAY_AMT1')
    PAY_AMT2 = st.number_input('PAY_AMT2')
    PAY_AMT3 = st.number_input('PAY_AMT3')
    PAY_AMT4 = st.number_input('PAY_AMT4')
    PAY_AMT5 = st.number_input('PAY_AMT5')
    PAY_AMT6 = st.number_input('PAY_AMT6')

    # Predict button
    if st.button('Predict'):
        data_dict = {
            'LIMIT_BAL': LIMIT_BAL,
            'SEX': SEX,
            'EDUCATION': EDUCATION,
            'MARRIAGE': MARRIAGE,
            'AGE': AGE,
            'PAY_0': PAY_0,
            'PAY_2': PAY_2,
            'PAY_3': PAY_3,
            'PAY_4': PAY_4,
            'PAY_5': PAY_5,
            'PAY_6': PAY_6,
            'BILL_AMT1': BILL_AMT1,
            'BILL_AMT2': BILL_AMT2,
            'BILL_AMT3': BILL_AMT3,
            'BILL_AMT4': BILL_AMT4,
            'BILL_AMT5': BILL_AMT5,
            'BILL_AMT6': BILL_AMT6,
            'PAY_AMT1': PAY_AMT1,
            'PAY_AMT2': PAY_AMT2,
            'PAY_AMT3': PAY_AMT3,
            'PAY_AMT4': PAY_AMT4,
            'PAY_AMT5': PAY_AMT5,
            'PAY_AMT6': PAY_AMT6
        }
        
        data = CustomData(data_dict)
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)

        result = round(pred[0], 2)

        st.write(f'The predicted credit card default is {result}')

if __name__ == "__main__":
    main()
