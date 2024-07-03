import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_confluence_search_result(get_slack_message, dict_user_config):
    # seleniumを使用してconfluence検索
    result_html = selenium_confluence_search(get_slack_message, dict_user_config)

    # 検索結果のHTMLデータをファイルに書き込む
    create_result_html(result_html, dict_user_config)

    print(f"HTMLデータを保存しました。")


def selenium_confluence_search(get_slack_message, dict_user_config):
    # webドライバーオプション
    options = webdriver.ChromeOptions()
    # webドライバーオプション（webブラウザを開かないように設定）
    # options.add_argument("--headless")
    # webドライバー起動
    driver = webdriver.Chrome(options=options)

    # Confluenceの基本ページにアクセス
    driver.get(dict_user_config["confluence_url"])
    driver.implicitly_wait(time_to_wait=30)

    # メールアドレスセットする。
    driver.find_element(By.ID, "username").send_keys(dict_user_config["mail_ad"])

    # 続けるボタンを押下
    driver.find_element(By.ID, "login-submit").click()
    driver.implicitly_wait(time_to_wait=30)

    # パスワードを入力
    driver.find_element(By.ID, "password").send_keys(dict_user_config["password"])

    # ログインボタンを押下
    driver.find_element(By.ID, "login-submit").click()
    driver.implicitly_wait(time_to_wait=30)

    # 検索処理
    # e8 = driver.find_element(
    #     By.XPATH,
    #     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button",
    # )
    # e8.click()
    # driver.implicitly_wait(time_to_wait=30)
    e9 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/header/div/div[2]/div/div/div/div/div[1]/div/input",
    )
    e9.send_keys(get_slack_message)
    e9.send_keys(Keys.ENTER)
    time.sleep(3)
    e10 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/main/div/div[1]/div/main/div[2]/div/form/div/div/div/div/div[2]/div[2]/button",
    )
    e10.click()
    time.sleep(20)

    # 検索結果をHTMLファイルに出力
    result = driver.find_element(
        By.XPATH, '//*[@id="content-body"]/main/div[2]/div/div[2]/div[1]'
    )
    result_html = result.get_attribute(name="innerHTML")

    # webドライバー終了
    driver.quit()

    return result_html


def create_result_html(result_html, dict_user_config):
    file_path = dict_user_config["file_path_html"]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(result_html)
