# 文献リストジェネレーター
## 趣旨
 * 西洋史学徒(特に京都大学文学研究科西洋史学研究室)向け
  * 「念頭に置いてつくった」程度の意で、他の人が使えないというわけではもちろんない
 * 普段は、並べ替えのしやすい、表計算ソフトで文献を管理しつつ、本番ではワードプロセッサソフトに文献リストを貼り付けたい
 * 表計算ソフトからコピペすると表として貼り付けられてうざい
  * どうも回避不能な模様
 * EndNote BasicやRefWorksも微妙でかゆい所に手が届かない状態
  * EndNote の有償版ではできる模様
  * でも買ってまでなぁ……。
 * そもそも、国や地域の違いで表記の仕方が違う => フルカスタマイズできるようにすればいいのでは
 * 前から温めていた案をさくっと実装したので、公開してみた
 * 何かコードを書きたかったというのが動機として大きいので、無償でいいサービスあったら教えてください

## ファイル
 1. gen_bib.py
  * ジェネレーター
 1. biblist.csv
  * 文献情報を入れるCSVファイル
 1. formats.csv
  * 文献リストのフォーマットを保管するCSVファイル

## 使い方
### Python3系をインストールする
 1. Python3.x を [http://www.pythonweb.jp/install/install/index1.html#section1] を参考にインストールする

### フォーマットを設定する
 1. formats.csv を表計算ソフトで開く
 1. 「文献種別」の列にフォーマットを設定したい文献の種別名(任意)を入力する(ex.' 英書')
 1. 「書式」の列に当該文献種別のフォーマットを書いていく
 1. 実際の文献情報で埋めたい項目名(任意)を '{ }' でくくってフォーマットを書く(ex. {題名})
 1. イタリック体にする必要があるところは '///' で挟む(ex. ///{題名}///)

### 文献情報を入力する
 1. biblist.csv を表計算ソフトで開く
 1. 1行目に formats.csv で設定した項目名を列挙する(順不同)
 1. 使わない項目があってもよく、ただ無視されるだけ(ex. 「著者ふりがな」=> 日本語著者を50音順に並べるための項目だが、文献リストには表示させない)
 1. 「文献種別」はどこに置いても良いが formats.csv の当該文字列と一致していなければならない
 1. 項目名を埋めてゆく
 1. 表示させたい順に表計算ソフトの機能を駆使して並べる
 1. CSVは書式を保持できないので、普段は使っている表計算ソフトの形式で取り扱って、必要に応じてCSVとして書き出すのがおすすめ

### 文献リストを生成・利用する
 1. gen_bib.py をダブルクリックする
 1. results.html が生成されるのでブラウザで開く
 1. 文献リストが表示されるので必要な部分をコピーする
 1. ワードプロセッサソフトで開いて貼り付ける
 1. フォントの種類、フォントサイズを設定する
 1. 終わり

### コマンドラインオプション
 使用法: 
  ```
  ./gen_bib.py [path_to_formats.csv] [path_to_biblist.csv]
  python gen_bib.py [path_to_formats.csv] [path_to_biblist.csv]
  ```
 
 媒体によって表記が異なる場合は、 formats.csv を書き分ければ、同じ biblist.csv を使いまわせる
 単純にフォルダごとコピペすれば同様のことは実現できるが、その場合は、同期を忘れないこと

## TODO
 1. エラー時の処理(現状、おかしいところがあると落ちるだけ)
 1. エンコーディングの自動判別(現状、Windows + Excelでの利用を想定して、SJISに決め打ち状態)
 1. コマンドラインオプションで出力先ファイル名も指定できるようにする
 1. TeX向けの出力(?)
