from urllib.parse import urlparse

from support.config import BASE_URL
from support.assertions.common_assertions import (
    expect_base_layout,
    expect_main_navigation,
)

PAGE_PATH = "/"

def test_should_open_home_page_and_show_base_layout(driver):
  driver.get(f"{BASE_URL}{PAGE_PATH}")

  current_path = urlparse(driver.current_url).path

  assert current_path == PAGE_PATH

  expect_base_layout(driver)
  expect_main_navigation(driver)
