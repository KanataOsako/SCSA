import requests
from bs4 import BeautifulSoup

# スクレイピング対象のhtmlファイルからsoupを作成
soup = BeautifulSoup(open('output.html'), 'html.parser')
