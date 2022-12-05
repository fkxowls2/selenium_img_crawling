from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request

import time
from tqdm import tqdm


class CrawlingManager():
    def __init__(self):
        self.driver_setting()
    
    def driver_setting(self):
        try:
            options = Options()
            options.add_experimental_option("detach", True)  # 브라우저 바로 닫힘 방지
            options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 불필요한 메시지 제거
            driver = webdriver.Chrome(ChromeDriverManager(path='DRIVER').install(), options=options)
            self.driver = driver
        except:
            print('Chrome이 설치되어 있는지 확인해주세요.')
    
    def img_crawling(self, keyword='python', save_path='.'):
        self.driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys(keyword)    # search word
        elem.submit()

        SCROLL_PAUSE_TIME = 2
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:   # Repeat until break
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    self.driver.find_element_by_css_selector(".mye4qd").click()
                except:
                    break
            last_height = new_height

        images = self.driver.find_elements_by_css_selector('.rg_i.Q4LuWd')
        
        time.sleep(2)
        idx = 1
        for image in tqdm(images):
            try:
                image.click()   # To get more quality images
                time.sleep(1)
                imgUrl = self.driver.find_element_by_css_selector('.n3VNCb.KAlRDb').get_attribute("src")
                urllib.request.urlretrieve(imgUrl, f'{save_path}/{str(idx)}.jpg')
                idx += 1
            except:
                pass

        self.driver.close()


def main():
    # dir_path = '.'
    cm = CrawlingManager()
    cm.img_crawling(keyword='dog')



if __name__ == "__main__" :
    main()