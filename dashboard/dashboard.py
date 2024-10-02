import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

main_data = pd.read_csv('dashboard/main_data.csv')
main_data['dteday'] = pd.to_datetime(main_data['dteday'])
st.title('Dashboard Penggunaan Sepeda - Bike Sharing Dataset')
st.subheader('Filter Data Berdasarkan Periode')

start_date = st.date_input('Tanggal Mulai', main_data['dteday'].min())
end_date = st.date_input('Tanggal Akhir', main_data['dteday'].max())

filtered_data = main_data[(main_data['dteday'] >= pd.to_datetime(start_date)) & 
                          (main_data['dteday'] <= pd.to_datetime(end_date))]

# Bagian 1: Tabel Data
st.subheader('Tabel Data Utama')
st.write(filtered_data.head())

# Bagian 2: Visualisasi 1 - Tren Penggunaan Sepeda Setiap Bulan
st.subheader('Tren Penggunaan Sepeda Setiap Bulan')
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_data, x='month', y='cnt', ci=None, marker="o")
plt.title('Tren Penggunaan Sepeda Setiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot(plt)

# Bagian 3: Visualisasi 2 - Pengaruh Cuaca Terhadap Pengguna Sepeda (Optimized)
st.subheader('Pengaruh Cuaca Terhadap Jumlah Pengguna Sepeda')
sampled_data = filtered_data.sample(frac=0.2, random_state=42)
plt.figure(figsize=(8, 5))
sns.barplot(data=sampled_data, x='weathersit', y='cnt')
plt.title('Pengaruh Cuaca Terhadap Jumlah Pengguna Sepeda (Sampled)')
plt.xlabel('Kategori Cuaca (1: Cerah, 2: Mendung, 3: Hujan)')
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot(plt)

# Bagian 4: Visualisasi 3 - Penggunaan Sepeda Pada Hari Kerja vs Hari Libur
st.subheader('Penggunaan Sepeda Pada Hari Kerja vs Hari Libur')
plt.figure(figsize=(10, 6))
sns.boxplot(data=filtered_data, x='workingday', y='cnt')
plt.title('Penggunaan Sepeda Pada Hari Kerja vs Hari Libur')
plt.xlabel('Hari Kerja (0: Libur, 1: Kerja)')
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot(plt)
