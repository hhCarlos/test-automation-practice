from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support.selectors.login_selectors import LoginSelectors

def wait_visible(driver, locator, timeout=10):
  return WebDriverWait(driver, timeout).until(
      EC.visibility_of_element_located(locator)
  )

def wait_clickable(driver, locator, timeout=10):
  return WebDriverWait(driver, timeout).until(
      EC.element_to_be_clickable(locator)
  )

def fill_login_form(driver, username, password):
  username_input = wait_visible(driver, LoginSelectors.USERNAME_INPUT)
  password_input = wait_visible(driver, LoginSelectors.PASSWORD_INPUT)

  username_input.clear()
  username_input.send_keys(username)

  password_input.clear()
  password_input.send_keys(password)

def submit_login_form(driver):
  submit_button = wait_clickable(driver, LoginSelectors.SUBMIT_BUTTON)
  submit_button.click()

def login(driver, username, password):
  fill_login_form(driver, username, password)
  submit_login_form(driver)

def logout(driver):
  logout_button = wait_clickable(driver, LoginSelectors.LOGOUT_BUTTON)
  logout_button.click()
