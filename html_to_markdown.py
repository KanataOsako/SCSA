from bs4 import BeautifulSoup
from markdownify import markdownify as md
import html2text
import re

def html_to_markdown(html_content):
    # BeautifulSoupを使ってHTMLをパースする
    soup = BeautifulSoup(html_content, 'html.parser')

    # html2textを使用してHTMLをMarkdownに変換する
    markdown_content = html2text.html2text(str(soup))
    mrkdwn_content = convert_markdown_to_mrkdwn(markdown_content)
    return mrkdwn_content

def html_to_markdown2(html_content):
    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(html_content, 'html.parser')
    # 残りのHTMLをマークダウンに変換
    markdown_content = md(str(soup), heading_style="ATX")
    mrkdwn_content = convert_markdown_to_mrkdwn(markdown_content)
    return mrkdwn_content

def convert_markdown_to_mrkdwn(markdown_text):
    # 太字
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'*\1*', markdown_text)
    # 斜体
    markdown_text = re.sub(r'\*(.*?)\*', r'_\1_', markdown_text)
    # リスト
    markdown_text = re.sub(r'^- ', r'• ', markdown_text, flags=re.MULTILINE)
    # リンク
    markdown_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<\2|\1>', markdown_text)
    return markdown_text
