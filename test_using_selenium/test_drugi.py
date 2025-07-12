from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_bing_search_success():

    driver = webdriver.Chrome()
    driver.get("https://www.bing.com/") 
    #znajdz element z id = "sb_form_q"
    search = driver.find_element(By.ID, "sb_form_q")
    sleep(2)
    search.click()
    search.send_keys("selenium")
    search.send_keys(Keys.ENTER)
    sleep(3)
    results = driver.find_element(By.CLASS_NAME, "sb_count") #regex generator
    print(results.text) #nie mam "text" w zwracanym ciale/ poszukac
    print(type(results.text))
    print(results.text.startswith("About"))
    assert results.text.startswith("About")
    sleep(2)
    driver.quit()

