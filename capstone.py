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
st.markdown('Kondisi perekonomian dunia saat ini tengah mengalami guncangan hebat akibat dari kondisi yang kian tidak menentu, dimulai dari krisis kesehatan global akibat pandemi COVID-19 yang terjadi pada awal tahun 2020, dilanjutkan dengan isu geopolitik antara Rusia dan Ukrania yang menyebabkan _supply disruption_ terhadap berbagai komoditas. Tidak terlepas dari kondisi krisis, Amerika Serikat (AS) sebagai negara _superpower_ pun terkena imbas dari isu ini, Pada bulan Juni 2022, Biro Statistik Tenaga Kerja AS _(Bureau of Labor Statistics)_ mencatat tingkat inflasi sempat menembus laju tertingginya sepanjang tahun 2022 pada nilai 9,1%, ini adalah level tertinggi dalam 40 tahun terakhir. Untuk merespon kebijakan tersebut, Bank Sentral beberapa negara mau tidak mau juga ikut meningkatkan suku bunganya untuk menahan keluarnya arus modal asing _(capital outflow)_, tercatat Bank Indonesia (BI) menaikan suku bunga acuan menjadi 4,25% pada bulan September 2022. Selain itu Mata uang Dollar AS merupakan mata uang yang paling banyak digunakan pada perdagangan internasional. Oleh karena itu, perubahan terhadap nilai mata uang tersebut akan berdampak bagi keseluruhan ekonomi global.')

c1, c2 = st.columns([1,1])
with c1:
   #st.markdown("Tidak terlepas dari kondisi krisis, Amerika Serikat (AS) sebagai negara superpower pun terkena imbas dari isu ini, Pada bulan Juni 2022, Biro Statistik Tenaga Kerja AS (Bureau of Labor Statistics) mencatat tingkat inflasi sempat menembus laju tertingginya sepanjang tahun 2022 pada nilai 9,1%, ini adalah level tertinggi dalam 40 tahun terakhir, bahkan jika keadaan terus memburuk tidak menutup kemungkinan akan menyebabkan resesi. Tercatat AS pernah mencatat tingkat inflasi tertinggi sepanjang sejarah sebesar 12,3% pada bulan Desember 1974. Adapun kebijakan yang diambil oleh pemerintah AS melalui Bank Sentral nya, The Federal Reserve (The Fed) pada saat itu adalah dengan menaikan suku bunga acuan. Data pada bulan September 2022 tercatat tingkat inflasi AS menurun menjadi 8,2%, namun ini masih tergolong tinggi, hal ini mendorong The Fed meningkatkan suku bunga acuan menjadi 3,25% pada bulan September 2022")
   df = pd.read_excel('./DataInflasiAS.xlsx')
   fig = px.line(df, x='Periode', y='Nilai', markers=True, color='Rate')
   fig.update_layout(title = 'Suku Bunga Acuan The Fed & Tingkat Inflasi di AS', title_font_size = 20, paper_bgcolor = "#b7d1e2", xaxis_title='Periode', yaxis_title='Persentase (%)')
   fig.show()
   st.plotly_chart(fig, use_container_width=True)
   st.caption("<p style='text-align: center;'>Sumber : Trading Economics</p>", unsafe_allow_html=True)
with c2:
   df2 = pd.read_excel('./DataInflasiIND.xlsx')
   fig2 = px.line(df2, x='Periode', y='Nilai', markers=True, color='Rate')
   fig2.update_layout(title = 'Suku Bunga Acuan BI & Tingkat Inflasi di Indonesia', title_font_size = 20, paper_bgcolor = "#e4e4e4", xaxis_title='Periode', yaxis_title='Persentase (%)')
   fig2.show()
   st.plotly_chart(fig2, use_container_width=True)
   st.caption("<p style='text-align: center;'>Sumber : Bank Indonesia</p>", unsafe_allow_html=True)

