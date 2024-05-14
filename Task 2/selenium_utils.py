from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tqdm import tqdm
import os

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

i = 1
# driver.get(f"https://live.bible.is/bible/HINDPI/MAT/{i}")
driver.get(f"https://live.bible.is/bible/hindpi/REV/4")

for i in tqdm(range(242, 261)):
    x = True
    while x:
        try:
            element = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "chapter"))
            )
            with open(f"Task 2\sources\{i}.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            x = False
            
            element = driver.find_element(By.CLASS_NAME, "next")
            element.click()
        except TimeoutException:
            continue


driver.quit()
