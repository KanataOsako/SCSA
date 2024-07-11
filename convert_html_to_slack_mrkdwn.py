from bs4 import BeautifulSoup
from markdownify import markdownify as md
import subprocess


def convert_html_to_slack_mrkdwn(dict_user_config):

    # HTMLをMarkdownに変換
    markdown_output = convert_html_to_markdown(
        open(dict_user_config["file_path_html"], "r", encoding="utf-8")
    )
    # MarkdownをSlack用Mrkdwnに変換
    mrkdwn_output = convert_markdown_to_slack_mrkdwn(markdown_output)
    # Slack用に編集したHTMLをMarkdownファイルに書き込む
    create_result_mrkdwn(mrkdwn_output, dict_user_config)


def convert_html_to_markdown(html_content):
    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(html_content, "html.parser")
    # 残りのHTMLをマークダウンに変換
    markdown_content = md(str(soup), heading_style="ATX")
    return markdown_content


def convert_markdown_to_slack_mrkdwn(markdown_text):
    result = subprocess.run(
        ["node", "convert.js", markdown_text],
        encoding="utf-8",
        capture_output=True,  # capture_output を使うことで stdout と stderr を取得
        text=True,
    )

    if result.returncode != 0:
        raise Exception(f"Error: {result.stderr.strip()}")

    return result.stdout.strip()


def create_result_mrkdwn(mrkdwn_output, dict_user_config):
    file_path = dict_user_config["file_path_markdown"]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(mrkdwn_output)
