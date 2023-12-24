import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image #画像を表示させる、PILというライブラリを使用、Imageというのを書いてくださいだってさ

st.title('Streamlit 超入門')

st.write('Display Image') 


#❛テキスト入力も作れる❜(インタラクティブなウィジェット(3))
#text = st.text_input('あなたの趣味を教えてください。') 
#'あなたの趣味:', text


#❛スライダーによる動的変化❜(インタラクティブなウィジェット(4))
#condition = st.slider('あなたの今の調子は？', 0, 100, 50) 
#'コンディション:', condition

#☆6.レイアウト作成(以下の３つを学ぶ)
# サイドバーの追加、ツーカラムレイアウト、エクスパンダ―

#サイドバー
#あなたの趣味を教えてください。と、あなたの今の調子は？
#の２つをサイドバーに追加したい時
#textとsliderのそれぞれの前にsidebarを追加して書けばサイドバーに表示される
text = st.sidebar.text_input('あなたの趣味を教えてください。') 
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50) 

'あなたの趣味:', text
'コンディション:', condition