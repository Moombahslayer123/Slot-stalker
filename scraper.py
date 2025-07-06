from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def get_betway_slots():
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in background
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Start driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Change this to the Betway slots page you want
        url = "https://www.betway.co.za/casino/slots"
        driver.get(url)

        time.sleep(5)  # Let page load — can be tweaked

        # You’ll need to inspect the Betway slot page to find the correct class
        # The following is a generic example and might need to be changed based on actual HTML
        slot_elements = driver.find_elements(By.CLASS_NAME, "casino-game-card__title")

        slot_names = [slot.text for slot in slot_elements if slot.text.strip() != ""]
        return slot_names

    except Exception as e:
        print(f"Scraping failed: {e}")
        return []

    finally:
        driver.quit()