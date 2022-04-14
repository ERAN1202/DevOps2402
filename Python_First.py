from selenium import webdriver

enter_facebook = webdriver.Chrome()
enter_facebook.get("https://www.facebook.com/")
username = enter_facebook.find_element_by_id("email")
password = enter_facebook.find_element_by_id("pass")
submit   = enter_facebook.find_element_by_id("loginbutton")
username.send_keys("mymail@gmail.com")
password.send_keys("mypassword")
submit.click()
