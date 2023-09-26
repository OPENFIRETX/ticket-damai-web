from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from time import sleep

# 找到元素点击
from selenium.webdriver.support.wait import WebDriverWait


def clickElementByClassName(className, driver):
    try:
        input_el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, className))
        )
    except TimeoutException:
        print("获取要点击的超过10s", className)
    finally:
        print("获取要点击的结束")

    # input_el = driver.find_element(By.CLASS_NAME, className)
    input_el.click()


# 从列表中找到要点击的元素
def clickElFromListByTag(listClassName, tag, driver):
    try:
        show_list = WebDriverWait(driver, 3).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, listClassName))
        )
    except TimeoutException:
        print("获取所有场次列表超过10s")
    finally:
        print("获取所有场次列表结束")

    try:
        my_show_element = WebDriverWait(show_list[0], 5).until(
            EC.presence_of_element_located((By.TAG_NAME, tag))
        )
    except TimeoutException:
        print("获取第一个场次列表超过10s")
    finally:
        print("获取第一个场次列表结束")

    my_show_element.click()
    # show_list = driver.find_elements(By.CLASS_NAME, listClassName)
    # my_show_element = show_list[0].find_element(By.TAG_NAME, tag)
    # sleep(1)

# def wait
