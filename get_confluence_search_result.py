import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_confluence_search_result(get_slack_message, dict_user_config):
    # seleniumを使用してconfluence検索
    result_html = selenium_confluence_search(get_slack_message,dict_user_config)
    # 検索結果のHTMLデータをファイルに書き込む
    create_result_html(result_html, dict_user_config)


def selenium_confluence_search(get_slack_message,dict_user_config):
    # webドライバーオプション
    options = webdriver.ChromeOptions()
    # webドライバーオプション（webブラウザを開かないように設定）
    options.add_argument("--headless")
    # webドライバー起動
    driver = webdriver.Remote(
        # TODO
        # サイドカーのURL
        command_executor=""
    )
    driver = webdriver.Chrome(options=options)

    # Confluenceの基本ページにアクセス
    driver.get(dict_user_config["confluence_url"])
    driver.implicitly_wait(time_to_wait=30)

    # Confluenceログイン処理
    e1 = driver.find_element(By.ID, "username")
    e1.send_keys(dict_user_config["mail_ad"])
    e2 = driver.find_element(By.ID, "login-submit")
    e2.click()
    driver.implicitly_wait(time_to_wait=30)
    e3 = driver.find_element(By.ID, "password")
    e3.send_keys(dict_user_config["password"])
    e4 = driver.find_element(By.ID, "login-submit")
    e4.click()
    driver.implicitly_wait(time_to_wait=30)
    
    # ２段階認証の有効化を問われた場合は設定しないを選択
    if len(driver.find_elements(By.ID,"mfa-promote-dismiss")) > 0 :
        e5 = driver.find_element(By.ID, 'mfa-promote-dismiss')
        e5.click()
        driver.implicitly_wait(time_to_wait=30)

    # 検索処理
    e6 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/header/div/div[2]/div/div/div/div/div[1]/div/input",
    )
    e6.send_keys(get_slack_message)
    e6.send_keys(Keys.ENTER)
    time.sleep(3)
    # TODO debug時コメントアウトstart
    # e10 = driver.find_element(
    #     By.XPATH,
    #     "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/main/div/div[1]/div/main/div[2]/div/form/div/div/div/div/div[2]/div[2]/button",
    # )
    # e10.click()
    # time.sleep(20)

    # # 検索結果をHTMLファイルに出力
    # result = driver.find_element(
    #     By.XPATH, '//*[@id="content-body"]/main/div[2]/div/div[2]/div[1]'
    # )
    # result_html = result.get_attribute(name="innerHTML")
    # TODO debug時コメントアウトend

    # TODO release時削除start
    result = driver.find_element(
        By.XPATH, '//*[@id="content-body"]/main/div[2]/div/div[3]/div/ul/li[1]/div/div[1]/div[2]'
    )
    result_html = result.get_attribute(name="innerHTML")
    # TODO release時削除end

    # webドライバー終了
    driver.quit()

    return result_html


def create_result_html(result_html, dict_user_config):
    file_path = dict_user_config["file_path_html"]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(result_html)

