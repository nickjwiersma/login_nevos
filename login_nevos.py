from selenium import webdriver

## Selenium 4 Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

## Selenium 4 Firefox
#from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager

## Selenium 4 MS Edge
#from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## Set variable for opening Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

## Set variable for opening Firefox
#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

## Set variable for opening Edge
#driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

## Set variables for username and password:
un = "your_login_credentials"
pw = "your_password"

# set waiting times for elements to load before proceeding
wait = WebDriverWait(driver, 10)
 
# Go to webpage
driver.get("https://helpdesk.evolutiongaming.com/nevos/oktaLogin?r=/")

# Type username "***" into Username field
wait.until(EC.presence_of_element_located((By.ID, "input43")))
username_locator = driver.find_element(By.ID, "input43")
username_locator.send_keys(un)

# Push next button
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-primary")))
next_button_locator = driver.find_element(By.CLASS_NAME, "button-primary")
next_button_locator.click()

# Push Password button
wait.until(EC.presence_of_element_located((By.XPATH, "/html//main[@id='okta-sign-in']/div[@class='auth-content']/div[@class='auth-content-inner']//form[@action='/oauth2/v1/authorize']//div[@class='list-content']/div[2]/div[@class='authenticator-description']/div[@class='authenticator-button']/a[@href='#']")))
submit_button_locator = driver.find_element(By.XPATH, "/html//main[@id='okta-sign-in']/div[@class='auth-content']/div[@class='auth-content-inner']//form[@action='/oauth2/v1/authorize']//div[@class='list-content']/div[2]/div[@class='authenticator-description']/div[@class='authenticator-button']/a[@href='#']")
submit_button_locator.click()

# Type password "***" into Password field
wait.until(EC.presence_of_element_located((By.NAME, "credentials.passcode")))
password_locator = driver.find_element(By.NAME, "credentials.passcode")
password_locator.send_keys(pw)

# Push verify button
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-primary")))
next_button_locator = driver.find_element(By.CLASS_NAME, "button-primary")
next_button_locator.click()


# Navigate to calendar
wait.until(EC.presence_of_element_located((By.ID, "my-calendar-link")))
verify_button_locator = driver.find_element(By.ID, "my-calendar-link")
verify_button_locator.click()
