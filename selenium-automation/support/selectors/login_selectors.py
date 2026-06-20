from selenium.webdriver.common.by import By


class LoginSelectors:
  USERNAME_INPUT = (By.ID, "username")
  PASSWORD_INPUT = (By.ID, "password")
  SUBMIT_BUTTON = (By.ID, "submit")
  ERROR_MESSAGE = (By.ID, "error")

  SUCCESS_TITLE = (By.CSS_SELECTOR, "#loop-container h1")
  SUCCESS_CONTENT = (By.CSS_SELECTOR, "#loop-container .post-content")
  LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a[href*="/practice-test-login/"]')
