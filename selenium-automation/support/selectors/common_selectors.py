from selenium.webdriver.common.by import By


class CommonSelectors:
  HEADER = (By.CSS_SELECTOR, "#site-header")
  MAIN = (By.CSS_SELECTOR, "#main-container")
  FOOTER = (By.CSS_SELECTOR, "#site-footer")

  NAV_CONTAINER = (By.CSS_SELECTOR, "#menu-primary")
  NAV_LIST = (By.CSS_SELECTOR, "#menu-primary-items")
  NAV_LINKS = (By.CSS_SELECTOR, "#menu-primary-items a")

  HOME_LINK = (By.CSS_SELECTOR, "#menu-item-43 > a")
  PRACTICE_LINK = (By.CSS_SELECTOR, "#menu-item-20 > a")
  COURSES_LINK = (By.CSS_SELECTOR, "#menu-item-21 > a")
  BLOG_LINK = (By.CSS_SELECTOR, "#menu-item-19 > a")
  CONTACT_LINK = (By.CSS_SELECTOR, "#menu-item-18 > a")
