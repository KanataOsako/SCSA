from bs4 import BeautifulSoup
from markdownify import markdownify as md
import html2text
import re
import commonmarkslack
from convert_markdown_to_mrkdwn import convert_markdown_to_slack_format

def html_to_markdown(html_content):
    # BeautifulSoupを使ってHTMLをパースする
    soup = BeautifulSoup(html_content, 'html.parser')

    # html2textを使用してHTMLをMarkdownに変換する
    markdown_content = html2text.html2text(str(soup))
    mrkdwn_content = convert_markdown_to_slack_format(markdown_content)
    return mrkdwn_content

def html_to_markdown2(html_content):
    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(html_content, 'html.parser')
    # 残りのHTMLをマークダウンに変換
    markdown_content = md(str(soup), heading_style="ATX")
    mrkdwn_content = convert_markdown_to_slack_format(markdown_content)
    return mrkdwn_content

# def convert__markdown_to_mrkdwn_2(markdown_text):
#     parser = commonmarkslack.Parser()
#     renderer = commonmarkslack.SlackRenderer()
#     ast = parser.parse(markdown_text.message.content.strip())
#     slack_md = renderer.render(ast)
#     return slack_md