c3, c4 = st.columns([1,2])
with c3:
   #st.markdown('Dampak lainnya adalah biaya bahan baku yang diambil dari AS atau dikirim dari AS akan mengalami kenaikan harga. Hal ini akan berimbas kepada inflasi global dikarenakan kenaikan harga ini akan meningkatkan biaya produksi sehingga produk yang dihasilkan akan mengalami kenaikan harga yang akan dibebankan kepada konsumen sehingga ada transmisi inflasi yang tinggi di AS terhadap harga produk di berbagai negara yang mengambil bahan baku dari AS. Peningkatan suku bunga di AS akan membuat para investor menginvestasikan modalnya pada pasar AS karena tergiur dengan bunga yang tinggi, hal ini akan berimbas pada nilai tukar mata uang dollar AS yang akan semakin perkasa terhadap mata uang lainnya.')
   #with open('style.css') as f:
   #   st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
   st.markdown("<p style='color: black; padding: 10px 10px 10px 20px; border-radius: 0px; border: 1px solid #CCCCCC;'> Peningkatan suku bunga di AS akan membuat para investor menginvestasikan modalnya pada pasar AS karena tergiur dengan nilai suku bunga yang tinggi, hal ini berimbas pada nilai kurs dollar AS yang kian menguat. Terlihat pergerakan nilai mata uang dunia yang cenderung menurun dalam setahun terakhir.</p>", unsafe_allow_html=True)

with c4:
     #load dataset
   df4 = pd.read_csv('./sgd_rate.csv')
   df5 = pd.read_csv('./gbp_rate.csv')
   df6 = pd.read_csv('./eur_rate.csv')
   df7 = pd.read_csv('./aud_rate.csv')
   df8 = pd.read_csv('./chf_rate.csv')
   df9 = pd.read_csv('./kwd_rate.csv')
   #df10 = pd.read_csv('./open_rate.csv')
   
   #initialize figure
   fig3 = go.Figure()

   #update plot sizing
   fig3.update_layout(autosize=True)

   #add traces
   #Figure Valuasi
   fig3.add_trace(
      go.Scatter(x=list(df4.Date), 
                 y=list(df4.decrease_price),
                 name="Singapura",
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
                 line=dict(color="#747375")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df9.Tanggal), 
                 y=list(df9.decrease_price),
                 name="Kuwait",
                 line=dict(color="#0a704b")
              ))
   fig3.add_trace(
      go.Scatter(x=list(df8.Date), 
                 y=list(df8.decrease_price),
                 name="Swiss",
                 line=dict(color="#590d0d")
              ))

   #Figure Kurs
   fig3.add_trace(
      go.Scatter(x=list(df4.Date), 
                 y=list(df4.close_price),
                 name="Singapura",
                 line=dict(color="#F06A6A"),
                 visible = False
              ))
   fig3.add_trace(
      go.Scatter(x=list(df5.Date), 
                 y=list(df5.close_price),
                 name="Inggris",
                 line=dict(color="#6155e6"),
                 visible = False
              ))
   fig3.add_trace(
      go.Scatter(x=list(df6.Date), 
                 y=list(df6.close_price),
                 name="Euro",
                 line=dict(color="#d602ed"),
                 visible = False
              ))
   fig3.add_trace(
      go.Scatter(x=list(df7.Date), 
                 y=list(df7.close_price),
                 name="Australia",
                 line=dict(color="#747375"),
                 visible = False
              ))
   fig3.add_trace(
      go.Scatter(x=list(df9.Tanggal), 
                 y=list(df9.close_price),
                 name="Kuwait",
                 line=dict(color="#0a704b"),
                 visible = False
              ))
   fig3.add_trace(
      go.Scatter(x=list(df8.Date), 
                 y=list(df8.close_price),
                 name="Swiss",
                 line=dict(color="#590d0d"),
                 visible = False
              ))

   #define annotation
   dec_price = [dict(x=df8.Date,
                     y=df8.decrease_price,
                     #xref="x", yref="y"
                     )]
   cl_price = [dict(x=df8.Date,
                    y=df8.close_price,
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
               visible = True,
               buttons=list([
                  dict(label="Valuasi",
                       method="update",
                       args=[{"visible": [True, True, True, True, True, False, False, False, False, False]},
                       {"title": "Nilai Valuasi Mata Uang Dunia Terhadap Dollar AS",
                        "annotations": dec_price}]), 
                  dict(label="Kurs",
                       method="update",
                       args=[{"visible": [False, False, False, False, False, True, True, True, True, True]},
                       {"title": "Nilai Kurs Mata Uang Dunia Terhadap Dollar AS",
                        "annotations": cl_price}]), 
               ]),
               direction="down",
               pad={"r": 10, "t": 10},
               showactive=True,
               x=-0.05,
               #xanchor="left",
               y=1
               #yanchor="top"
              ),
      ]
   )
   
   fig3.update_layout(title = 'Nilai Valuasi Mata Uang Dunia Terhadap Dollar AS', title_font_size = 20, paper_bgcolor = "#e4e4fe", xaxis_title='Periode', yaxis_title='Nilai')
   fig3.show()
   st.plotly_chart(fig3, use_container_width=True)
   st.caption("<p style='text-align: center;'>Sumber : Yahoo Finance</p>", unsafe_allow_html=True)


