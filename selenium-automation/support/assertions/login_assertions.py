from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support.selectors.login_selectors import LoginSelectors

def expect_visible(driver, locator, timeout=10):
  return WebDriverWait(driver, timeout).until(
      EC.visibility_of_element_located(locator)
  )

def expect_success_login_page(driver):
  title = expect_visible(driver, LoginSelectors.SUCCESS_TITLE)
  content = expect_visible(driver, LoginSelectors.SUCCESS_CONTENT)
  logout_button = expect_visible(driver, LoginSelectors.LOGOUT_BUTTON)

  assert "Logged In Successfully" in title.text
  assert "Congratulations" in content.text
  assert "Log out" in logout_button.text

def expect_login_error(driver, expected_message):
  error_message = expect_visible(driver, LoginSelectors.ERROR_MESSAGE)

  assert expected_message in error_message.text
