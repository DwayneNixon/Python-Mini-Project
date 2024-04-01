import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class YouTubeSearchAndPlay():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def search_and_play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com")
        search = self.driver.find_element(By.XPATH, '//*[@id="search"]')
        search.send_keys(query)
        search.send_keys(Keys.RETURN)

        #time.sleep(5)  # Wait for 5 seconds for search results to load
        # Click on the first video that appears in the search results
        #first_video = self.driver.find_element(By.XPATH, '//*[@id="contents"]/ytd-video-renderer[1]')
        #first_video.click()

        # Let the video play for some time
        time.sleep(60)  # Adjust the time as needed

        self.driver.quit()

    def play(self, video_query):
        self.search_and_play(video_query)

        

