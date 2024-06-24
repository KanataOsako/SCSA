
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
    file_path = './output.md'

    # HTMLファイルの内容を読み込む
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Slackに投稿するメッセージの準備
    message = {
        'channel': channel,
        'text': 'HTMLファイルの内容です:',
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': content
                }
            }
        ]
    }

    # リクエストヘッダにトークンを設定
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {slack_token}'
    }

    # Slack APIにPOSTリクエストを送信してメッセージを投稿
    response = requests.post('https://slack.com/api/chat.postMessage', headers=headers, json=message)

    # # slack投稿用の変数の定義 
    # url = "https://slack.com/api/chat.postMessage"
    # token = slack_token
    # channel_id = channel

    # header={"Content-Type": "application/json",
    #         "Authorization": "Bearer "+token}
    
    # # 投稿
    # res=requests.post(url,
    #                     headers=header,
    #                     data=json.dumps({
    #     "token":token,
    #     "channel":channel_id,
    #     'text': 'HTMLファイルの内容です:',
    #     'blocks': [
    #         {
    #             'type': 'section',
    #             'text': {
    #                 'type': 'mrkdwn',
    #                 'text': f'```\n{html_content}\n```'
    #             }
    #         }
    #     ]
    # }))
    # print(res.text)

    # レスポンスを確認（エラーハンドリングなどは適宜追加してください）
    if response.status_code == 200:
        print('SlackにHTMLファイルの内容を送信しました。')
    else:
        print(f'エラー: Slack APIでエラーが発生しました - {response.status_code}, {response.text}')
