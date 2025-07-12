from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_bing_search_link_into_selenium():
    """
    GIVEN https://www.selenium.dev/ is opened
    AND Documentation link is found
    WHEN link is clicked
    THEN selenium.dev/documentation website is loaded

    wskazówka: By.LINK_TEXT, "Documentation"
    """
    driver = webdriver.Chrome()
    driver.maximize_window() #lub set_window_size
    driver.get("https://www.selenium.dev/") 
    documentation_link = driver.find_element(By.LINK_TEXT, "Documentation")
    documentation_link.click()
    sleep(3)
    print(driver.title)
    driver.quit()
