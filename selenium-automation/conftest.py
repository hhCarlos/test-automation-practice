import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
  options = Options()
  options.add_argument("--window-size=1440,900")

  if os.getenv("HEADLESS", "false").lower() == "true":
      options.add_argument("--headless=new")

  driver = webdriver.Chrome(options=options)
  driver.implicitly_wait(0)

  yield driver

  driver.quit()
