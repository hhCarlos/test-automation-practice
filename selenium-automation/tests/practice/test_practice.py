from urllib.parse import urlparse

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support.config import BASE_URL

from support.assertions.common_assertions import (
    expect_base_layout,
    expect_main_navigation,
)

from support.selectors.practice_selectors import PracticeSelectors

PAGE_PATH = "/practice/"

PRACTICE_LINKS = [
    {
        "locator": PracticeSelectors.TEST_LOGIN_PAGE_LINK,
        "text": "Test Login Page",
        "path": "/practice-test-login/",
    },
    {
        "locator": PracticeSelectors.TEST_EXCEPTIONS_PAGE_LINK,
        "text": "Test Exceptions",
        "path": "/practice-test-exceptions/",
    },
    {
        "locator": PracticeSelectors.TEST_TABLE_PAGE_LINK,
        "text": "Test Table",
        "path": "/practice-test-table/",
    },
]

def get_current_path(driver):
  return urlparse(driver.current_url).path

def expect_visible(driver, locator, timeout=10):
  return WebDriverWait(driver, timeout).until(
      EC.visibility_of_element_located(locator)
  )

def expect_clickable(driver, locator, timeout=10):
  return WebDriverWait(driver, timeout).until(
      EC.element_to_be_clickable(locator)
  )

def test_should_open_practice_page_and_show_base_layout(driver):
  driver.get(f"{BASE_URL}{PAGE_PATH}")

  assert get_current_path(driver) == PAGE_PATH

  expect_base_layout(driver)
  expect_main_navigation(driver)

def test_should_show_practice_exercise_links(driver):
  driver.get(f"{BASE_URL}{PAGE_PATH}")

  post_content = expect_visible(driver, PracticeSelectors.POST_CONTENT)

  assert post_content.is_displayed()

  for link_data in PRACTICE_LINKS:
      link = expect_visible(driver, link_data["locator"])

      assert link_data["text"] in link.text
      assert link_data["path"] in link.get_attribute("href")

def test_should_navigate_to_test_login_page(driver):
  driver.get(f"{BASE_URL}{PAGE_PATH}")

  login_link = expect_clickable(
      driver,
      PracticeSelectors.TEST_LOGIN_PAGE_LINK,
  )

  assert "Test Login Page" in login_link.text

  login_link.click()

  WebDriverWait(driver, 10).until(
      lambda current_driver: get_current_path(current_driver)
      == "/practice-test-login/"
  )

  assert get_current_path(driver) == "/practice-test-login/"
