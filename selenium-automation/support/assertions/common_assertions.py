from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support.selectors.common_selectors import CommonSelectors

def expect_visible(driver, locator, timeout=10):
  return WebDriverWait(driver, timeout).until(
      EC.visibility_of_element_located(locator)
  )

def expect_exists(driver, locator, timeout=10):
  return WebDriverWait(driver, timeout).until(
      EC.presence_of_element_located(locator)
  )

def expect_base_layout(driver):
  expect_visible(driver, CommonSelectors.HEADER)
  expect_visible(driver, CommonSelectors.MAIN)

  # Footer exists, but in this site it can have 0px height.
  expect_exists(driver, CommonSelectors.FOOTER)

def expect_main_navigation(driver):
  expect_visible(driver, CommonSelectors.NAV_CONTAINER)
  expect_visible(driver, CommonSelectors.NAV_LIST)

  links = driver.find_elements(*CommonSelectors.NAV_LINKS)

  assert len(links) > 0
