#from turtle import color
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
#import colorama as init
#from colorama import init
#from termcolor import colored
import yfinance as yf
#from dash import Dash, dcc, html, Input, Output
#import fontstyle as tx
#import matplotlib.pyplot as plt
#import shape
#from sklearn import datasets
#from sklearn.ensemble import RandomForestRegressor
#from datetime import datetime
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive
#import requests
#from io import BytesIO
#import xlrd 

#st.title("Dampak Inflasi AS terhadap Perekonomian Indonesia")
st.set_page_config(layout='wide')
#st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)
#st.image(style="width:100%;height:400px"./inflasi.png")
#st.image("./inflasi.jpg", width = 1000)

st.markdown("<h1 style='text-align: center; color: black;'>Dampak Inflasi AS terhadap Perekonomian Indonesia</h1>", unsafe_allow_html=True)
st.write('---')
st.write("""
Made with **streamlit** by Novianto Sudardan
""")
st.markdown("Kondisi perekonomian dunia saat ini tengah mengalami guncangan hebat akibat dari kondisi yang kian tidak menentu, dimulai dari krisis kesehatan global akibat pandemi yang terjadi pada awal tahun 2020, kemudian dilanjutkan dengan pecahnya perang yang terjadi antara Rusia dan Ukrania yang menyebabkan supply disruption terhadap berbagai komoditas di beberapa negara, konflik yang berkepanjangan ini menyebabkan efek domino, tidak hanya memicu krisis energi tetapi juga krisis pangan, sehingga hal ini menyebabkan terjadinya inflasi global, beberapa negara kemudian menyikapinya dengan mengeluarkan kebijakan seperti pengetatan kebijakan moneter untuk mengurangi dampak negatif yang ditimbulkan akibat isu geopolitik yang terjadi saat ini.")

c1, c2 = st.columns([1,2])

with c1:
   st.markdown("Tidak terlepas dari kondisi krisis, Amerika Serikat (AS) sebagai negara superpower pun terkena imbas dari isu ini, Pada bulan Juni 2022, Biro Statistik Tenaga Kerja AS (Bureau of Labor Statistics) mencatat tingkat inflasi sempat menembus laju tertingginya sepanjang tahun 2022 pada nilai 9,1%, ini adalah level tertinggi dalam 40 tahun terakhir, bahkan jika keadaan terus memburuk tidak menutup kemungkinan akan menyebabkan resesi. Tercatat AS pernah mencatat tingkat inflasi tertinggi sepanjang sejarah sebesar 12,3% pada bulan Desember 1974. Adapun kebijakan yang diambil oleh pemerintah AS melalui Bank Sentral nya, The Federal Reserve (The Fed) pada saat itu adalah dengan menaikan suku bunga acuan. Data pada bulan September 2022 tercatat tingkat inflasi AS menurun menjadi 8,2%, namun ini masih tergolong tinggi, hal ini mendorong The Fed meningkatkan suku bunga acuan menjadi 3,25% pada bulan September 2022")
with c2:
   st.markdown("<body style='border-radius: 6px; box-shadow : 0 1px 4px rgba(0,0,0,.23);></body>", unsafe_allow_html=True)
   df = pd.read_excel('./DataInflasiAS.xlsx')
   fig = px.line(df, x='Periode', y='Nilai', markers=True, color='Rate')
   fig.update_layout(title = 'Suku Bunga Acuan The Fed & Tingkat Inflasi di AS', title_font_size = 20, paper_bgcolor = "#b7d1e2", xaxis_title='Periode', yaxis_title='Persentase (%)')
   fig.show()
   st.plotly_chart(fig, use_container_width=True)
   st.caption("<p style='text-align: center;'>Sumber : Trading Economics</p>", unsafe_allow_html=True)
#Made with **streamlit** by [tradingeconomics] (https://tradingeconomics.com/united-states/inflation-cpi)

#st.subheader('Tingkat Inflasi AS')
#df = pd.read_excel('./DataInflasiAS.xlsx')

#df['Periode'] = pd.to_datetime(df['Periode'])
#df = df.set_index('data')
#inflasi = df[['Periode', 'Data Inflasi']].set_index('Periode')
#st.line_chart(inflasi)

#df = px.data.gapminder().query("continent=='Oceania'")
#fig = px.line(df, x = df['Periode'], y = df['Data Inflasi'], title = 'Data Inflasi AS')
#st.write(""" **Suku Bunga Acuan The Fed & Tingkat Inflasi di AS** """)

