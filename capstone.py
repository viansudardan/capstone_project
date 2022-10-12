import streamlit as st
import pandas as pd
#import yfinance as yf
#import fontstyle as tx
#import matplotlib.pyplot as plt
#import shap
#from sklearn import datasets
#from sklearn.ensemble import RandomForestRegressor
from datetime import datetime
import pandas as pd
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive
#import requests
#from io import BytesIO
#import xlrd 

#st.title("Dampak Inflasi AS terhadap Perekonomian Indonesia")
#st.set_page_config(layout='wide')
#st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)
#st.image("/Users/vianbeladona/Desktop/inflation.jpg")

st.markdown("<h1 style='text-align: center; color: black;'>Dampak Inflasi AS terhadap Perekonomian Indonesia</h1>", unsafe_allow_html=True)
st.write('---')
st.write("""
Made with **streamlit** by Novianto Sudardan
""")
st.markdown("Kondisi perekonomian dunia saat ini tengah mengalami guncangan hebat akibat dari kondisi yang kian tidak menentu, dimulai dari krisis kesehatan global akibat pandemi yang terjadi pada awal tahun 2020, kemudian dilanjutkan dengan pecahnya perang yang terjadi antara Rusia dan Ukrania yang menyebabkan supply disruption terhadap berbagai komoditas di beberapa negara, konflik yang berkepanjangan ini menyebabkan efek domino, tidak hanya memicu krisis energi tetapi juga krisis pangan, sehingga hal ini menyebabkan terjadinya inflasi global, beberapa negara kemudian menyikapinya dengan mengeluarkan kebijakan seperti pengetatan kebijakan moneter untuk mengurangi dampak negatif yang ditimbulkan akibat isu geopolitik yang terjadi saat ini.")
st.markdown("Tidak terlepas dari kondisi krisis, Amerika Serikat (AS) sebagai negara superpower pun terkena imbas dari isu ini, Pada bulan Juni 2022, Biro Statistik Tenaga Kerja AS (Bureau of Labor Statistics) mencatat tingkat inflasi sempat menembus laju tertingginya sepanjang tahun 2022 pada nilai 9,1%, ini adalah level tertinggi dalam 40 tahun terakhir, bahkan jika keadaan terus memburuk tidak menutup kemungkinan akan menyebabkan resesi. Tercatat AS pernah mencatat tingkat inflasi tertinggi sepanjang sejarah sebesar 12,3% pada bulan Desember 1974. Adapun kebijakan yang diambil oleh pemerintah AS melalui Bank Sentral nya, The Federal Reserve (The Fed) pada saat itu adalah dengan menaikan suku bunga acuan. Data pada bulan Agustus 2022 mencatat tingkat inflasi AS menurun menjadi 8,3%, namun ini masih tergolong tinggi, hal ini mendorong The Fed meningkatkan suku bunga acuan menjadi 3,25% pada bulan September 2022")
#url = 'https://docs.google.com/spreadsheets/d/1uySLhqVWYaoWhIBjqxFzakGmw3F3Wiea/export?format=xlsx'
#sheet_id = '1ADVWW9yneU5kaOveB0Hdht__bgDp3Poe'
#df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
#df = pd.read_excel('https://docs.google.com/spreadsheets/d/1uySLhqVWYaoWhIBjqxFzakGmw3F3Wiea/edit?usp=sharing&ouid=102342643769211379317&rtpof=true&sd=true')
#wb = xlrd.open_workbook('https://github.com/viansudardan/capstone_project/blob/main/DataInflasiAS.xlsx')
df = pd.read_excel('./DataInflasiAS.xlsx')
df['Periode'] = pd.to_datetime(df['Periode'])

#public_gsheets_url = "https://docs.google.com/spreadsheets/d/1apCe5kVwegEpP6Zhs821wzoaiC5BHKAT8F5ySI5sXqM/edit?usp=sharing"

#df2 = df.drop([''], axis = 1)
st.subheader('Tingkat Inflasi AS')
#st.dataframe(df)

inflasi = df[['Periode', 'Data Inflasi']].set_index('Periode')
#plt.grid()
#plt.show()
st.line_chart(inflasi)

