from html_to_markdown import html_to_markdown

def edit_html():
    # HTMLをMarkdownに変換
    markdown_output = html_to_markdown(open('./output.html','r',encoding="utf-8"))
    # 取得したHTMLデータをファイルに書き込む
    file_path = './output.md'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(markdown_output)
    print('HTML→MarkDownに変換しました。')


