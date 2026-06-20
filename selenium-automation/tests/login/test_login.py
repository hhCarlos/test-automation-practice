from urllib.parse import urlparse

from selenium.webdriver.support.ui import WebDriverWait

from support.config import BASE_URL
from support.actions.login_actions import login, logout
from support.assertions.login_assertions import (
    expect_success_login_page,
    expect_login_error,
)

LOGIN_PATH = "/practice-test-login/"
SUCCESS_PATH = "/logged-in-successfully/"

VALID_USER = {
    "username": "student",
    "password": "Password123",
}

INVALID_USERNAME = {
    "username": "incorrectUser",
    "password": "Password123",
    "expected_error": "Your username is invalid!",
}

INVALID_PASSWORD = {
    "username": "student",
    "password": "incorrectPassword",
    "expected_error": "Your password is invalid!",
}

def get_current_path(driver):
  return urlparse(driver.current_url).path

def wait_until_path_is(driver, expected_path, timeout=10):
  WebDriverWait(driver, timeout).until(
      lambda current_driver: get_current_path(current_driver) == expected_path
  )

def test_should_login_successfully_with_valid_credentials(driver):
  driver.get(f"{BASE_URL}{LOGIN_PATH}")

  login(
      driver,
      VALID_USER["username"],
      VALID_USER["password"],
  )

  wait_until_path_is(driver, SUCCESS_PATH)

  assert get_current_path(driver) == SUCCESS_PATH

  expect_success_login_page(driver)

def test_should_show_error_when_username_is_invalid(driver):
  driver.get(f"{BASE_URL}{LOGIN_PATH}")

  login(
      driver,
      INVALID_USERNAME["username"],
      INVALID_USERNAME["password"],
  )

  assert get_current_path(driver) == LOGIN_PATH

  expect_login_error(driver, INVALID_USERNAME["expected_error"])

def test_should_show_error_when_password_is_invalid(driver):
  driver.get(f"{BASE_URL}{LOGIN_PATH}")

  login(
      driver,
      INVALID_PASSWORD["username"],
      INVALID_PASSWORD["password"],
  )

  assert get_current_path(driver) == LOGIN_PATH

  expect_login_error(driver, INVALID_PASSWORD["expected_error"])

def test_should_logout_successfully_after_login(driver):
  driver.get(f"{BASE_URL}{LOGIN_PATH}")

  login(
      driver,
      VALID_USER["username"],
      VALID_USER["password"],
  )

  wait_until_path_is(driver, SUCCESS_PATH)

  logout(driver)

  wait_until_path_is(driver, LOGIN_PATH)

  assert get_current_path(driver) == LOGIN_PATH
