from selenium import webdriver
from time import sleep
from secrets import username, password

class Tinderbot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://tinder.com/')
        sleep(2)
    
    def login(self):
        loginBtn = self.driver.find_element_by_xpath('//button[span[text()="Log in"]]')
        loginBtn.click()
        sleep(2)

        try: 
            facebookLoginBtn = self.driver.find_element_by_xpath('//button[span[text()="Log in with Facebook"]]')
            facebookLoginBtn.click()
            sleep(1)
        except Exception:
            showMoreBtn = self.driver.find_element_by_xpath('//button[text()="More Options"]')
            showMoreBtn.click()
            sleep(1)

            facebookLoginBtn = self.driver.find_element_by_xpath('//button[span[text()="Log in with Facebook"]]')
            facebookLoginBtn.click()
            sleep(1)
        
        #Save main_windows, to switch to facebook login windows
        main_windows = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        sleep(1)

        self.driver.find_element_by_id('email').send_keys(username)
        self.driver.find_element_by_id('pass').send_keys(password)

        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        sleep(2)

        self.driver.switch_to_window(main_windows)
        sleep(0.5)



tinderBot = Tinderbot()
tinderBot.login()

        