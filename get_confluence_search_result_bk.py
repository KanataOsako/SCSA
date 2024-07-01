import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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
    e9 =  driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/header/div/div[2]/div/div/div/div/div[1]/div/input')
    e9.send_keys(get_slack_message)
    e9.send_keys(Keys.ENTER)

    time.sleep(3)
    e10 =  driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/main/div/div[1]/div/main/div[2]/div/form/div/div/div/div/div[2]/div[2]/button')
    e10.click()
    time.sleep(30)
    # 検索結果をHTMLファイルに出力
    result = driver.find_element(By.XPATH, '//*[@id="content-body"]/main/div[2]/div/div[2]/div[1]')
    result_html = result.get_attribute(name='innerHTML')

    # webドライバー終了
    driver.quit()

    # 取得したHTMLデータをファイルに書き込む
    file_path = './output.html'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(result_html)

    print(f"HTMLデータを {file_path} に保存しました。")

# get_confluence_search_result("confluenceについて教えて")