#st.subheader('Suku Bunga Acuan The Fed')
#df2 = pd.read_excel('./suku_bunga_the_fed.xlsx')
#df2['Bulan'] = pd.to_datetime(df2['Bulan'])
#sukubunga = df2[['Bulan', 'Suku Bunga']].set_index('Bulan')
#st.line_chart(sukubunga)

c3, c4 = st.columns([2,1])
with c3:
   df2 = pd.read_excel('./DataInflasiIND.xlsx')
   fig2 = px.line(df2, x='Periode', y='Nilai', markers=True, color='Rate')
   fig2.update_layout(title = 'Suku Bunga Acuan BI & Tingkat Inflasi di Indonesia', title_font_size = 20, paper_bgcolor = "#e4e4e4", xaxis_title='Periode', yaxis_title='Persentase (%)')
   fig2.show()
   st.plotly_chart(fig2, use_container_width=True)
   st.caption("<p style='text-align: center;'>Sumber : Bank Indonesia</p>", unsafe_allow_html=True)

with c4:
   st.markdown('Untuk merespon kebijakan tersebut, Bank Sentral diberbagai negara mau tidak mau juga ikut meningkatkan suku bunganya untuk menahan keluarnya arus modal asing (capital outflow), tercatat Bank Indonesia (BI) menaikan suku bunga acuan menjadi 4,25% pada bulan September 2022.')
   st.markdown('Dampak lainnya adalah biaya bahan baku yang diambil dari AS atau dikirim dari AS akan mengalami kenaikan harga. Hal ini akan berimbas kepada inflasi global dikarenakan kenaikan harga ini akan meningkatkan biaya produksi sehingga produk yang dihasilkan akan mengalami kenaikan harga yang akan dibebankan kepada konsumen sehingga ada transmisi inflasi yang tinggi di AS terhadap harga produk di berbagai negara termasuk produk yang ada di Indonesia yang mengambil bahan baku dari AS.')
#st.subheader('Suku Bunga Acuan Bank Indonesia (BI)')
#df4 = pd.read_excel('./suku_bunga_bi.xlsx')
#df4['Bulan'] = pd.to_datetime(df4['Bulan'])
#sukubungaBI = df4[['Bulan', 'Suku Bunga']].set_index('Bulan')
#st.line_chart(sukubungaBI)

c5, c6 = st.columns([1,2])
with c5:
   st.markdown('Peningkatan suku bunga di AS akan membuat para investor menginvestasikan modalnya pada pasar AS karena tergiur dengan bunga yang tinggi, hal ini akan memicu aliran modal global meninggalkan negara-negara yang memiliki suku bunga dibawah nilai suku bunga yang ditetapkan oleh The Fed, termasuk Indonesia. Hal ini akan berimbas kepada nilai tukar mata uang dollar AS yang akan semakin perkasa terhadapa mata uang lainnya, tercatat kurs mata uang rupiah terhadap dollar pada akhir bulan September 2022 adalah sebesar 15.303,70 dan tidak menutup kemungkinan akan semakin melemah jika pemerintah tidak memiliki strategi yang tepat untuk mengatasinya. Harus menjadi perhatian bagi pemerintah bahwasannya menaikan suku bunga dapat memperlambat laju pertumbuhan ekonomi dan menurunkan daya beli masyarakat.')
