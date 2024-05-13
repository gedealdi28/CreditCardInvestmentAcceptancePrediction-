import pandas as pd
import streamlit as st
import joblib

def app():
    st.title('Prediksi Apakah Nasabah akan Investasi Bank Term Deposit ')

    model = joblib.load("xgb_best.pkl")

    # Input form
    with st.form ('Form Data Pelanggan'):
        age = st.number_input('Age', min_value=18)
        job = st.selectbox('Job', ['unemployed', 'services', 'management', 'blue-collar', 'self-employed', 'entrepreneur', 'technician', 'admin'])
        marital = st.selectbox('Marital', ['married', 'single', 'divorced'])
        education = st.selectbox('Education', ['primary', 'secondary', 'tertiary'])
        default = st.selectbox('Default', ['yes', 'no'])
        balance = st.number_input('Balance', min_value=0)
        housing = st.selectbox('Housing', ['yes', 'no'])
        loan = st.selectbox('Loan', ['yes', 'no'])
        contact = st.selectbox('Contact', ['cellular', 'telephone', 'unknown'])
        day = st.number_input('Day', min_value=1, max_value=31)
        month = st.selectbox('Month', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        duration = st.number_input('Duration', min_value=0)
        campaign = st.number_input('Campaign', min_value=0)
        pdays = st.number_input('Pdays', min_value=-1)
        previous = st.number_input('Previous', min_value=0)
        poutcome = st.selectbox('Poutcome', ['success', 'failure', 'other', 'unknown'])
        y = st.selectbox('Y', ['1', '0'])
        
        sub= st.form_submit_button('Submit Data')

        # Jika tombol Submit ditekan
        if sub:
            # Membuat data input
            data_inf = {
                'age': [age],
                'job': [job],
                'marital': [marital],
                'education': [education],
                'default': [default],
                'balance': [balance],
                'housing': [housing],
                'loan': [loan],
                'contact': [contact],
                'day': [day],
                'month': [month],
                'duration': [duration],
                'campaign': [campaign],
                'pdays': [pdays],
                'previous': [previous],
                'poutcome': [poutcome],
                'y': [y]
            }
            df = pd.DataFrame(data_inf)

            # Memprediksi menggunakan model
            prediksi = model.predict(df)
            if prediksi[0] == 0:
                hasil = 'This Customer will likely reject our offer'
            elif prediksi[0] == 1:
                hasil = 'This Customer will likely accept our offer'

            st.write(hasil)

if __name__ == "__main__":
    app()
