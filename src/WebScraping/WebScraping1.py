import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://rues.org.co/')
no_id_button = driver.find_element(by=By.ID, value="txtNIT")
no_id_button.send_keys("830070625")
no_id_button.send_keys(Keys.RETURN)
 
# try:
#     elements = WebDriverWait(driver, 20).until(
#         EC.presence_of_all_elements_located((By.ID, "rmTable2"))
#     )
# finally:
#     # driver.quit()
#     # for element in elements:
#     #     print(element.get_attribute('innerHTML'))
 
#     print(driver.page_source)
driver.implicitly_wait(50)
print(driver.page_source)
# results_table = driver.find_element(by=By.ID, value="rmTable2")
# print(results_table.get_attribute('innerHTML'))

input()
 
driver.close()