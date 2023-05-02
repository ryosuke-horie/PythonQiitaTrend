# Qiitaのトレンドを取得する。
# API：https://qiita-api.vercel.app/api/trend

# ライブラリのインポート
import requests # HTTPリクエストを送る
import json # JSON形式のデータを扱う

# Qiitaのトレンドを取得する関数
def get_qiita_trend():
    # APIにリクエストを送る
    response = requests.get('https://qiita-api.vercel.app/api/trend')

    # JSON形式のデータを辞書型に変換する
    data = json.loads(response.text)

    # トレンドのタイトルとURLを表示する
    for i in range(len(data)):
        print(data[i]['node']['title'])
        print(data[i]['node']['linkUrl'])
        print()

# 単体で実行した場合
if __name__ == '__main__':
    get_qiita_trend()

