from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_bing_search_link_into_selenium():
    """ GIVEN "selenium alamakota" is typed into search on site bing.com
    AND "ENTER" is pressed (search request)
    AND "selenium.dev" hyperlink is foiund
    WHEN link is clicked
    THEN Rselenium.dev is loaded
    """

    driver = webdriver.Chrome()
    driver.get("https://www.bing.com/") 
    #znajdz element z id = "sb_form_q"
    search = driver.find_element(By.ID, "sb_form_q")
    sleep(2)
    search.click()
    search.send_keys("selenium")
    search.send_keys(Keys.ENTER)
    sleep(3)
    selenium_link = driver.find_element(By.PARTIAL_LINK_TEXT, "selenium.dev")
    selenium_link.click()
    sleep(3)
    print(driver.title)
    driver.quit()