from selenium.webdriver.common import *
from selenium.webdriver.remote.webdriver import WebElement, WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from .logger import logger


class HandleBase:
    """
    :loctor: 元素的定位及定位元素的方式，如（xpath, '//*[@id="kw"]'）
    :module: 当前页面要定位的模块名称
    :timeout:超时时间
    """
    def __init__(self, driver):
        self.driver = driver

    def is_visible(self):
        return ec.visibility_of_element_located

    def wait_element(self, loctor, module=None, timeout=20) -> WebElement:
        try:
            logger.info("正在定位%s元素出现" % (module))
            ele = WebDriverWait(driver=self.driver, timeout=timeout).until(ec.visibility_of_element_located(loctor))
            logger.info("%s元素已经成功定位" % (module))
            return ele
        except Exception as e:
            logger.info("%s元素定位失败" % (module))
            raise e

    @property
    def get_current_url(self):
        try:
            logger.info("正在获取当前页面的url")
            logger.info("获取当前页面的url成功")
            return self.driver.current_url

        except Exception as e:
            logger.info("获取当前页面url失败")
            raise e