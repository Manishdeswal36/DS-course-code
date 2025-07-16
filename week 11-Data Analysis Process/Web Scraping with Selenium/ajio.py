from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# ✅ Setup stealth options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/114.0.5735.110 Safari/537.36")

# ✅ Use ChromeDriverManager to auto-match versions
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# ✅ Hide "navigator.webdriver" detection
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        });
    """
})

# ✅ Start browsing
driver.get("https://www.ajio.com/men-backpacks/c/830201001")
time.sleep(3)

# ✅ Scroll logic
old_height = driver.execute_script("return document.body.scrollHeight")
counter = 1
max_scrolls = 50

while counter <= max_scrolls:
    print(f"Scroll {counter}")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(1.5, 2.5))

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == old_height:
        print("✅ Reached bottom of page.")
        break
    old_height = new_height
    counter += 1

# ✅ Save HTML
html = driver.page_source
with open("ajio.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ HTML saved to ajio.html")
driver.quit()
