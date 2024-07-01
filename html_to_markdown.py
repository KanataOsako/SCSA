from bs4 import BeautifulSoup
from markdownify import markdownify as md
import html2text

def html_to_markdown(html_content):
    # BeautifulSoupを使ってHTMLをパースする
    soup = BeautifulSoup(html_content, 'html.parser')

    # html2textを使用してHTMLをMarkdownに変換する
    markdown_content = html2text.html2text(str(soup))

    return markdown_content

def html_to_markdown2(html_content):
    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(html_content, 'html.parser')
    # 残りのHTMLをマークダウンに変換
    markdown_content = md(str(soup), heading_style="ATX")
    return markdown_content
