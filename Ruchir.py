from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\ProgramData\Microsoft\Windows\Start Menu\Programs')

    def play(self_, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video= self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        video.click()