c5, c6 = st.columns([2,1])
with c5:
   df3 = pd.read_csv('./ind_rate.csv')

   #initialize figure
   fig4 = go.Figure()

   #update plot sizing
   fig4.update_layout(autosize=True)

   #add traces
   #Figure Valuasi
   fig4.add_trace(
      go.Scatter(x=list(df3.Date), 
                 y=list(df3.decrease_price),
                 name="Indonesia",
                 line=dict(color="#33CFA5")
              ))
   #Figure Kurs
   fig4.add_trace(
      go.Scatter(x=list(df3.Date), 
                 y=list(df3.close_price),
                 name="Indonesia",
                 line=dict(color="#e30202"),
                 visible = False
              ))
   #define annotation
   dec_price2 = [dict(x=df3.Date,
                     y=df3.decrease_price,
                     #xref="x", yref="y"
                     )]
   cl_price2 = [dict(x=df3.Date,
                    y=df3.close_price,
                    #xref="x", yref="y"
                    )]
#add dropdown
   fig4.update_layout(
      updatemenus=[
            dict(
               active = 0,
               bgcolor = '#fff',
               bordercolor = '#fff',
               #margin=dict(t=5, b=5, l=1, r=1),
               visible = True,
               buttons=list([
                  dict(label="Valuasi",
                       method="update",
                       args=[{"visible": [True, False]},
                       {"title": "Nilai Valuasi Mata Uang Rupiah Terhadap Dollar AS",
                        "annotations": dec_price2
                        }]), 
                  dict(label="Kurs",
                       method="update",
                       args=[{"visible": [False, True]},
                       {"title": "Nilai Kurs Mata Uang Rupiah Terhadap Dollar AS",
                        "annotations": cl_price2
                        }]), 
               ]),
               direction="down",
               pad={"r": 10, "t": 10},
               showactive=True,
               x=-0.05,
               #xanchor="left",
               y=1
               #yanchor="top"
              ),
      ]
   )

   fig4.update_layout(title = 'Nilai Valuasi Mata Uang Rupiah Terhadap Dollar AS', title_font_size = 20, paper_bgcolor = "#e4e4e4", xaxis_title='Periode', yaxis_title='Nilai')
   fig4.show()
   st.plotly_chart(fig4, use_container_width=True)
   st.caption("<p style='text-align: center;'>Sumber : Yahoo Finance</p>", unsafe_allow_html=True)


with c6: 
   st.markdown("<p style='color: black; padding: 10px 10px 10px 20px;  border-radius: 0px; border: 1px solid #CCCCCC;'>Nilai mata uang Rupiah juga terkena dampaknya, sampai dengan saat ini valuasinya sudah melemah lebih dari seribu Rupiah semenjak tahun lalu. Tidak menutup kemungkinan nilai mata uang Rupiah akan semakin melemah jika pemerintah tidak memiliki strategi yang tepat untuk mengatasinya.</p>", unsafe_allow_html=True)
