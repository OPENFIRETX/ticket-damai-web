from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By


from selenium.webdriver.support.wait import WebDriverWait

from userInfo import date
from utils import clickElementByClassName


def buy(driver: webdriver):
    # 点击日期进入选择场次

    clickDate(driver)

    # 选择场次

    clickTime(driver)

    # 选择票价

    clickPrice(driver)

    # 选择数量

    clickNum(driver)

    # 点击马上购买
    clickBuy(driver)


def clickDate(driver):
    def handleFn(t, i, s_i):
        if t.isdigit():
            if "29" == t:
                print("找到了 ", t)
                return i
            else:
                return s_i
        else:
            return s_i

    # 最外层list
    show_index = -1

    try:
        outer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "month"))
        )
    except TimeoutException:
        print("获取月份超过10s")
    finally:
        print("获取月份结束")

    # outer = driver.find_element(By.CLASS_NAME, "month")
    show_list = outer.find_elements(By.CSS_SELECTOR, ".wh_content_item:not(.disabled)")
    # print("外层list")
    # print(show_list)
    for (index, show) in enumerate(show_list):
        # print(show.text)
        # 文字的元素列表
        texts = show.find_element(By.CLASS_NAME, "wh_item_date")
        texts_list = texts.text.split("\n")  # 获取日期时 div里所有文字
        for (j, text) in enumerate(texts_list):
            # 自定义判断
            show_index = handleFn(text, index, show_index)

    # 判断搜到没有
    if show_index == -1:
        print("没有日期!!!!!!!!!!!!!!!!")
        return
    else:
        print("有日期!!!!!!!!!!!!!!!!!")

    # 点击找到的日期
    show_list[show_index].click()


def clickTime(driver):
    def handleFn(t, i, si):
        if "16:30" in t:
            return i
        else:
            return si

    # 最外层list
    show_list = driver.find_elements(By.CSS_SELECTOR, ".select_right_list_item:not(.sku_item)")
    show_index = -1
    print("外层list")
    print(show_list)
    for (index, show) in enumerate(show_list):
        # 文字的元素列表
        texts = show.find_element(By.TAG_NAME, "span")
        texts_list = texts.text.split("\n")  # 获取日期时 div里所有文字
        for (j, text) in enumerate(texts_list):
            # 自定义判断
            show_index = handleFn(text, index, show_index)

    # 判断搜到没有
    if show_index == -1:
        print("没有时间段!!!!!!!!!!!!!!!!")
        return
    else:
        print("有时间段!!!!!!!!!!!!!!!!!")


    # 点击找到的时间
    print(show_list[show_index].text)
    show_list[show_index].click()



def clickPrice(driver):
    def handleFn(t, i, si):
        # print(t)
        if "99元" in t:
            return i
        else:
            return si

    # 最外层list
    show_list = driver.find_elements(By.CLASS_NAME, "sku_item")
    show_index = -1
    print("外层list")
    print(show_list)
    for (index, show) in enumerate(show_list):
        # 文字的元素列表
        texts = show.find_element(By.CLASS_NAME, "skuname")
        texts_list = texts.text.split("\n")  # 获取日期时 div里所有文字
        for (j, text) in enumerate(texts_list):
            # 自定义判断
            show_index = handleFn(text, index, show_index)

    # 判断搜到没有
    if show_index == -1:
        print("没有票价!!!!!!!!!!!!!!!!")
        return
    else:
        print("有票价!!!!!!!!!!!!!!!!!")


    # 点击找到的日期
    # 点击找到的日期
    print(show_list[show_index].text)
    show_list[show_index].click()


def clickNum(driver):
    clickElementByClassName("cafe-c-input-number-handler-up", driver)


def clickBuy(driver):
    clickElementByClassName("buy-link", driver)
