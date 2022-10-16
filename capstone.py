import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf

st.set_page_config(layout='wide')
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

c5, c6 = st.columns([1,2])
with c5:
   st.markdown('Peningkatan suku bunga di AS akan membuat para investor menginvestasikan modalnya pada pasar AS karena tergiur dengan bunga yang tinggi, hal ini akan memicu aliran modal global meninggalkan negara-negara yang memiliki suku bunga dibawah nilai suku bunga yang ditetapkan oleh The Fed, termasuk Indonesia. Hal ini akan berimbas kepada nilai tukar mata uang dollar AS yang akan semakin perkasa terhadapa mata uang lainnya, tercatat kurs mata uang rupiah terhadap dollar pada akhir bulan September 2022 adalah sebesar 15.303,70 dan tidak menutup kemungkinan akan semakin melemah jika pemerintah tidak memiliki strategi yang tepat untuk mengatasinya. Harus menjadi perhatian bagi pemerintah bahwasannya menaikan suku bunga dapat memperlambat laju pertumbuhan ekonomi dan menurunkan daya beli masyarakat.')
with c6: 
   #load dataset
   df3 = pd.read_csv('./ind_rate.csv')
   df4 = pd.read_csv('./jpy_rate.csv')
   df5 = pd.read_csv('./gbp_rate.csv')
   df6 = pd.read_csv('./eur_rate.csv')
   df7 = pd.read_csv('./aud_rate.csv')
   df8 = pd.read_csv('./cny_rate.csv')
   df9 = pd.read_csv('./chf_rate.csv')
   #fig3 = px.line(df3, x='Date', y='close_price', markers=False)
   #fig3.update_layout(title = 'Kurs Mata Uang Dunia Terhadap Dollar AS', title_font_size = 20, paper_bgcolor = "#e4e4fe", xaxis_title='Tanggal', yaxis_title='Nilai')
   #fig3.show()
   #st.plotly_chart(fig3, use_container_width=True)
   
   #initialize figure
   fig4 = px.line(df3, x='Date', y='close_price', markers=False, color='Negara')
   fig4.update_layout(title = 'Kurs Mata Uang Dunia Terhadap Dollar AS', title_font_size = 20, paper_bgcolor = "#e4e4fe", xaxis_title='Tanggal', yaxis_title='Nilai')
   fig4.show()
   st.plotly_chart(fig4, use_container_width=True)
   fig3 = go.Figure()

   #update plot sizing
   fig3.update_layout(
      autosize=True)
    #width=800,
    #height=900,
    #color = "white",
    #margin=dict(t=15, b=10, l=10, r=15))
    #template="plotly_white",)

   #add traces
   #Figure Valuasi
   fig3.add_trace(
      go.Scatter(x=list(df3.Date), 
                 y=list(df3.decrease_price),
                 name="Indonesia",
                 line=dict(color="#33CFA5")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df4.Date), 
                 y=list(df4.decrease_price),
                 name="Jepang",
                 line=dict(color="#F06A6A")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df5.Date), 
                 y=list(df5.decrease_price),
                 name="Inggris",
                 line=dict(color="#6155e6")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df6.Date), 
                 y=list(df6.decrease_price),
                 name="Euro",
                 line=dict(color="#d602ed")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df7.Date), 
                 y=list(df7.decrease_price),
                 name="Australia",
                 line=dict(color="#02ede5")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df8.Date), 
                 y=list(df8.decrease_price),
                 name="China",
                 line=dict(color="#590d0d")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df9.Date), 
                 y=list(df9.decrease_price),
                 name="Swiss",
                 line=dict(color="#f5f507")
              ))

   #Figure Kurs
   fig3.add_trace(
      go.Scatter(x=list(df3.Date), 
                 y=list(df3.close_price),
                 name="Indonesia",
                 line=dict(color="#33CFA5")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df4.Date), 
                 y=list(df4.close_price),
                 name="Jepang",
                 line=dict(color="#F06A6A")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df5.Date), 
                 y=list(df5.close_price),
                 name="Inggris",
                 line=dict(color="#6155e6")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df6.Date), 
                 y=list(df6.close_price),
                 name="Euro",
                 line=dict(color="#d602ed")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df7.Date), 
                 y=list(df7.close_price),
                 name="Australia",
                 line=dict(color="#02ede5")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df8.Date), 
                 y=list(df8.close_price),
                 name="China",
                 line=dict(color="#590d0d")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df9.Date), 
                 y=list(df9.close_price),
                 name="Swiss",
                 line=dict(color="#f5f507")
              ))


   #define annotation
   dec_price = [dict(x=df4.Date,
                     y=df4.decrease_price,
                     #xref="x", yref="y"
                     )]
   cl_price = [dict(x=df4.Date,
                    y=df4.close_price,
                    #xref="x", yref="y"
                    )]
   #add dropdown
   fig3.update_layout(
      updatemenus=[
            dict(
               active = 0,
               bgcolor = '#fff',
               bordercolor = '#fff',
               #margin=dict(t=5, b=5, l=1, r=1),
               buttons=list([
                  dict(label="Valuasi",
                       method="update",
                       args=[{"visible": [True, True, True, True, True, True, True, False, False, False, False, False, False, False]},
                       {"title": "Nilai Valuasi Mata Uang Dunia Terhadap Dollar AS",
                        "annotations": dec_price}]), 
                  dict(label="Kurs",
                       method="update",
                       args=[{"visible": [False, False, False, False, False, False, False, True, True, True, True, True, True, True]},
                       {"title": "Nilai Kurs Mata Uang Dunia Terhadap Dollar AS",
                        "annotations": cl_price}]), 
               ]),
               direction="down",
               pad={"r": 10, "t": 10},
               showactive=True,
               #x=0,
               xanchor="left",
               #y=10,
               yanchor="bottom"
              ),
      ]
   )

   #fig3 = px.line(df3, x='Date', y='close_price', markers=False, color='Negara')
   fig3.update_layout(title = 'Kurs Mata Uang Dunia Terhadap Dollar AS', title_font_size = 20, paper_bgcolor = "#e4e4fe", xaxis_title='Tanggal', yaxis_title='Nilai')
   fig3.show()
   st.plotly_chart(fig3, use_container_width=True)
   st.caption("<p style='text-align: center;'>Sumber : Yahoo Finance</p>", unsafe_allow_html=True)

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