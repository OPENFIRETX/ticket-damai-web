from selenium.common import TimeoutException

from userInfo import url, name

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import clickElementByClassName, clickElFromListByTag


def search(driver: webdriver):
    try:
        input_ele = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "input-search"))
        )
        input_ele.send_keys(name)  # name替换为你需要输入的内容
    except TimeoutException:
        print("搜索输入框等待超过10s")
    finally:
        print("搜索输入框结束")

    # 搜索场次
    # input_ele = driver.find_element(By.CLASS_NAME, "input-search")
    # input_ele.send_keys(name)
    clickElementByClassName("btn-search", driver)

    # 结果列表
    clickElFromListByTag("items__txt__title", "a", driver)

