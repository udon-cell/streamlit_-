import streamlit as st
import numpy as np
import pandas as pd

#☆3.マップ作成
#Pandasのデータフレームで用意していく


df = pd.DataFrame(
    np.random.rand(100,2), #100個プロットしたい、2行欲しい
    #カラム名を指定 
    columns = ['lat', 'lon'] #latitude:緯度とlongitude:経度
)
#st.dataframe(df)


#ランダムだと緯度と経度の値が正確ではないので
#試しに東京付近の緯度経度を指定してプロットしようと思います。
df = pd.DataFrame(
    #0.5度緯度が違うとだいぶ場所がずれるので
    #緯度や軽度の桁を下げる為に割り算して50で割ってみようと思います。
    #小さな値なら足しても誤差はないかなと思います。
    #ランダムに出した数字に東京付近の緯度経度を足してあげる
    #すると、大体35.69度付近の緯度と139.70付近の経度の
    # ランダムな値というか座標ができる
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70], 
    columns = ['lat', 'lon'] #latitude:緯度とlongitude:経度
)
df #dfと書くとdfに入った内容が表示される

#上記の緯度経度を元にマッピングしていく mapを利用する
#ランダムな数値が書かれた表を呼び込んで、マップが作成できる
st.map(df)

#応用例として、店の情報(緯度経度)が分かればマッピングできることになる
#streamlit>tutorial>API referemceを見ればマッピングの使用詳細が知れるよ
#今回のはScatterplots on mapsというので調べられる。