st.subheader('Suku Bunga Acuan The Fed')

#df2 = pd.read_excel('/Users/vianbeladona/Desktop/tetris/suku_bunga_the_fed.xlsx')

#df2['Bulan'] = pd.to_datetime(df2['Bulan'])

#sukubunga = df2[['Bulan', 'Suku Bunga']].set_index('Bulan')
#plt.grid()
#plt.show()
#st.line_chart(sukubunga)

st.markdown('Peningkatan suku bunga di AS dapat memicu aliran modal global akan meninggalkan negara berkembang termasuk Indonesia (capital outflow). Investor berbondong-bondong akan menginvestasikan modalnya pada pasar modal di AS, karena tergiur dengan kenaikan suku bunga tersebut. Dampak yang ditimbulkan adalah nilai tukar rupiah yang akan semakin melemah terhadap dollar AS.')
#st.caption('Spearman Rank Correlation Result rho = 0.861')
#st.markdown('Terbukti bahwa inflasi di AS memiliki korelasi positif yang kuat terhadap nilai tukar rupiah dengan koefisien korelasi sebesar 0.86')

st.subheader('Nilai Tukar Mata Uang Rupiah')
#df3 = pd.read_excel('/Users/vianbeladona/Desktop/tetris/Kurs_Rupiah.xlsx')

#df3['Tanggal'] = pd.to_datetime(df3['Tanggal'])

#kurs = df3[['Tanggal', 'Kurs Jual']].set_index('Tanggal')
#plt.grid()
#plt.show()
#st.line_chart(kurs)

st.markdown('Untuk merespon kebijakan tersebut, Bank Sentral diberbagai negara mau tidak mau juga ikut meningkatkan suku bunganya untuk menahan keluarnya arus modal asing, tercatat Bank Indonesia (BI) menaikan suku bunga acuan menjadi 4,25% pada bulan September 2022. Namun harus menjadi perhatian bagi pemerintah bahwasannya kenaikan suku bunga berarti akan memperlambat laju pertumbuhan ekonomi dan menurunkan daya beli masyarakat.')

#st.subheader('Suku Bunga Acuan Bank Indonesia (BI)')
#df4 = pd.read_excel('/Users/vianbeladona/Desktop/tetris/suku_bunga_bi.xlsx')

#df4['Bulan'] = pd.to_datetime(df4['Bulan'])

#sukubungaBI = df4[['Bulan', 'Suku Bunga']].set_index('Bulan')
#st.line_chart(sukubungaBI)

#st.markdown('Selain itu tingkat inflasi AS yang tinggi dapat mengganggu kinerja ekspor tujuan AS. Jika konsumsi rumah tangga di AS menurun, maka hal ini dapat mempengaruhi demand dari komoditas ekspor Indonesia yang juga akan mengalami penurunan sehingga devisa negara juga akan mengalami penurunan.')
st.markdown('Dampak lainnya biaya bahan baku yang diambil dari AS atau dikirim dari AS akan mengalami kenaikan harga. Hal ini akan berimbas kepada inflasi global dikarenakan kenaikan harga ini akan meningkatkan biaya produksi sehingga produk yang dihasilkan akan mengalami kenaikan harga yang akan dibebankan kepada konsumen sehingga ada transmisi inflasi yang tinggi di AS terhadap harga produk di berbagai negara termasuk produk yang ada di Indonesia yang mengambil bahan baku dari AS.')

##st.subheader('Tingkat Inflasi di Beberapa Negara')
#df5 = pd.read_excel('/Users/vianbeladona/Desktop/tetris/suku_bunga_bi.xlsx')
#st.markdown('Peningkatan inflasi yang terjadi di AS mau tidak mau berimbas terhadap kondisi perekonomian di Indonesia. Tingginya inflasi AS memicu kenaikan suku bunga BI, kenaikan harga barang, serta pelemahan terhadap nilai tukar mata uang Rupiah, dimana beberapa variabel tersebut dapat membuat pertumbuhan ekonomi Indonesia mengalami perlambatan. Namun, pada kali ini Pemerintah Indonesia terselamatkan karena harga komoditas ekspor seperti kelapa sawit dan batu bara mengalami kenaikan sehingga kinerja perdagangan luar negeri masih tumbuh secara positif ditengah tekanan ekonomi global. Pertumbuhan ekonomi Indonesia pada kuartal II tahun 2022 cukup impresif berada di angka 5,4%.')

