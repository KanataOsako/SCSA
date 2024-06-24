import requests
import json

def post_slack():
    # confluence認証情報をjsonファイルから取得する
    json_open = open('user_config.json', 'r')
    json_load = json.load(json_open)

    # Slack API Token (OAuth Access Token)
    slack_token = json_load['SLACK_TOKEN']

    # Slackチャンネル名またはID
    channel = json_load['SLACK_CHANNEL_ID']

    # HTMLファイルのパス
    html_file_path = './output.html'

    # HTMLファイルの内容を読み込む
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Slackに投稿するメッセージの準備
    message = {
        'token': slack_token,
        'channel': channel,
        'text': 'HTMLファイルの内容です:',
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': '```' + html_content + '```'
                }
            }
        ]
    }

    # Slack APIにPOSTリクエストを送信してメッセージを投稿
    response = requests.post('https://slack.com/api/chat.postMessage', json=message)

    # レスポンスを確認（エラーハンドリングなどは適宜追加してください）
    if response.status_code == 200:
        print('SlackにHTMLファイルの内容を送信しました。')
    else:
        print(f'エラー: Slack APIでエラーが発生しました - {response.status_code}, {response.text}')
