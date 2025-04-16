from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    # Might be needed for WSL
    options = webdriver.ChromeOptions() 
    options.headless = True

    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    wait = WebDriverWait(driver, 15)

    # Wait until the username input is present
    username = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

    username.send_keys("Admin")
    password.send_keys("admin123")
    login_button.click()

    # driver.find_element(By.NAME, "username").send_keys("Admin")

    # driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    # driver.find_element(By.ID, "btnLogin").click()
    assert "Dashboard" in driver.page_source