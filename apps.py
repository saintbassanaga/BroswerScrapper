import datetime
import random
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver


def initiate_browser():
    proxyscrape = {
        "proxy": {

            "http": "http://oe4fhoeqvk:p0h3941tq1@resi.proxyscrape.com:8000/",
            "https": "https://oe4fhoeqvk:p0h3941tq1@resi.proxyscrape.com:8000/",
            'no_proxy': 'localhost,127.0.0.1'  # excludes

        },
    }

    option = Options()
    #option.add_argument("--headless")
    # option.add_argument("--user-agent={}".format(random.choice(user_agent_list)))
    option.add_argument("--start-maximized")
    option.add_argument("--ignore-certificate-errors")
    option.add_argument('--allow-insecure-localhost')
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--no-sandbox")
    # option.add_argument("--disable-setuid-sandbox")
    option.add_argument("--disable-gpu")
    # option.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(seleniumwire_options=proxyscrape, options=option)
    browser.delete_all_cookies()
    return browser


def TheMyst():
    driver = initiate_browser()
    try:

        List = ['The Myst', 'The Myst Condo']

        driver.get("https://www.google.com")
        time.sleep(10)
        try:
            driver.find_element(By.CSS_SELECTOR, "#L2AGLb > div").click()
        except:
            pass
        a = 0
        time.sleep(1)

        keyword = random.choice(List)
        driver.find_element(By.CSS_SELECTOR, ".gLFyf").send_keys(keyword)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".gLFyf").send_keys(Keys.ENTER)
        time.sleep(1)

        while a < 8:
            try:
                driver.find_element(By.PARTIAL_LINK_TEXT, "https://www.the-myst.com").click()
                print(datetime.datetime.now().strftime("%H:%M:%S"), keyword)
                time.sleep(5)
                break
            except:
                # driver.find_element(By.CSS_SELECTOR,"#pnnext > span:nth-child(2)").click()
                time.sleep(10)
            a = a + 1
        if a == 8:
            print(datetime.datetime.now().strftime("%H:%M:%S"), "Cannot find Website: ", keyword)

        time.sleep(2)

        driver.close()
        time.sleep(10)

    except:
        print('-------------------------------- Error in Search')
        driver.quit()


i = 0
while i < 10:
    TheMyst()
    time.sleep(6)
    i = i + 1