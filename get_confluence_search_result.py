import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_confluence_search_result (get_slack_message):
    # confluence認証情報をjsonファイルから取得する
    json_open = open('user_config.json', 'r')
    json_load = json.load(json_open)
    confluence_url = json_load['CONFLUENCE_URL']
    mail_ad = json_load['MAIL_AD']
    user_id = json_load['USER_ID']
    password = json_load['PASSWORD']

    # webドライバーの設定
    options = webdriver.ChromeOptions()
    # webブラウザを開かないように設定
    # options.add_argument('--headless')

    # webドライバー起動
    driver = webdriver.Chrome(options=options)
    driver.get(confluence_url)
    driver.implicitly_wait(time_to_wait=30)
    # Confluenceの基本ページにアクセス
    e1 = driver.find_element(By.ID, 'google-auth-button')
    e1.click()
    driver.implicitly_wait(time_to_wait=30)
    e2 = driver.find_element(By.ID, 'identifierId')
    e2.send_keys(mail_ad)
    e3 = driver.find_element(By.ID, 'identifierNext')
    e3.click()
    driver.implicitly_wait(time_to_wait=30)
    e4 = driver.find_element(By.ID, 'rawUsername')
    e4.send_keys(user_id)
    e5 = driver.find_element(By.CLASS_NAME, 'btn-primary')
    e5.click()
    driver.implicitly_wait(time_to_wait=30)
    e6 = driver.find_element(By.ID, 'password')
    e6.send_keys(password)
    e7 = driver.find_element(By.CLASS_NAME, 'btn-primary')
    e7.click()
    driver.implicitly_wait(time_to_wait=30)
    e8 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
    e8.click()

    # 検索処理
    driver.implicitly_wait(time_to_wait=30)
    e9 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/header/div/div[2]/div/div/div/div/div[1]/div/input')
    e9.send_keys(get_slack_message)
    e9.send_keys(Keys.ENTER)
    time.sleep(3)
    e10 =  driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/main/div/div[1]/div/main/div[2]/div/form/div/div/div/div/div[2]/div[2]/button')
    e10.click()
    time.sleep(20)
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

get_confluence_search_result("旅費精算のやり方を教えて")
