import os
from get_confluence_search_result  import get_confluence_search_result
from post_slack  import post_slack
from slack_bolt import App
# ボットトークンと署名シークレットを使ってアプリを初期化します
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.message()
def message_hello(message):
    print(message['text'])
    get_confluence_search_result(message['text'])
    post_slack()

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
