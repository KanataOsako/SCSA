import requests


def post_slack(dict_user_config):
    # Slack API Token (OAuth Access Token)
    slack_token = dict_user_config["slack_token"]
    # SlackチャンネルID
    slack_channel_id = dict_user_config["slack_channel_id"]

    # mrkdwnファイルのパス
    file_path = dict_user_config["file_path_markdown"]

    # mrkdwnファイルの内容を読み込む
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Slackに投稿するメッセージの準備
    message = {
        "channel": slack_channel_id,
        "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": content}}],
    }

    # リクエストヘッダにトークンを設定
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {slack_token}",
    }

    # Slack APIにPOSTリクエストを送信してメッセージを投稿
    response = requests.post(
        "https://slack.com/api/chat.postMessage", headers=headers, json=message
    )

    # レスポンスを確認（エラーハンドリングなどは適宜追加してください）
    if response.status_code == 200:
        print("Slackに検索結果を送信しました。")
    else:
        print(
            f"エラー: Slack APIでエラーが発生しました - {response.status_code}, {response.text}"
        )
