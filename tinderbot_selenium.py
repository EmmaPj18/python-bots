from selenium import webdriver
from time import sleep
from secrets import username, password

class Tinderbot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        print('Welcome to the Tinder Bot made by EmmaPj18')
        self.driver.get('https://tinder.com/')
        sleep(3)

    def login(self):
        print('Log in to Tinder using Facebook credentials.')
        #Open login dialog
        try:
            login_btn = self.driver.find_element_by_xpath('//button[span[text()="Log in"]]')
            login_btn.click()
            sleep(1)
        except Exception:
            # If facebook button is present, click it. If not, click show More and then click facebook login button.
            try: 
                self.driver.find_element_by_xpath('//button[span[text()="Log in with Facebook"]]').click()
                sleep(1)
            except Exception:
                self.driver.find_element_by_xpath('//button[text()="More Options"]').click()
                sleep(1)

                self.driver.find_element_by_xpath('//button[span[text()="Log in with Facebook"]]').click()
                sleep(1)        
        
        #Save main_windows, to switch to facebook login windows
        main_windows = self.driver.window_handles[0]

        #Login to facebook
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_id('email').send_keys(username)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        sleep(4)

        #return to main windows
        self.driver.switch_to.window(main_windows)
        sleep(1)

        #click on all pop ups
        self.driver.find_element_by_xpath('//button[span[text()="I Accept"]]').click()
        self.driver.find_element_by_xpath('//button[span[text()="Allow"]]').click()
        self.driver.find_element_by_xpath('//button[span[text()="Enable"]]').click()

        print('Login success')

    def auto_swipe(self):
        like_btn = self.driver.find_element_by_xpath('//button[@aria-label="Like"]')
        auto_wipe_enable = like_btn.is_enabled()
        
        if auto_wipe_enable:
            print('Starting auto swipe')

        while auto_wipe_enable:
            try:
                self._like()
            except Exception:
                try:
                    self.driver.find_element_by_xpath('//button[span[text()="Not interested"]]').click()
                except Exception:
                    pass
            finally:
                auto_wipe_enable = like_btn.is_enabled()

        print('Finishing auto swipe')

    def _like(self):
        self.driver.find_element_by_xpath('//button[@aria-label="Like"]').click()
        sleep(0.8)

    def _dislike(self):
        self.driver.find_element_by_xpath('//button[@aria-label="Nope"]').click()
        sleep(0.5)


if __name__ == "__main__":
    tinderBot = Tinderbot()
    tinderBot.login()
    tinderBot.auto_swipe()

        