from selenium import webdriver

class Music:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs')

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        video.click()