st.markdown('Selain itu tingkat inflasi AS yang tinggi dapat mengganggu kinerja ekspor tujuan AS. Jika konsumsi rumah tangga di AS menurun, maka hal ini dapat mempengaruhi demand dari komoditas ekspor Indonesia yang juga akan mengalami penurunan sehingga devisa negara juga akan mengalami penurunan.')
st.markdown('Namun, pada kali ini Pemerintah Indonesia terselamatkan karena harga komoditas ekspor seperti kelapa sawit dan batu bara mengalami kenaikan sehingga kinerja perdagangan luar negeri masih tumbuh secara positif ditengah tekanan ekonomi global. Pertumbuhan ekonomi Indonesia pada kuartal II tahun 2022 cukup impresif berada di angka 5,4%. ')
st.subheader('Pertumbuhan Ekonomi Indonesia')
#df6 = pd.read_excel('/Users/vianbeladona/Desktop/tetris/pertumbuhan_ekonomi.xlsx')

#df6['date'] = pd.to_datetime(df6['date'])

#pertumbuhan = df6[['date', 'Pertumbuhan Tahunan']].set_index('date')
#st.line_chart(pertumbuhan)
st.subheader('Lalu, apa yang harus dilakukan oleh Pemerintah RI')
st.markdown('Peningkatan inflasi yang terjadi di AS mau tidak mau berimbas terhadap kondisi perekonomian di Indonesia. Tingginya inflasi AS memicu kenaikan suku bunga BI, kenaikan harga barang, serta pelemahan terhadap nilai tukar mata uang Rupiah, dimana beberapa variabel tersebut dapat membuat pertumbuhan ekonomi Indonesia mengalami perlambatan. Pada kali ini Indonesia masih kuat menahan dampak inflasi AS karena sebetulnya inflasi di Indonesia sendiri lebih disebabkan oleh fenomena domestik, yaitu faktor volatile foods sebagai penyumbang utama dan juga dibantu dengan harga komoditas ekspor Indonesia yang meningkat.')
#st.markdown('Namun Pemerintah Indonesia tidak boleh lengah dengan kondisi ini, jika inflasi terus meningkat dan kondisi perekonomian global mengalami resesi, maka harus disiapkan kebijakan – kebijakan untuk merespon hal tersebut. Solusi yang dapat dilakukan untuk menahan laju inflasi dapat dilakukan dengan berbagai cara, yang pertama melalui kebijakan fiskal dengan mengurangi pengeluaran anggaran pemerintah. Kedua melalui kebijakan moneter dengan meningkatkan suku bunga sehingga dapat mengendalikan jumlah uang yang beredar. Ketiga kebijakan non-moneter dan non-fiskal seperti kebijakan yang meringankan para pengusaha sehingga dapat menambah hasil produksi, kemudian kebijakan penetapan harga maksimum, sehingga diharapkan daya beli masyarakat menjadi lebih baik.')
st.markdown('Namun Pemerintah Indonesia tidak boleh lengah dengan kondisi ini, jika inflasi terus meningkat dan kondisi perekonomian global mengalami resesi, pemerintah harus menyiapkan strategi – strategi untuk merespon hal tersebut. Solusi yang dapat dilakukan untuk menahan laju inflasi dapat dilakukan dengan berbagai cara, yang pertama melalui kebijakan fiskal dengan mengurangi pengeluaran anggaran pemerintah. Kedua melalui kebijakan moneter dengan mengendalikan jumlah uang yang beredar. Ketiga kebijakan non-moneter dan non-fiskal seperti kebijakan yang meringankan para pengusaha sehingga dapat menambah hasil produksi, kemudian kebijakan penetapan harga maksimum, sehingga diharapkan daya beli masyarakat menjadi lebih baik.')