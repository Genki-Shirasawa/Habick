# 習慣可視化アプリ "Habick"
[![logo](https://user-images.githubusercontent.com/74233278/145626939-e65973b2-8396-486b-bb88-05560f48c686.png)](https://habick.org)*(URL : [https://habick.org](https://habick.org))*

今のあなたの習慣が残りの人生の何％を占めているのかを可視化し、危機感を与え、習慣改善のきっかけを作るWebアプリです。


1. [デモ画面](https://github.com/Genki-Shirasawa/Habick#%E3%83%87%E3%83%A2%E7%94%BB%E9%9D%A2)
2. [テスト用アカウント](https://github.com/Genki-Shirasawa/Habick#%E3%83%86%E3%82%B9%E3%83%88%E7%94%A8%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88)
3. [使用技術](https://github.com/Genki-Shirasawa/Habick#%E4%BD%BF%E7%94%A8%E6%8A%80%E8%A1%93)
4. [機能一覧](https://github.com/Genki-Shirasawa/Habick#%E6%A9%9F%E8%83%BD%E4%B8%80%E8%A6%A7)
5. [工夫した点](https://github.com/Genki-Shirasawa/Habick#%E5%B7%A5%E5%A4%AB%E3%81%97%E3%81%9F%E7%82%B9)
6. [ローカルでの動作方法](https://github.com/Genki-Shirasawa/Habick#%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%AB%E3%81%A7%E3%81%AE%E5%8B%95%E4%BD%9C%E6%96%B9%E6%B3%95)
7. [実装予定の機能](https://github.com/Genki-Shirasawa/Habick#%E5%AE%9F%E8%A3%85%E4%BA%88%E5%AE%9A%E3%81%AE%E6%A9%9F%E8%83%BD)
8. [作成者情報](https://github.com/Genki-Shirasawa/Habick#%E4%BD%9C%E6%88%90%E8%80%85%E6%83%85%E5%A0%B1)


# デモ画面

![habick_top](https://user-images.githubusercontent.com/74233278/145671890-a854f189-a655-4d4b-80f7-2500672fd7cd.png)  


# テスト用アカウント

以下のアカウントで[ログイン](https://habick.org/login/)すると、ユーザー登録不要でアプリを楽しめます。   
ユーザー名 : test  
パスワード : test1209


# 使用技術
- 言語
  - Python 3.7
  - HTML
  - CSS
  - JavaScript
- FW
  - Django 3.1.4
  - BootStrap 5.1
- インフラ
  - Nginx
  - Gunicorn
  - Vultr
- DB
  - SQLite


# 機能一覧

- ユーザーの登録機能 ([signupfunc](https://github.com/Genki-Shirasawa/Habick/blob/1556bcbc95a96defed766292e7d1edc9278ad41b/habitapp/views.py#L16))
- ログイン機能 ([loginfunc](https://github.com/Genki-Shirasawa/Habick/blob/1556bcbc95a96defed766292e7d1edc9278ad41b/habitapp/views.py#L32))
- ログアウト機能 ([logoutfunc](https://github.com/Genki-Shirasawa/Habick/blob/1556bcbc95a96defed766292e7d1edc9278ad41b/habitapp/views.py#L51))
- 習慣の登録機能 ([HabitCreate](https://github.com/Genki-Shirasawa/Habick/blob/1556bcbc95a96defed766292e7d1edc9278ad41b/habitapp/views.py#L73))
- 習慣の削除機能 ([HabitDelete](https://github.com/Genki-Shirasawa/Habick/blob/1556bcbc95a96defed766292e7d1edc9278ad41b/habitapp/views.py#L87))
- 習慣の編集機能 ([HabitUpdate](https://github.com/Genki-Shirasawa/Habick/blob/1556bcbc95a96defed766292e7d1edc9278ad41b/habitapp/views.py#L93))


# 工夫した点

- pythonコーディング規約であるpep8に従い、可読性・保守性を意識して実装しました。
- BootStrapを用いることで、シンプルかつレスポンシブなUIに仕上げました。


# ローカルでの動作方法

python、gitがインストール済みの環境で行ってください。

1. リポジトリをクローンする
```bash
git clone https://github.com/Genki-Shirasawa/Habick.git
```
2. リポジトリに移動
```bash
cd Habick
```
3. 仮想環境の構築&立ち上げ
```bash
python -m venv myvenv
source myvenv/bin/activate
```
4. 必要なライブラリ等をインストールする
```bash
pip install -r requirement.txt
```
5. サーバーを立ち上げる
```
python manage.py runserver
```


# 実装予定の機能

- [ ] 習慣の可視化機能
- [ ] 命のタイマー機能
- [ ] 本番環境用にDBの変更


# 作成者情報

- 作成者 : 白澤　元気
- 所属 : 鹿児島大学大学院　理工学研究科　海洋土木工学プログラム
- E-mail : bjuuh268@gmail.com
