import streamlit as st

st.title("Title")
st.text("Text")

# Input nama dari pengguna
nama = st.text_input('Masukkan nama Anda')
nim = st.text_input('Masukkan NIM Anda')
inikota = st.selectbox("Pilih Matakuliah Anda:", {'RPL', 'IF', 'DS'})
umur = st.slider("Masukan Umur anda", 1,100,20)

# Tombol untuk menampilkan sapaan
if st.button('Enter'):
    #st.write(f'Halo, {nama}! Selamat datang di Streamlit.')
    if nama and nim and inikota and umur:
        st.text("Nama :"+nama)
        if len(nim) != 10:
            st.text("error")
        else:
            st.text("NIM  : {nim}")
        st.text("Kota :"+inikota)
        st.text("Umur :", umur)


#inikota = st.selectbox("Pilih Matakuliah Anda:", {'RPL', 'IF', 'DS'})
#st.write(inikota)

#umur = st.slider("Masukan Umur anda", 1,100,20)
#st.write(umur)

gender = st.radio("Gender", {'LAKI', 'Wanita'})
st.write(gender)

if gender == "LAKI" :
    st.write("Selamat datang bapak :", nama)
else :
    st.write("Selamat datang ibu :", nama)

list_hobi = st.text_area("Hobi", "Makan, Minum, Tidur, Berak")
list_hobi = [x.strip() for x in list_hobi.split(',')]
st.write(list_hobi)

st.image("https://cdn0-production-images-kly.akamaized.net/D7ZP3GfIPGwm-HOXGjNxIH1DMg4=/640x360/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/4219701/original/009682100_1667963905-GettyImages-1068070022-cc640df4be4d4c3a8b4356f76beeee60.jpg", caption="Ini Apa?")

st.markdown('[Jangan Di Klik](https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran)')

import pandas as pd
data = {'Pekerjaan' : ["Programer", "Doktor", "Kang Parkir"],
        'Tier' : ["A", "S", "S+"]}
df = pd.DataFrame(data)

st.dataframe(df)

st.title("Buka Data")
file = st.file_uploader("Pilih File", type=['jpg', 'csv'])

if file is not None:
    st.write(file.type)
    if file.type == 'image/jpeg' :
        st.image(file)
    else :
        dataData = pd.read_csv(file)
        st.dataframe(dataData)

st.title('Kalkulator Sederhana')
angka1 = st.number_input("Masukan Angka 1", value=0)
angka2 = st.number_input("Masukan Angka 2", value=0)

operasi = st.radio('Pilih operasi matematika', ['Penjumlahan (+)', 'Pengurangan (-)', 'Perkalian (*)', 'Pembagian (/)'])

if st.button('Hitung'):
    if operasi == 'Penjumlahan (+)':
        hasil = angka1 + angka2
    elif operasi == 'Pengurangan (-)':
        hasil = angka1 - angka2
    elif operasi == 'Perkalian (*)':
        hasil = angka1 * angka2
    elif operasi == 'Pembagian (/)':
        if angka2 == 0:
            hasil = "Tidak bisa dibagi dengan 0"
        else:
            hasil = angka1 / angka2
    st.success(f"Hasil {operasi} {hasil}")


st.sidebar.header("Fitur Kiri")

if st.sidebar.checkbox("Biodata") :
    st.sidebar.write(f"Nama: {nama}")