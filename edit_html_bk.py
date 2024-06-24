from bs4 import BeautifulSoup
import re

def html_to_markdown(html_content):
    # BeautifulSoupを使ってHTMLを解析
    soup = BeautifulSoup(html_content, 'html.parser')

    # リスト要素の変換
    def list_element(tag):
        if tag.name == 'ul':
            return '\n'.join(['- ' + li.text.strip() for li in tag.find_all('li')])
        elif tag.name == 'ol':
            return '\n'.join([str(i + 1) + '. ' + li.text.strip() for i, li in enumerate(tag.find_all('li'))])
        return None

    # リンク要素の変換
    def link_element(tag):
        return f"[{tag.text.strip()}]({tag['href']})"

    # 画像要素の変換
    def image_element(tag):
        alt = tag.get('alt', 'image')
        return f"![{alt}]({tag['src']})"

    # コードブロック要素の変換
    def code_element(tag):
        return f"```\n{tag.text.strip()}\n```"

    # 各要素の変換関数を定義
    markdown_transformations = {
        'h1': lambda tag: f"# {tag.text.strip()}",
        'h2': lambda tag: f"## {tag.text.strip()}",
        'h3': lambda tag: f"### {tag.text.strip()}",
        'h4': lambda tag: f"#### {tag.text.strip()}",
        'h5': lambda tag: f"##### {tag.text.strip()}",
        'h6': lambda tag: f"###### {tag.text.strip()}",
        'p': lambda tag: f"{tag.text.strip()}",
        'ul': list_element,
        'ol': list_element,
        'a': link_element,
        'img': image_element,
        'code': code_element,
        'pre': code_element,
        'blockquote': lambda tag: f"> {tag.text.strip()}",
        'br': lambda tag: "\n",  # <br>タグの変換
        'hr': lambda tag: "---\n",  # <hr>タグの変換
    }

    # HTMLをMarkdownに変換する関数
    def convert_tag(tag):
        if tag.name in markdown_transformations:
            return markdown_transformations[tag.name](tag)
        return ""

    # 各タグをMarkdownに変換
    markdown_content = '\n'.join(convert_tag(tag) for tag in soup.find_all())

    return markdown_content.strip()

# テスト用のHTMLサンプル
html_sample = open('./output.html','r',encoding="utf-8")

# HTMLをMarkdownに変換して出力
markdown_output = html_to_markdown(html_sample)
print(markdown_output)
