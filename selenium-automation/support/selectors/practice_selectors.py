from selenium.webdriver.common.by import By


class PracticeSelectors:
  POST_CONTENT = (By.CSS_SELECTOR, "#main-container .post-content")

  TEST_LOGIN_PAGE_LINK = (
      By.CSS_SELECTOR,
      'a[href*="/practice-test-login/"]',
  )

  TEST_EXCEPTIONS_PAGE_LINK = (
      By.CSS_SELECTOR,
      'a[href*="/practice-test-exceptions/"]',
  )

  TEST_TABLE_PAGE_LINK = (
      By.CSS_SELECTOR,
      'a[href*="/practice-test-table/"]',
  )
