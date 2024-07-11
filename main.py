import os
import json
from get_confluence_search_result import get_confluence_search_result
from post_slack import post_slack
from slack_bolt import App
from convert_html_to_slack_mrkdwn import convert_html_to_slack_mrkdwn
from dotenv import load_dotenv

load_dotenv()


# ボットトークンと署名シークレットを使ってアプリを初期化します
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


def get_user_config():
    # 接続先confluenceURL
    confluence_url = os.environ["CONFLUENCE_URL"]
    # メールアドレス
    mail_ad = os.environ["MAIL_AD"]
    # ユーザーID
    user_id = os.environ["USER_ID"]
    # パスワード
    password = os.environ["PASSWORD"]
    # output用htmlファイルパス
    file_path_html = os.environ["FILE_PATH_HTML"]
    # output用markdownファイルパス
    file_path_markdown = os.environ["FILE_PATH_MARKDOWN"]
    # slackトークン
    slack_token = os.environ["SLACK_TOKEN"]
    # slackチャンネルID
    slack_channel_id = os.environ["SLACK_CHANNEL_ID"]

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


@app.message()
def main(message):
    # jsonファイルから設定値を取得
    dict_user_config = get_user_config()
    # confluence検索処理
    get_confluence_search_result(message["text"], dict_user_config)
    # html→slackのmrkdwnに変換処理
    convert_html_to_slack_mrkdwn(dict_user_config)
    # slack通知処理
    post_slack(dict_user_config)


# Start your appqqq 
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