st.markdown('Inflasi yang terjadi di AS juga dapat mengganggu kinerja ekspor Indonesia. Jika konsumsi rumah tangga di AS menurun, maka hal ini dapat mempengaruhi _demand_ dari komoditas ekspor yang akan mengalami penurunan sehingga devisa negara juga akan mengalami penurunan. Namun, pada kali ini Pemerintah Indonesia terselamatkan karena harga komoditas ekspor seperti kelapa sawit dan batu bara mengalami kenaikan sehingga kinerja perdagangan luar negeri masih tumbuh secara positif ditengah tekanan ekonomi global. Pertumbuhan ekonomi Indonesia pada kuartal II tahun 2022 cukup impresif berada di angka 5,4%. Tingkat inflasi di AS yang tinggi pada kali ini tidak berimbas signifikan terhadap perekonomian Indonesia, terlihat dari grafik PDB yang mengalami kenaikan. Namun jika kondisi ini terus berlangsung, peningkatan inflasi yang terjadi di AS mau tidak mau berimbas terhadap kondisi perekonomian di Indonesia. Tingginya inflasi di AS akan memicu kenaikan suku bunga BI, kenaikan harga barang, serta pelemahan terhadap nilai tukar mata uang Rupiah, dimana beberapa variabel tersebut dapat membuat pertumbuhan ekonomi Indonesia mengalami perlambatan.')
#st.markdown('Untuk menghitung pertumbuhan ekonomi dapat dilakukan dengan menggunakan perhitungan Pendapatan Domestik Bruto (PDB) atas dasar harga konstan. Rumus umum untuk PDB dengan pendekatan pengeluaran adalah penjumlahan dari semua konsumsi, investasi, pengeluaran pemerintah, dan perdagangan luar negeri.')

c7, c8 = st.columns([1,1])
with c7:
   df11 = pd.read_excel('./pdb_ekspor.xlsx')
   df12 = pd.read_excel('./pdb_impor.xlsx')
   fig5 = go.Figure()
   fig5.add_trace(go.Bar(x=list(df11.Periode),
             y=list(df11.Nilai),
             name="Ekspor",
             marker_color='rgb(55, 83, 109)'
            ))
   fig5.add_trace(go.Bar(x=(df12.Periode),
             y=(df12.Nilai),
             name="Impor",
             marker_color='rgb(26, 118, 255)'
            ))
   fig5.update_layout(title ="Nilai Ekspor Impor Indonesia", title_font_size = 20, paper_bgcolor = "#f2cb9b", xaxis=dict(title='Periode'), yaxis=dict(title='Milyar Rupiah'), barmode='group', bargap=0.15, bargroupgap=0.1)
   fig5.show()
   st.plotly_chart(fig5, use_container_width=True)
   st.caption("<p style='text-align: center;'>Sumber : Badan Pusat Statistik</p>", unsafe_allow_html=True)

with c8: 
   #df13 = pd.read_excel('./pdb_union.xlsx')
   #fig5 = px.bar(df13, x="Periode", y="Nilai", color="Jenis")
   #fig5.update_layout(title = "PDB Indonesia (Pengeluaran)", title_font_size = 20, paper_bgcolor = "#f2cb9b", xaxis_title='Periode', yaxis_title='Milyar Rupiah')
   #fig5.show()
   #st.plotly_chart(fig5, use_container_width=True)
   #st.caption("<p style='text-align: center;'>Sumber : BPS</p>", unsafe_allow_html=True)
   df13 = pd.read_excel('./pdb_source.xlsx')
   fig5 = go.Figure()
   fig5.add_trace(go.Bar(x=(df13.Periode),
            y=(df13.Inventory),
            name="Inventory",
            marker_color='rgb(227, 209, 9)'
            ))
   fig5.add_trace(go.Bar(x=list(df13.Periode),
            y=list(df13.Eksim),
            name="Ekspor - Impor",
            marker_color='rgb(67, 227, 9)'
            ))
   fig5.add_trace(go.Bar(x=(df13.Periode),
            y=(df13.LNPRT),
            name="LNPRT",
            marker_color='rgb(240, 5, 5)'
            ))
   fig5.add_trace(go.Bar(x=(df13.Periode),
            y=(df13.PMTB),
            name="PMTB",
            marker_color='rgb(227, 125, 9)'
            ))
   fig5.add_trace(go.Bar(x=(df13.Periode),
            y=(df13.KRT),
            name="KRT",
            marker_color='rgb(26, 118, 255)'
            ))
   fig5.add_trace(go.Bar(x=(df13.Periode),
            y=(df13.Pemerintah),
            name="Pemerintah",
            marker_color='rgb(9, 230, 230)'
            ))
   fig5.add_trace(go.Scatter(x=list(df13.Periode), 
            y=list(df13.pdb),
            name="PDB",
            line=dict(color="#37536d")
            ))
   fig5.update_layout(title = 'PDB Indonesia (Pengeluaran)', title_font_size = 20, paper_bgcolor = "#e4e4fe", xaxis_title='Periode', yaxis_title='Milyar Rupiah', barmode='stack')
   fig5.show()
   st.plotly_chart(fig5, use_container_width=True)
   st.caption("<p style='text-align: center;'>Sumber : Badan Pusat Statistik</p>", unsafe_allow_html=True)

   
