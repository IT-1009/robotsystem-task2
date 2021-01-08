# robotsystem-task2
# 2020年：ロボットシステム学課題２
## 目的
ROSを使い、３つのファイル間で通信する
## プログラムの内容
「tuu.py」はパブリッシャ、「tuukaa.py」はサブスクライバとパブリッシャ、「kaa.py」はサブスクライバになっている
「tuu.py」で入力したデータは「tuukaa.py」を経由して、「kaa.py」で出力される
「tuukaa.py」でデータを変化させるため、「tuu.py」での入力内容によって、「kaa.py」の出力内容が変わる
「tuukaa.py」にデータを送受信した回数が表示される
### 入力と出力の変化
"Hello"　　　　　　　　　->　　"Hey Ya!"
"What are you doing?"　　->　　"I'm pooping now"
"DIO"　　　　　　　　　　->　　"THE WORLD!!!!!"
上記以外の入力　　　　　 ->　　"hello"
## 手順
1.ROSをインストールしておく
2.Git clone後、「myROS」ディレクトリに入る
3.端末のタブかターミナルを４つに分ける
4.それぞれで『roscore』『rosrun mypkg tuu.py』『rosrun mypkg tuukaa.py』『rosrun mypkg kaa.py』を実行する
5.「tuu.py」での入力が「kaa.py」に反映されている、「tuukaa.py」に通信回数が表示されているのを確認する
6.「tuu.py」は『CTRL+D』、それ以外は『CTRL+C』で終了する
### 注意
「tuu.py」で入力する際に、入力を""で挟ないとエラーになる
例）Hello    ->  エラー
　　"Hello"  ->  成功
