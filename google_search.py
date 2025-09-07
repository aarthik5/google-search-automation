from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://duckduckgo.com/")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python programming")
search_box.send_keys(Keys.RETURN)

time.sleep(2)

results = driver.find_elements(By.XPATH, "//a[@data-testid='result-title-a']")[:5]
for idx, r in enumerate(results, start=1):
    print(f"{idx}. {r.text}\n   {r.get_attribute('href')}")

driver.quit()