import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image 
import time #プログレスバーを表示させるために必要なライブラリをインポート

st.title('Streamlit 超入門')

st.write('Display Image') 

st.write('プログレスバーの表示')
'Start!!' #これは書いておいてと言われたが何のために使うの？
#何か表示したいときは'文字列'で表示できるみたいね、streamlitは。
#プログレスバーの表示が開始！って意味でただ書いていただけだった。


#☆プログレスバー
#/////////////////////////////////////////////////////////////////
latest_iteration = st.empty() #st.empty()で空の要素を追加　それをlatest_iterationとしたい

#プログレスバーを用意する
#st.progressは()内の値の型はintまたはfloat
# (整数の場合は)0 <= 値 <= 100、(浮動小数点の場合は) 0.0 <= 値 <= 1.0
bar = st.progress(0) 

##for i in range(100): #iという値に0から99まで計100個の数字が入っていく。
##    print(1)
##    time.sleep(0.1) #0.1秒スリープする(止まる)
for i in range(100):
    latest_iteration.text(f'反復 {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1) #これがないと一瞬で終ってしまう。これがあることでfor文の実行処理を遅らせている。
    #time.sleep()の中の数値は小さい方が早く処理が終わる。
    #sleepさせておく時間が短くなるので。
    
'Doe!' #for文の処理が終わったよ！って表現したいみたいだった。
#////////////////////////////////////////////////////////////////




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


    