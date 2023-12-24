import streamlit as st
import numpy as np
import pandas as pd

#タイトルを付ける
st.title('Streamlit 入門')

#データフレームつまり表を扱うのでDataFrameというのを追加
#st.write('DataFrame')

#表(データフレームdf)を作成,表の書き方①
df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

#データフレームを表示
#st.write(df)

#表の他の書き方②　dataframeと書く
#dataframeと書くと指定できる引数とかあるらしい
#widthとheightで横と縦の長さを指定できたりする
st.dataframe(df)

#dataframeの良さとして例えば,引数を入れてあげると
#表の大きさを変えられる。これはwriteではできずdataframeにはできるのだ。
#tableというので書いても同じく表の大きさを変えられる。
st.dataframe(df, width = 200, height = 100)

#styleの中にhighlightというのがある。上でdfでpdのものを呼んで代入しているので
#highlightというかhighlight_maxはパンダスに用意されている機能ではあるが
#利用すると簡単に表に変更を加えられたりして便利。
#highlight_maxとすると行の中もしくは列の中で
#最大のものをハイライトすることができる。
#highlightの機能を使うようなときは、dfに.styleをつけて
#表のスタイルについて設定するぞと認識させるみたいだね。
st.dataframe(df.style.highlight_max, width = 200, height = 100)

#例えば、列の最大値にハイライトを付けたい場合は
#axisに0を入れる。行の最大値ならaxisに1を入れる。
st.dataframe(df.style.highlight_max(axis=0))


#テーブルを作成する方法③
#tableというのが使える
#上で設定したdfを呼ぶ
st.table(df)

#スタイルを付けるならば
st.table(df.style.highlight_max(axis=0))

#st.tableはスタティックな(静的な)テーブルを作りたい時に使う
#writeやdataframeと違って、tableはソート(カラムをクリックして順番を入れ替える)
#のができないのだ。だから、tableはただ表を作るだけって時に使う
#反対に動的なテーブルを作りたいときはdataframeが良い。
#ソートはしたいけど、別に表の幅とか高さ、ハイライトなどいらなければwriteでいい。

#データの表示のさせ方をもう少し詳しく見たければ
#streamlitのサイトに行きドキュメントってところに
#Tutorilasの中のREFERENCEの中にAPI reference
#という中にいくつかあって、Display dataを見てみると
#上で学んだ、streamlit.dataframeとかstreamlit.tableとかの解説とかあって
#データを表示させるときによく使うような機能がまとめられている。

#マジックコマンド""" """というのについてやる（詳しくはやらないけど便利なので調べてみてねだって）
#"""はpythonの文字列
#マークダウン記法を""" """の中に記述出来るらしい
# #をつける数によって文字の大きさが変えられる
#pythonのコードを書きますよって時は```python ``` とするらしい
#詳しくはstreamlitのサイト>ドキュメント>
# Tutorilas>REFERENCE>API reference>display textを探してみるといい
#streamlit.textとかstreamlit.markdownとか載っている
#マークダウンの記述はそこに書いてあるmarkdownを使っても書けるし
# 今回のマジックコマンド""" """でも書ける
#他にTex(テフと読む)というのも書ける

"""
# 章
## 節
### 項

```python

import streamlit as st
import numpy as np
import pandas as pd
```

"""