with c6:   
   #df3 = pd.read_csv('./union_currency.csv')
   #fig3 = px.line(df3, x='Date', y='Close', markers=False, color='Currency')
   #fig3.update_layout(title = 'Mata Uang Dunia Terhadap Dollar AS', title_font_size = 20, paper_bgcolor = "#e4e4fe", xaxis_title='Tanggal', yaxis_title='Nilai')
   #fig3.show()
   #st.plotly_chart(fig3, use_container_width=True)
   #st.caption("<p style='text-align: center;'>sumber : Yahoo Finance</p>", unsafe_allow_html=True)

   #1.load dataset
   df3 = pd.read_csv('./open_rate.csv')
   #df4 = pd.read_csv('./union_currency.csv')

   #2.initialize figure
   #fig3 = go.Figure()
   fig3 = px.line(df3, x='Date', y='decrease_price', markers=False, color='Currency')
   fig3.update_layout(title = 'Nilai Valuasi Mata Uang Dunia Terhadap Dollar AS', xaxis_title='Periode', yaxis_title='Nilai', bgcolor = '#fff',bordercolor = '#fff',)
   fig3.show()
   st.plotly_chart(fig3, use_container_width=True),

   #fig4 = px.line(df4, x='Date', y='Close', markers=False, color='Currency')

   #3.add traces
   #fig3.add_trace(
   #   go.Scatter(x=list(df3.Date), 
   #           y=list(df3.decrease_price),
   #           name="Valuasi",
   #           #line=dict(color="#33CFA5")
   #           ))
   #fig.add_trace(
   #   go.Scatter(x=list(df3.Date), 
   #           y=list(df3.close_price),
   #           name="Kurs",
   #           #line=dict(color="#F06A6A")
   #           ))

   #Nilai = st.radio("",('Valuasi', 'Kurs'), key=None, help=None)
   #if Nilai == "Valuasi":
   #   fig3.update_layout(title = 'Nilai Mata Uang Dunia Terhadap Dollar AS', title_font_size = 20, paper_bgcolor = "#c7d7e8", xaxis_title='Periode', yaxis_title='Nilai'),
   #   fig3.show(),
   #   #st.plotly_chart(fig3, use_container_width=True),
   #elif Nilai == "Kurs":
   #   fig4.update_layout(title = 'Nilai Mata Uang Dunia Terhadap Dollar AS', title_font_size = 20, paper_bgcolor = "#c7d7e8", xaxis_title='Periode', yaxis_title='Nilai'),
   #   fig4.show(),
   #   #st.plotly_chart(fig4, use_container_width=True),

   #update plot sizing
   #fig3.update_layout(
    #width=800,
    #height=900,
    #color = "white",
    #autosize=False,
    #margin=dict(t=5, b=5, l=1, r=1),
    #template="plotly_white",)

   #fig3.update_layout(title = 'Nilai Valuasi Mata Uang Dunia Terhadap Dollar AS', xaxis_title='Periode', yaxis_title='Nilai')
   
   #4.add line
   #fig3 = px.line(df3, x='Date', y='decrease_price', markers=False, color='Currency')
   #fig3.update_layout(title = 'Nilai Valuasi Mata Uang Dunia Terhadap Dollar AS', xaxis_title='Periode', yaxis_title='Nilai')
   #fig3.show()

   #5.add dropdown
   #fig3.update_layout(
   #   updatemenus=[
   #         dict(
   #            active = 0,
   #            bgcolor = '#fff',
   #            bordercolor = '#fff',
   #            buttons=list([
   #               dict(label="Valuasi",
   #                    method="update",
   #                    args=[{"type": "Valuasi"},
   #                    {"title": "Nilai Valuasi Mata Uang Dunia Terhadap Dollar AS",
   #                     }]), 
   #               dict(label="Kurs",
   #                    method="update",
   #                    args=[{"type": "Kurs"},
   #                    {"title": "Nilai Kurs Mata Uang Dunia Terhadap Dollar AS",
   #                     }]), 
   #            ]),
   #           direction="down",
   #            pad={"r": 10, "t": 10},
   #            #color="white",
   #            showactive=True,
   #            #x=0.1,
   #            xanchor="left",
   #            #y=1.1,
   #            yanchor="top"
   #           ),
   #   ]
   #)
   #fig3.update_layout(title = 'Nilai Mata Uang Dunia Terhadap Dollar AS', title_font_size = 20, paper_bgcolor = "#c7d7e8", xaxis_title='Periode', yaxis_title='Nilai')
   #fig3.show()
   #st.plotly_chart(fig3, use_container_width=True)
   #st.plotly_chart(fig3)

   #tickerSymbol = st.radio("Pick Stock",["GOOGL", "AAPL"])
   #tickerSymbol_text = st.text_input("Enter Ticker")
   #ickerData = yf.Ticker(tickerSymbol_text)
   #select_period = st.select_slider("Select Period", ["1d", "5d","1mo"])
   #tickerDF = tickerData.history(period = select_period)
   st.caption("<p style='text-align: center;'>Sumber : Yahoo Finance</p>", unsafe_allow_html=True)

   #df3 = pd.read_excel('./Kurs_Rupiah.xlsx')
   #fig3 = px.line(df3, x='Tanggal', y='Kurs Jual', markers=True)
   #fig3.update_layout(title = 'Kurs Dollar AS Terhadap Mata Uang Dunia', xaxis_title='Tanggal', yaxis_title='Nilai Kurs')
   #fig3.show()
   #st.plotly_chart(fig3, use_container_width=True)
   #st.caption("<p style='text-align: center;'>Sumber : Bank Indonesia</p>", unsafe_allow_html=True)


