import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class infow():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)
        
    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.send_keys(query)
        search.send_keys(Keys.RETURN)

        time.sleep(10)  # Wait for 10 seconds
        self.driver.quit()
        
