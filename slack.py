from dotenv import load_dotenv
import json
import get_confluence_search_result
import post_slack

# Use the package we installed
from slack_bolt import App

json_open = open('user_config.json', 'r')
json_load = json.load(json_open)

# Initializes your app with your bot token and signing secret
load_dotenv()
app = App(
    token=json_load['SLACK_BOT_TOKEN'],
    signing_secret=json_load['SLACK_TOKEN']
)

@app.message()
def message_hello(message, say):
    print(message)
    get_confluence_search_result(message)
    # post_slack()
    # HTMLファイルのパス
    html_file_path = './output.html'

    # HTMLファイルの内容を読み込む
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Slackに投稿するメッセージの準備
    message = {
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
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"<@{message['user']}>Hey there!")

# Start your app
if __name__ == "__main__":
    # app.start(port=int(os.environ.get("PORT", 3000)))
    app.start(3000)  # POST http://localhost:3000/slack/events
