from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()

driver.get("https://free-mp3-download.net") 

search_input = driver.find_element(By.ID,"q")

search_input.send_keys("Mantis John Digweed")

search_button = driver.find_element(By.ID, "snd")  

search_button.click()

wait = WebDriverWait(driver, 20)
button_xpath = "/html/body/main/div/div[2]/div/table/tbody/tr[1]/td[3]/a/button"  
wait.until(EC.presence_of_element_located((By.XPATH, button_xpath)))
button = driver.find_element(By.XPATH, button_xpath)
button.click()
wait2 = WebDriverWait(driver, 20)
close_button_xpath = "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[3]"


wait2 = WebDriverWait(driver, 10)
driver.execute_script("""
const elements = document.getElementsByClassName("google-auto-placed");
while (elements.length > 0) elements[0].remove();
                      """)

wait2 = WebDriverWait(driver, 10)
driver.execute_script("""
const elements = document.getElementsByClassName("adsbygoogle adsbygoogle-noablate");
while (elements.length > 0) elements[0].remove();
                      """)

button.click()


iframe_captcha = driver.find_element(By.XPATH,".//iframe[@title='reCAPTCHA']")
driver.switch_to.frame(iframe_captcha)
wait2 = WebDriverWait(driver, 10)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/div/span").click()
wait2 = WebDriverWait(driver, 10)
driver.switch_to.default_content()

wait2 = WebDriverWait(driver, 20)
download_button_xpath = ".//button[contains(text(),'Download')]"
wait2.until(EC.presence_of_element_located((By.XPATH, download_button_xpath)))
download_button = driver.find_element(By.XPATH, download_button_xpath)
download_button.click()

input("Press something to close: ")

# Close the browser when you're done
driver.quit()