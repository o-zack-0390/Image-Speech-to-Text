# Image-Speech-to-Text
URL : <a href="https://o-zack-0390-image-speech-to-text-app-hqfvv0.streamlit.app/">Image-Speech-to-Text</a><br>
「😴」が表示されてる場合は「Yes, get this app back up!」を押して起動してください。

<h3>概要</h3>
画像ファイルと音声ファイルから文字起こしをする。無料枠を使用しているため以下の制限がある。<br><br>
<ul>
  <li>画像ファイルはjpgファイルのみ対応</li>
  <li>音声ファイルはwavファイルのみ対応</li>
  <li>容量200MBとなっているが無料枠なので実際は20M程度</li>
  <li>データサイズが無料枠を超過している場合はエラーメッセージを表示</li>
  <li>容量が大きいサイズは無料枠を超えないサイズまで分割して使用することになる</li>
</ul>
スマホから使用することも多いため不要な処理を極力排除してレスポンス時間が短くなるようにしている。<br><br>

<h3>開発背景</h3>
研究のzoomミーティングでは、共有されている画面に書いてあることを必死にメモすることが多く、教授の話をメモすることも多いが、これらを手書きで行うには限界があり、どうしてもメモできない箇所が毎回あった。<br>
そこで、画像から文字起こしが可能で、音声からも文字起こしができるアプリがあれば便利だと思い作成した。<br>
Google社の文字起こしサイトを使用する方法も考えたが、「Google社の無料枠だと使用回数・使用容量に制限が掛かる」ので回数に制限がないstreamlitで実装することにした。<br><br>

<h3>開発言語</h3>
python3<br><br>

<h3>ライブラリ</h3>
Tesseract-Ocr<br>
SpeechRecognition<br><br>

<h3>フレームワーク</h3>
Streamlit<br><br>

<h3>使用方法(Speech to Text)</h3>
1. 「変換方法の選択」で「Speeech to Text」を選択<br>
2. 　waveファイルをアップロード<br>
3. 「テキストに変換」を押す<br><br>
<img width="579" alt="image" src="https://user-images.githubusercontent.com/116938721/220658035-16125175-2fdf-44ef-b7f2-f1d5ea2cb0de.png">

音声ファイル<br>
<a href="https://www.city.kasugai.lg.jp/_res/projects/default_project/_page_/001/016/637/310415-02a.mp3">声の広報かすがい　4月15日号（NO.698）</a>
<br><br>

<h3>使用方法(Image to Text)</h3>
1. 「変換方法の選択」で「Image to Text」を選択<br>
2.　jpgファイルをアップロード<br>
3. 「テキストに変換」を押す<br><br>

<img width="593" alt="image" src="https://user-images.githubusercontent.com/116938721/220660467-7af39c89-cc8f-430d-8638-b2fc9c52e822.png">

画像ファイル<br>
<img width="560" alt="image" src="https://user-images.githubusercontent.com/116938721/221807393-42a7e64c-6532-4561-b0ae-8992cb56e6f5.png">
<br><br>

元資料<br>
<a href="https://www.city.kasugai.lg.jp/covid19/1023611/1019477.html">新型コロナウイルス感染症の予防</a>
