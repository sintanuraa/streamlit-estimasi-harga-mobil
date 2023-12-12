import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Kilometer Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size Mobil')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineZise]]
    )
    st.write ('Estimasi harga mobil bekas dalam Ponds : ', predict)
    st.write ('Estimasi harga mobil bekas dalam IDR (Juta) : ', predict*17000)