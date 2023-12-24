import streamlit as st
import numpy as np
import pandas as pd

#☆2.チャートの作り方

'''
df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})
'''
#上の表からデータの中身を変えたいと思います。
#DataFrameで表を作成
    #numpyのrandom関数ぽいの.randで範囲指定みたいな感じ
    #行列を作る。縦に20個横に3個の行列を作る
    #randomで乱数を作る
    #random.randが正規分布を元に乱数を作成とかなんとか
    #正規分布が分からない人は調べておいてください
    #ある規則性のあるというか形をしたグラフからデータを取ってきている
df = pd.DataFrame(
    np.random.rand(20,3), 
    #カラム名を指定 
    columns = ['a', 'b', 'c']
)
st.dataframe(df)
#上記の表のデータを折れ線グラフでまずは表示したいと思います
#streamlitのline_chartというのを使用してdfのデータを入れてあげればいい
#dataframeのカラムはそれぞれ折れ線として表示されていく
#出来た折れ線グラフをSVGとかPNG形式で方法できたりもする
st.line_chart(df)

#line_chartに似たものとしてarea_chartというものがある
#折れ線グラフの中を塗りつぶしてあるのが特徴
st.area_chart(df)

#バーチャート(棒グラフ)を作ることも出来る
st.bar_chart(df)

#こういったグラフにつかえるもの、チャート形式は
#streamlit>tutorial>API reference>Display chartsに載っている
#あと、例えば、streamlit_line_chartにもあるParametersとあるが
#こういったParametersがいわゆる引数となるよ