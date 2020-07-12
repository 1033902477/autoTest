import pytest, time
from selenium import webdriver
from page.baidu_page import BaiDuPage


class Webobject:
    pass


@pytest.fixture(scope='class')
def init():
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(chrome_options=opts)
    driver.set_window_size(1366, 768)
    driver.implicitly_wait(30)
    driver.get('http://www.baidu.com')

    baidu = BaiDuPage(driver)
    setattr(Webobject, 'baidu', baidu)

    yield Webobject
    time.sleep(2)
    driver.quit()


