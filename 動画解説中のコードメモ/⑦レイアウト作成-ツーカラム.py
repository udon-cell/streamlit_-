import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image #画像を表示させる、PILというライブラリを使用、Imageというのを書いてくださいだってさ

st.title('Streamlit 超入門')

st.write('Display Image') 

st.write('説明')




#レイアウト作成-ツーカラム
#☆ツーカラム(2つの列の、というか2カラムの状態)にする
#beta_columnsを使用して、2カラムにしたいときは()内を2を入れて(2)
#3カラムにしたいときは(3)とする
#今回は２カラムにしたい
#2023/12/13現在、st.beta_columnsはst.columnsに変更されているので注意！
left_column, right_column = st.columns(2) 
#左側にボタンを追加して、右側にテキストを表示したい時
#left_column.button #.buttonをつける。seidebar.をつけたのと同じような感じ
# left_column.button('右カラムに文字を表示') #右カラムに文字を表示という文字を表示したいので。
#右カラムに表示するものを用意していく
button = left_column.button('右カラムに文字を表示') #buttonという変数に入れておくとして
if button: #buttonがTrueなら(押下されたら)
    right_column.write('ここは右カラム')#右カラムに文字を書きますよ
    
    



