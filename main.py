from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request

import time
from tqdm import tqdm


options = Options()
options.add_experimental_option("detach", True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 불필요한 메시지 제거

driver = webdriver.Chrome(ChromeDriverManager(path='DRIVER').install(), options=options)
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("python")    # search word
elem.submit()

SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:   # Repeat until break
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')
count = 1
for image in tqdm(images):
    try:
        image.click()   # To get more quality images
        time.sleep(1)
        imgUrl = driver.find_element_by_css_selector('img.n3VNCb').get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count)+".jpg")
        count = count + 1
    except:
        pass

driver.close()