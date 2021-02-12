from selenium import webdriver
import time



try: 
    
    link1 = "https://www.avito.ru/sochi#login?authsrc=h"
    browser = webdriver.Chrome()
    browser.get(link1)
    time.sleep(5)
    login1 = browser.find_element_by_name("login")
    login1.send_keys("+7 982 991-47-45")# вписываем свой логин
    puss1 = browser.find_element_by_name("password")
    puss1.send_keys("Viranovsky4745")# вписываем свой пароль
    time.sleep(1)
    button = browser.find_element_by_name("submit")# авторизуемся
    button.click()
    time.sleep(5)
    
    browser.execute_script("window.open('https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1')")# открываем в новой вкладке страницу из-за капчи
    time.sleep(5)
    
    browser.switch_to.window(browser.window_handles[1])# переключаемся на новую вкладку
    
    thing = browser.find_element_by_xpath('//div[@data-marker="item"]/div[1]/div[2]/div[1]').click()
    time.sleep(5)# выбираем первый попавшийся товар
    
   
    browser.switch_to.window(browser.window_handles[2]) # так как открывается новая вкладка, переключаемся на неё
    
    buy = browser.find_element_by_xpath('//button[@data-marker="delivery-item-button-main"]').click()# жмём на "купить с доставкой"
    time.sleep(5)
    
    phone = browser.find_element_by_xpath('//input[@data-marker="sd/order-widget-field/phone"]')
    
    test = phone.get_attribute("value")# берём значение 
    
    assert test == "" # сравниваем значение, если сравнение прошло неудачно - выйдет ошибка "AssertionError"
    
    
    
    
finally:
    
    time.sleep(10)
    
    browser.quit()# закрываем браузер после всех манипуляций
    