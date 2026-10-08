# アプリケーション名

html_mail_generator

## 作成した目的

Pythonを用いた業務自動化・HTMLメール生成の練習。
雛形のHTMLメールテンプレートをもとに、ターミナルから必要な情報を入力することで、HTMLを自動生成するツールを作成。
HTMLの本文・セクション・ボタンなどの可変部分をPythonから設定し、Jinja2を利用して反映する処理を実装。
また、入力値のバリデーション、生成前の確認、既存ファイルの上書き確認などの処理も実装。

### URL

- GitHub：https://github.com/BRina1016/html_mail_generator

### 機能一覧

・HTMLメール生成
・出力ファイル名入力
・メール本文入力
・メール本文の改行入力対応
・可変セクション生成
・セクションごとの本文表示・非表示設定
・セクションごとのボタン表示・非表示設定
・本文のみのセクション生成
・ボタンのみのセクション生成
・本文＋ボタンのセクション生成
・本文・ボタンがないセクションの自動除外
・セクション数を自由に設定できる機能
・ボタンURL入力
・ボタン文言入力
・入力値バリデーション
・URL形式チェック
・空欄チェック
・y/n入力チェック
・生成前の入力内容確認機能
・生成キャンセル機能
・出力フォルダ自動作成機能
・既存HTMLファイルの上書き確認

### 使用技術(実行環境)

- Python 3.13
- Jinja2
- HTML
- CSS
- JSON

### 使用ライブラリ

Jinja2
HTMLテンプレートとPython側のデータを連携するために使用。
Python側で設定したセクション情報をJinja2のfor文・if文を利用してHTMLへ反映。

### アプリケーション構成

html_mail_generator/
├── generate.py
├── data/
│ └── mail_data.json
├── template/
│ └── mail.html
└── output/

generate.py
　HTMLメール生成処理を行うメインプログラム。
　入力値の取得、バリデーション、セクション情報の生成、確認処理、HTML生成、ファイル保存を行う。

mail_data.json
　HTMLメールのデータを管理するJSONファイル。
　メール本文、セクション、フッターなどの情報を管理。

mail.html
　HTMLメールのテンプレート。
　Jinja2を利用し、Python側から渡されたデータをHTMLへ反映。

output
　生成したHTMLメールを保存するフォルダ。
　存在しない場合はPython側で自動作成。

### 可変セクション

本アプリケーションでは、HTMLメール内のセクションを固定せず、Python側でリストとして管理。
各セクションごとに、本文とボタンを個別に表示・非表示設定。

sections = [
{
"show_text": True,
"text": "セクション1の本文",
"show_button": True,
"button_text": "詳しく見る",
"button_url": "https://example.com/1"
},
{
"show_text": False,
"text": "",
"show_button": True,
"button_text": "商品を見る",
"button_url": "https://example.com/2"
},
{
"show_text": True,
"text": "セクション3の本文",
"show_button": False,
"button_text": "",
"button_url": ""
}
]

### 処理フロー

・ターミナルから出力ファイル名を入力
・メール本文を入力
・セクションを追加するか設定
・セクションごとに本文の表示・非表示を設定
・本文を表示する場合は本文を入力
・セクションごとにボタンの表示・非表示を設定
・ボタンを表示する場合はボタン文言とURLを入力
・次のセクションを追加するか設定
・入力内容を確認
・Jinja2を使用してHTMLメールを生成
・outputフォルダへHTMLファイルを保存

### セットアップ

1. リポジトリをクローン
   　　git clone <https://github.com/BRina1016/html_mail_generator>

2. プロジェクトディレクトリへ移動
   　　cd html_mail_generator

3. 仮想環境を作成
   　　python3 -m venv .venv

4. 仮想環境を有効化
   　　source .venv/bin/activate

5. Jinja2をインストール
   　　pip install Jinja2

### 実行方法

仮想環境を有効化した状態で、以下のコマンドを実行。
python generate.py

画面の指示に従って、出力ファイル名・メール本文・セクション・ボタン情報などを入力。

入力内容を確認してyを入力するとHTMLメールが生成。

生成されたHTMLファイルはoutputフォルダに保存。
