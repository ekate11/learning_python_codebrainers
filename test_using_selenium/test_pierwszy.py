from selenium import webdriver
from time import sleep

def get_website_title(url):
    driver = webdriver.Chrome()
    driver.get(url)
    title = driver.title
    driver.quit()
    return title

def test_chrome1_title():
    title = get_website_title("https://onet.pl/")
    assert title == "Onet – Jesteś na bieżąco"

def test_chrome2_title():
    driver = webdriver.Chrome()  #otwieramy driver przegladarki .opera, .safari
    driver.get("https://onet.pl/")
    assert driver.title == "Onet – Jesteś na bieżąco"
    site_title = driver.title
    driver.quit()
    

#driver.get("https://onet.pl/")
#sleep(5)
#site_title = driver.title
#print(site_title)
#assert site_title == "Onet – Jesteś na bieżąco"
#sleep(2) # Czekaj 5 sekund

def test_chrome_krakow_title():
    driver = webdriver.Chrome()  
    driver.get("https://krakow.naszemiasto.pl/")
    assert driver.title == "Kraków Nasze Miasto - Wiadomości, informacje i wydarzenia"
    driver.quit()

