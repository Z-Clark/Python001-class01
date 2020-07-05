# 模拟浏览器行为，点击、填写表单
from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html

    browser.get('https://shimo.im')  # 目标网站
    time.sleep(1)

    # 模拟点击登录
    # browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    browser.find_element_by_xpath(
        '//button[contains(@class,"login-button")]').click()

    # 输入用户名和密码
    browser.find_element_by_xpath(
        '//input[contains(@name, "mobileOrEmail")]').send_keys('764284142@qq.com')
    browser.find_element_by_xpath(
        '//input[contains(@name, "password")]').send_keys('a123456')
    time.sleep(1)
    browser.find_element_by_xpath(
        '//button[contains(@class, "sm-button submit")]').click()

    cookies = browser.get_cookies()  # 获取cookies
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()
