from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# webブラウザを開かないように設定
# options.add_argument('--headless')
# 処理終了時webブラウザが落ちないように設定
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(
   'https://lib.kagoshima-city.jp/'
)

print(driver.page_source)

# 要素を取得する
e1 = driver.find_element(By.CLASS_NAME,'open')

# テキストボックスに値を設定する
# e_site_search_text = driver.find_element(By.CLASS_NAME,'search-text')
e_text_box = driver.find_element(By.NAME ,'text(1)')
e_text_box.send_keys("slack")
# 検索ボタンをクリックする
e_btn = driver.find_element(By.XPATH ,'//*[@id="content"]/div[3]/form/div[1]/button')
e_btn.click()