st.subheader('Lalu, apa yang harus dilakukan oleh Pemerintah RI')
#st.markdown('Peningkatan inflasi yang terjadi di AS mau tidak mau berimbas terhadap kondisi perekonomian di Indonesia. Tingginya inflasi AS memicu kenaikan suku bunga BI, kenaikan harga barang, serta pelemahan terhadap nilai tukar mata uang Rupiah, dimana beberapa variabel tersebut dapat membuat pertumbuhan ekonomi Indonesia mengalami perlambatan. Pada kali ini Indonesia masih kuat menahan dampak inflasi AS karena sebetulnya inflasi di Indonesia sendiri lebih disebabkan oleh fenomena domestik, yaitu faktor volatile foods sebagai penyumbang utama dan juga dibantu dengan harga komoditas ekspor Indonesia yang meningkat.')
#st.markdown('Namun Pemerintah Indonesia tidak boleh lengah dengan kondisi ini, jika inflasi terus meningkat dan kondisi perekonomian global mengalami resesi, pemerintah harus menyiapkan strategi – strategi untuk merespon hal tersebut. Solusi yang dapat dilakukan untuk menahan laju inflasi dapat dilakukan dengan berbagai cara, yang pertama melalui kebijakan fiskal dengan mengurangi pengeluaran anggaran pemerintah. Kedua melalui kebijakan moneter dengan mengendalikan jumlah uang yang beredar. Ketiga kebijakan non-moneter dan non-fiskal seperti kebijakan yang meringankan para pengusaha sehingga dapat menambah hasil produksi, kemudian kebijakan penetapan harga maksimum, sehingga diharapkan daya beli masyarakat menjadi lebih baik.')
st.markdown('Tingkat inflasi yang tinggi akan memicu penekanan jika tidak di imbangi dengan faktor ekonomi yg meningkat seperti kegiatan ekspor-impor, peningkatan devisa, peningkatan investasi, serta stabilitas ekonomi dalam negeri. Pemerintah Indonesia tidak boleh lengah dengan kondisi ini, harus waspada terhadap berakhirnya _windfall_ komoditas ditambah lagi jika inflasi terus meningkat dan kondisi perekonomian global mengalami resesi, pemerintah harus menyiapkan strategi – strategi untuk merespon hal tersebut. Solusi yang dapat dilakukan untuk menahan laju inflasi dapat dilakukan dengan berbagai cara, yang pertama melalui kebijakan fiskal yang dapat dilakukan dengan mengurangi pengeluaran anggaran pemerintah. Kedua melalui kebijakan moneter, yaitu pengendalian terhadap jumlah uang yang beredar. Ketiga kebijakan non-moneter dan non-fiskal seperti kebijakan yang meringankan para pengusaha agar dapat lebih produktif sehingga dapat menambah hasil produksi dan menyerap tenaga kerja lokal, kemudian kebijakan penetapan harga maksimum, sehingga diharapkan daya beli masyarakat menjadi lebih baik.')