#st.subheader('Nilai Tukar Mata Uang Rupiah')
#df4 = pd.read_excel('./Kurs_Rupiah.xlsx')
#df3['Tanggal'] = pd.to_datetime(df3['Tanggal'])
#kurs = df3[['Tanggal', 'Kurs Jual']].set_index('Tanggal')
#st.line_chart(kurs)


#st.subheader('Tingkat Inflasi di Beberapa Negara')
#df5 = pd.read_excel('/Users/vianbeladona/Desktop/tetris/suku_bunga_bi.xlsx')
#st.markdown('Peningkatan inflasi yang terjadi di AS mau tidak mau berimbas terhadap kondisi perekonomian di Indonesia. Tingginya inflasi AS memicu kenaikan suku bunga BI, kenaikan harga barang, serta pelemahan terhadap nilai tukar mata uang Rupiah, dimana beberapa variabel tersebut dapat membuat pertumbuhan ekonomi Indonesia mengalami perlambatan. Namun, pada kali ini Pemerintah Indonesia terselamatkan karena harga komoditas ekspor seperti kelapa sawit dan batu bara mengalami kenaikan sehingga kinerja perdagangan luar negeri masih tumbuh secara positif ditengah tekanan ekonomi global. Pertumbuhan ekonomi Indonesia pada kuartal II tahun 2022 cukup impresif berada di angka 5,4%.')

st.markdown('Tingkat inflasi AS yang tinggi juga dapat mengganggu kinerja ekspor Indonesia. Jika konsumsi rumah tangga di AS menurun, maka hal ini dapat mempengaruhi demand dari komoditas ekspor Indonesia yang juga akan mengalami penurunan sehingga devisa negara juga akan mengalami penurunan.')
st.markdown('Namun, pada kali ini Pemerintah Indonesia terselamatkan karena harga komoditas ekspor seperti kelapa sawit dan batu bara mengalami kenaikan sehingga kinerja perdagangan luar negeri masih tumbuh secara positif ditengah tekanan ekonomi global. Pertumbuhan ekonomi Indonesia pada kuartal II tahun 2022 cukup impresif berada di angka 5,4%, dan pertumbuhan Indonesia pada kuartal III tahun 2022 diproyeksikan akan meningkat sebesar 0,1% yaitu berada di angka 5,5%.')

st.subheader('Pertumbuhan Ekonomi Indonesia')
df6 = pd.read_excel('./pertumbuhan_ekonomi.xlsx')
df6['date'] = pd.to_datetime(df6['date'])
pertumbuhan = df6[['date', 'Pertumbuhan Tahunan']].set_index('date')
st.line_chart(pertumbuhan)

st.subheader('Lalu, apa yang harus dilakukan oleh Pemerintah RI')
st.markdown('Peningkatan inflasi yang terjadi di AS mau tidak mau berimbas terhadap kondisi perekonomian di Indonesia. Tingginya inflasi AS memicu kenaikan suku bunga BI, kenaikan harga barang, serta pelemahan terhadap nilai tukar mata uang Rupiah, dimana beberapa variabel tersebut dapat membuat pertumbuhan ekonomi Indonesia mengalami perlambatan. Pada kali ini Indonesia masih kuat menahan dampak inflasi AS karena sebetulnya inflasi di Indonesia sendiri lebih disebabkan oleh fenomena domestik, yaitu faktor volatile foods sebagai penyumbang utama dan juga dibantu dengan harga komoditas ekspor Indonesia yang meningkat.')
st.markdown('Namun Pemerintah Indonesia tidak boleh lengah dengan kondisi ini, jika inflasi terus meningkat dan kondisi perekonomian global mengalami resesi, pemerintah harus menyiapkan strategi – strategi untuk merespon hal tersebut. Solusi yang dapat dilakukan untuk menahan laju inflasi dapat dilakukan dengan berbagai cara, yang pertama melalui kebijakan fiskal dengan mengurangi pengeluaran anggaran pemerintah. Kedua melalui kebijakan moneter dengan mengendalikan jumlah uang yang beredar. Ketiga kebijakan non-moneter dan non-fiskal seperti kebijakan yang meringankan para pengusaha sehingga dapat menambah hasil produksi, kemudian kebijakan penetapan harga maksimum, sehingga diharapkan daya beli masyarakat menjadi lebih baik.')