# import re
# import time
# import logging
# import chromedriver_autoinstaller

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

# logger = logging.getLogger(__name__)

# def is_valid_url(url):
#     regex = re.compile(
#            r"^(https?://)?(www\.)?(naukri\.com|recruit\.naukri\.com|hiring\.naukri\.com)/[a-zA-Z0-9\-._~:/?#\[\]@!$&'()*+,;=]+$"
#     )
#     return re.match(regex, str(url)) is not None

# # def setup_driver(driver_path, user_data_dir, profile_dir, headless=True):
# #     chrome_options = Options()
# #     if headless:
# #         chrome_options.add_argument("--headless")
# #     chrome_options.add_argument("--start-maximized")
# #     chrome_options.add_argument("--disable-gpu")
# #     chrome_options.add_argument("--no-sandbox")
# #     chrome_options.add_argument("--disable-dev-shm-usage")
# #     chrome_options.add_argument(f"user-data-dir={user_data_dir}")
# #     chrome_options.add_argument(f"--profile-directory={profile_dir}")
    
# #     try: 
# #         service = Service(driver_path)
# #         driver = webdriver.Chrome(service=service, options=chrome_options)
# #         return driver
# #     except Exception as e:
# #          logger.error(f"❌ Error launching ChromeDriver: {e}")
# #          raise
    
# #     return driver
# def setup_driver(driver_path=None, user_data_dir=None, profile_dir=None, headless=True):
#     chromedriver_autoinstaller.install()  # Automatically downloads the matching version

#     chrome_options = Options()
#     if headless:
#         chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")

#     driver = webdriver.Chrome(options=chrome_options)
#     return driver


# def scrape_profile(driver, url, wait_time=2):
#     try:
#         driver.get(url)
#         time.sleep(wait_time)
#         email_element = driver.find_element(By.CSS_SELECTOR, "span[title] span.thWrapper span")
#         phone_element = driver.find_element(By.CSS_SELECTOR, "p.showContactContainerPhone span")
#         return email_element.text.strip(), phone_element.text.strip()
#     except Exception:
#         return "Not Found", "Not Found"

# def scrape_demo_profile(index):
#     return f"user{index}@example.com", f"+91-99999{str(index).zfill(4)}"

import re

# Demo-safe regex URL validator
def is_valid_url(url):
    regex = re.compile(
        r"^(https?://)?(www\.)?(naukri\.com|recruit\.naukri\.com|hiring\.naukri\.com)/[a-zA-Z0-9\-._~:/?#\[\]@!$&'()*+,;=]+$"
    )
    return re.match(regex, str(url)) is not None

# Placeholder for real scraping (won't be called in Streamlit demo)
def scrape_profile(driver, url, wait_time=2):
    return "Scraping Disabled", "Scraping Disabled"

# Used in demo mode
def scrape_demo_profile(index):
    return f"user{index}@example.com", f"+91-99999{str(index).zfill(4)}"

# Prevent real WebDriver use
def setup_driver(driver_path=None, user_data_dir=None, profile_dir=None, headless=True):
    return None
