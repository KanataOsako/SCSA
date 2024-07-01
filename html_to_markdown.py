from bs4 import BeautifulSoup
from markdownify import markdownify as md
import html2text
import re
import commonmarkslack

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
    # 見出し
    text = re.sub(r'(^|\n)###### (.*)', r'\1* \2 *', text)
    text = re.sub(r'(^|\n)##### (.*)', r'\1* \2 *', text)
    text = re.sub(r'(^|\n)#### (.*)', r'\1* \2 *', text)
    text = re.sub(r'(^|\n)### (.*)', r'\1* \2 *', text)
    text = re.sub(r'(^|\n)## (.*)', r'\1* \2 *', text)
    text = re.sub(r'(^|\n)# (.*)', r'\1* \2 *', text)
    
    # 強調（太字）
    text = re.sub(r'\*\*(.*?)\*\*', r'*\1*', text)
    text = re.sub(r'__(.*?)__', r'*\1*', text)
    
    # 強調（斜体）
    text = re.sub(r'\*(.*?)\*', r'_\1_', text)
    text = re.sub(r'_(.*?)_', r'_\1_', text)
    
    # コードブロック
    text = re.sub(r'```(.*?)```', r'```\1```', text, flags=re.DOTALL)
    
    # インラインコード
    text = re.sub(r'`(.*?)`', r'`\1`', text)
    
    # リンク
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<\2|\1>', text)
    
    return text

def convert__markdown_to_mrkdwn_2(markdown_text):
    parser = commonmarkslack.Parser()
    renderer = commonmarkslack.SlackRenderer()
    ast = parser.parse(markdown_text.message.content.strip())
    slack_md = renderer.render(ast)
    return slack_md