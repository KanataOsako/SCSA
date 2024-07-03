import os
import json
from get_confluence_search_result import get_confluence_search_result
from post_slack import post_slack
from slack_bolt import App
from convert_html_to_slack_mrkdwn import convert_html_to_slack_mrkdwn

# jsonファイル名
JSON_FILE_NAME = "user_config.json"


# ボットトークンと署名シークレットを使ってアプリを初期化します
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


@app.message()
def main(message):
    # jsonファイルから設定値を取得
    dict_user_config = get_user_config(JSON_FILE_NAME)
    # confluence検索処理
    get_confluence_search_result(message["text"], dict_user_config)
    # html→slackのmrkdwnに変換処理
    convert_html_to_slack_mrkdwn(dict_user_config)
    # slack通知処理
    post_slack(dict_user_config)


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))


def get_user_config(json_file_name):
    # jsonファイル読み込み
    json_open = open(json_file_name, "r")
    json_load = json.load(json_open)
    # 接続先confluenceURL
    confluence_url = json_load["CONFLUENCE_URL"]
    # メールアドレス
    mail_ad = json_load["MAIL_AD"]
    # ユーザーID
    user_id = json_load["USER_ID"]
    # パスワード
    password = json_load["PASSWORD"]
    # output用htmlファイルパス
    file_path_html = json_load["FILE_PATH_HTML"]
    # output用markdownファイルパス
    file_path_markdown = json_load["FILE_PATH_MARKDOWN"]
    # slackトークン
    slack_token = json_load["SLACK_TOKEN"]
    # slackチャンネルID
    slack_channel_id = json_load["SLACK_CHANNEL_ID"]

    dict_user_config = {
        "confluence_url": confluence_url,
        "mail_ad": mail_ad,
        "user_id": user_id,
        "password": password,
        "file_path_html": file_path_html,
        "file_path_markdown": file_path_markdown,
        "slack_token": slack_token,
        "slack_channel_id": slack_channel_id,
    }
    return dict_user_config
