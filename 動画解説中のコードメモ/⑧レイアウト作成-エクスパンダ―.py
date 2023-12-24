import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image #画像を表示させる、PILというライブラリを使用、Imageというのを書いてくださいだってさ

st.title('Streamlit 超入門')

st.write('Display Image') 

st.write('説明')





left_column, right_column = st.columns(2) 
button = left_column.button('右カラムに文字を表示') 
if button: 
    right_column.write('ここは右カラム')
    
    
#☆エクスパンダ―
#動画解説中ではbeta_expanderというようにbeta_がついているが2013時点ではbeta_は外す
expander1 = st.expander('問い合わせ1') #expander変数を用意して代入
expander1.write('問い合わせ1内容の回答') #.writeは書きこめるようにしている
expander2 = st.expander('問い合わせ2') 
expander2.write('問い合わせ2内容の回答')
expander3 = st.expander('問い合わせ3') 
expander3.write('問い合わせ3内容の回答')


    