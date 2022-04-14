#Targil 1 + 2 :

from selenium import webdriver
from time import sleep
def browser_search():
    pick_browser = input("Choose browser to search website: ")
    if pick_browser == "Chrome":
        my_driver = webdriver.Chrome()
        get_website = my_driver.get("http://www.walla.co.il")
        currentURL = my_driver.current_url
        print(currentURL)
        web_title = my_driver.title
        print(web_title)
        sleep(3)
        my_driver.refresh()
        web_name = my_driver.current_url
        print(web_name)
        if currentURL == web_name:
            print("website name is equal to variable in clause 1")
        else:
            print("website name is different from variable in clause 1")
    elif pick_browser == "Firefox":
        my_driver_2 = webdriver.Firefox(executable_path="C:/Program Files/Mozilla Firefox/firefox.exe")
        my_driver_2.get("http://www.walla.co.il")


browser_search()

#Targilt 4

from selenium import webdriver


translate_google = webdriver.Chrome()
translate_google.get("https://translate.google.co.il")
translate_google.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys("אריה")


#Targil 5

from selenium import webdriver

enter_youtube = webdriver.Chrome()
enter_youtube.get("https://www.youtube.com")
search_box = enter_youtube.find_element_by_xpath("//*[@id='search']")
search_box.send_keys('moon')
SearchButton = enter_youtube.find_element_by_xpath("//*[@id='search-icon-legacy']/yt-icon")
SearchButton.click()

#Targil 6?
from selenium import webdriver

enter_google_translate = webdriver.Chrome()
enter_google_translate.get("https://translate.google.com/")
locator_1 = enter_google_translate.find_element_by_id("gt-submit")
locator_2 = enter_google_translate.find_element_by_class_name("jfk-button")
locator_3 = enter_google_translate.find_element_by_xpath("//input[@type=‘submit']")
print(locator_3)
#I try to print all that elements and I got error!!!

#Targil 7

from selenium import webdriver

enter_facebook = webdriver.Chrome()
enter_facebook.get("https://www.facebook.com/")
username = enter_facebook.find_element_by_id("email")
password = enter_facebook.find_element_by_id("pass")
submit   = enter_facebook.find_element_by_id("loginbutton")
username.send_keys("mymail@gmail.com")
password.send_keys("mypassword")
submit.click()
