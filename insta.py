from time import sleep
from tkinter import Button
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class InstagramLogin():
    def __init__(self,user, password, hashtag) -> None:
        self.hashtag = hashtag
        self.user = user
        self.password = password
        self.browser = self.open_browser("https://www.instagram.com/")
        self.login_instagram()
        # self.deny_alerts()
    
    def open_browser(self, url):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        navegador = webdriver.Chrome("chromedriver.exe", options=options)
        navegador.get(url)
        sleep(6)
        return navegador
        
    def login_instagram(self):
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.user)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        self.browser.find_elements(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')[0].click()
        sleep(10)
    
    
    def find_by_xpath(self, path):
        try:
            # element = self.browser.find_element(By.XPATH, button).click()
            element = WebDriverWait(self.browser, 3).until(EC.element_to_be_clickable((By.XPATH, path)))
            return element
        except:
            return print('error on find the element')
        
    def deny_alerts(self):
        try :
            
            save_login = self.find_by_xpath('//*[@id="mount_0_0_Zn"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/section/div/button')
            save_login.click()
        except:
            return print('deny save login error')
        # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._a9--._a9_1]'))).click()
        sleep(3)
        button = '//*[starts-with(@id, "mount_0")]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
        deny = self.find_by_xpath(button)
        sleep(5)
        deny.click()

    def go_to_hashtag(self):
        sleep(3)
        link = f"https://www.instagram.com/explore/tags/{self.hashtag}/"
        self.browser.get(link)
        sleep(3)

    def click_like(self):
        try:
            click_like = '//*[starts-with(@id, "mount_0_0_")]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button'
            like = self.find_by_xpath(click_like)
            like.click()
            
       
        except:
            click_like= '//*[starts-with(@id, "mount_0_0_")]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[3]/div/div/section[1]/span[1]/button'
            like = self.find_by_xpath(click_like)
            like.click()
            sleep(2)
            

    def first_next(self):
        first_click_next_page = '//*[starts-with(@id, "mount_0_0")]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button'
        next = self.find_by_xpath(first_click_next_page)
        next.click() 
        
    def start_like(self):
        sleep(5)
        try:
            first_image = '//*[starts-with(@id, "mount_0_0_")]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a'

            image = self.find_by_xpath(first_image)
            image.click()
            sleep(3)
        except:
            self.go_to_hashtag()
            sleep(3)
            image = self.find_by_xpath(first_image)
            image.click()
            

        loop= True
        sleep(1)
        self.click_like()
        
        self.first_next()
        self.click_like()
        while loop == True:

            click_next_page2 = '//*[starts-with(@id, "mount_0_0_")]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button'
            next2 = self.find_by_xpath(click_next_page2)
            next2.click()
            sleep(2)
            
            self.click_like()
            
            