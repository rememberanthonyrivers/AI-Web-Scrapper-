import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Launching chrome browser...")
    
    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try: 
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)
        print("\n *** Data has been scraped. ***\n")
        return html
        
    
    finally:
        driver.quit()