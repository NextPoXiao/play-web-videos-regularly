from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import json
import time
import os

#使用chrome浏览器
def chrome(url, json_data):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    open_broswer(url, browser, json_data)

#使用Edge浏览器
def edge(url, json_data):
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option("detach", True)
    browser = webdriver.Edge(options=options)
    open_broswer(url, browser, json_data)

#浏览器的操作
def open_broswer(url, browser,json_data):
    browser.maximize_window()
    browser.get(url)
    wait = WebDriverWait(browser, 10)
    button0 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, json_data['opentv_video_class_name'])))
    button0.click()
    time.sleep(1)
    button1 = browser.find_element(By.XPATH, json_data['opentv_Play_xpath'])
    button1.click()
    time.sleep(1)
    button2 = browser.find_element(By.XPATH, json_data['opentv_maximize_xpath'])
    button2.click()

#检查是否开启
def on_or_off():
    #读取json文件
    with open("set_up.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
    use_browse = json_data['use_browse']
    url = json_data['opentv_url']
    if json_data['run_now'] == "yes":
        #使用的浏览器
        if use_browse == "chrome":
            chrome(url, json_data)
        else:
            edge(url, json_data)
    #如果今天是工作日，并且今天开启了，就等待开启时间
    elif json_data['today_opentv'] == "yes" and datetime.date.today().weekday() <= 4:
        wait_time(json_data)
    elif json_data['week_opentv'] == "yes":
        wait_time(json_data)

#等待开启时间
def wait_time(json_data):
    url = json_data['opentv_url']
    opentv_time = json_data['opentv_time']
    set_time = opentv_time.split(":")
    #计算现在与每天20：45的差多少秒
    now = datetime.datetime.now()
    hour = int(set_time[0])
    minute = int(set_time[1])
    seconds = int(set_time[2])
    #总共剩下多少秒
    diff_seconds = (hour - now.hour) * 3600 + (minute - now.minute) * 60 + (seconds - now.second)
    #print(diff_seconds)
    if diff_seconds > 0:
        time.sleep(diff_seconds)
        use_browse = json_data['use_browse']
        # 使用的浏览器
        if use_browse == "chrome":
            chrome(url, json_data)
        elif use_browse == "edge":
            edge(url, json_data)
    elif -900 <= diff_seconds <= 0:
        use_browse = json_data['use_browse']
        # 使用的浏览器
        if use_browse == "chrome":
            chrome(url, json_data)
        elif use_browse == "edge":
            edge(url, json_data)

if __name__ == '__main__':
    #如果没有文件，就新建并写入
    json_file_path = "set_up.json"
    if not os.path.exists(json_file_path):
        with open(json_file_path,'w') as  f:
            json.dump({"today_opentv": "yes",
                       "opentv_time": "20:45:00",
                       "week_opentv": "no",
                       "run_now": "no",
                       "use_browse": "chrome",
                       "opentv_url": "http://10.23.26.242/#/videos/",
                       "opentv_video_class_name": "video-phone",
                       "opentv_Play_xpath": "//*[@id=\"OnlinePlayer\"]/div[4]/div[3]/button",
                       "opentv_maximize_xpath": "//*[@id=\"OnlinePlayer\"]/div[4]/div[4]/div[6]"}
                   ,f)
        on_or_off()
    else:
        on_or_off()