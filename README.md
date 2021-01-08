# 2020年：ロボットシステム学課題２
## 目的
第10回で作成したROSのパッケージをベースに、オリジナリティーある改造をし、GitHubに置くこと。
## リポジトリ概要
ROSを使用し、３つのファイル間で通信しまるで誰かと会話しているように思えるようなパッケージを作成しました。  
「**scripts**」  
プログラムがここに入っています。  
`reply1`のパブリッシャにいれた入力に対して`Noko`が返信してくれます。  
`mid1.py`のファイルは受け取ったデータから反応を決定し返信を考えるという中間ファイルです。また何回会話したかの回数が表示されます。  
`receive1.py`ここで`Noko`からの返信が見れます。  
`count.py・twice.py`授業でやったやつです。countは数値を10hzで出して画面に表示します、twiceはそれを倍にします。今回のメインではありませんがとりあえず置いておきます。  
「**CmakeLists.txt**」  
このパッケージにおけるmakefileです。  
「**LICENSE**」  
このパッケージにおけるライセンスです。  
「**README.md**」  
読んでください。  
「**package.xml**」  
パッケージの情報がまとめてあります。  
### 会話パターン
YOU --- "Hello,Noko"　Noko --- "Hello,human"  
YOU --- "See You,Noko"　Noko --- "See you"　＋exit方法を教えてくれます。  
YOU --- "How about you?"　Noko --- "?????"　彼女の返答は３パターンあります！Nokoの気分次第ですね…！  
上記以外の入力 "error"  
## 動作環境
Ubuntu 20.04LTS
## デモ動画のリンク

## インストール手順
・自身のcatkin_ws内のsrcに移動、なければ作成しこのリポジトリのcodeをgit cloneする
## 使用方法
`cd catkin_ws/src/mypkg`
端末を4つ開き`roscore` `rosrun mypkg reply1.py` `rosrun mypkg mid1.py` `rosrun mypkg receive1.py`を実行する。
## ライセンス
BSD 3-Clause License
