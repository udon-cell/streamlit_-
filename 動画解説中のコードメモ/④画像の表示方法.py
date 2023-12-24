import streamlit as st
import numpy as np
import pandas as pd



#☆4.画像を表示させる
#画像を表示させるためにはPILというライブラリを使用する
from PIL import Image #Imageというのを書いてくださいだってさ

st.write('Display Image') #Display Imageと書いておいてくださいだってさ

#画像を読み込みたいので画像(ファイル名をsample.jpegとした)を用意
#画像を読み込み importに書いたImageを書く
#Image.openで画像を開く
#()内に写真の格納先を書く
#今回は作業ファイルと同じ階層にある画像を使うのでファイルの名前だけ
#を書けば済むらしい
img = Image.open('猫.jpg')
#これだけだと表示させられないのでst.imaegeで表示させる
#st.image(img)でまず画像を入れて、captionを追加して、
# captionでキャプションを表示。キャプションとは写真・図版に添えられた説明文
#use_column_widthを設定することが多く、これは
# 実際のウェブアプリのカラムを実際のレイアウトに合わせて表示してくれる
#アプリのカラムというのが、タイトルとか図とかを表示する場所の幅みたいな
#ことを指すみたいで、それは決まってるんだけど、
#use_column_widthはそれを他のものに合わせて調度収まる幅に
#変えてくれるというか調節してくれる機能だったと思うとのこと。
st.image(img, caption = '猫を下から眺める',use_column_width = True)

#画像以外のメディアを表示することもできるよ
#Streamlitのサイトでtutorial>API reference>Display media
#ということろを見てみるとstreamlit.imageという画像表示できるものが載っていて
#他にもstreamlit.audioを使えば、音楽を再生するボタンを表示させられる
#他にもビデオとかをのせる機能などもある。
#JavaScriptsとかHTMLと比べてこういった機能を載せるのが簡単なのが
#Streamlitの特徴らしい。