import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def get_confluence_search_result(get_slack_message):
    # confluence認証情報をjsonファイルから取得する
    json_open = open('user_config.json', 'r')
    json_load = json.load(json_open)
    MAIL_AD = json_load['MAIL_AD']
    PASS = json_load['PASS']

    # webドライバーの設定
    options = webdriver.ChromeOptions()
    # webブラウザを開かないように設定
    # options.add_argument('--headless')
    # 処理終了時webブラウザが落ちないように設定
    options.add_experimental_option("detach", True)

    # webドライバー起動
    driver = webdriver.Chrome(options=options)
    driver.get(
    'https://kanata-osako.atlassian.net/wiki/home'
    )
    driver.implicitly_wait(time_to_wait=30)

    # メールアドレスセットする。
    driver.find_element(By.ID,'username').send_keys(MAIL_AD)

    # 続けるボタンを押下
    driver.find_element(By.ID,'login-submit').click()
    driver.implicitly_wait(time_to_wait=30)

    # パスワードを入力
    driver.find_element(By.ID,'password').send_keys(PASS)

    # ログインボタンを押下
    driver.find_element(By.ID,'login-submit').click()
    time.sleep(10)

    # 検索処理
    driver.find_element(By.CSS_SELECTOR, ".css-1ban08t").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".css-1k56oow").send_keys(get_slack_message)
    driver.find_element(By.CSS_SELECTOR, ".css-19t243v").click()
    time.sleep(20)
    # 検索結果をHTMLファイルに出力
    result = driver.find_element(By.CSS_SELECTOR, ".css-yeoe5q")
    result_html = result.get_attribute(name='innerHTML')

    # webドライバー終了
    driver.quit()

    # 取得したHTMLデータをファイルに書き込む
    file_path = './output.html'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(result_html)

    print(f"HTMLデータを {file_path} に保存しました。")
