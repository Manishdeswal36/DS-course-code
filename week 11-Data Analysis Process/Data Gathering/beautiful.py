import undetected_chromedriver as uc
import time

url = 'https://www.ambitionbox.com/list-of-companies?page=1'   # or any other URL

# 1. Open actual Chrome using undetected_chromedriver
driver = uc.Chrome()

# 2. Visit the site
driver.get(url)

# 3. Wait for the page and JavaScript to load (increase sleep if site is slow)
time.sleep(6)

# 4. Extract full HTML code
html = driver.page_source

# 5. Save HTML to a file
with open('output.html', 'w', encoding='utf-8') as file:
    file.write(html)

# 6. Optionally print first 500 characters, or all of it
print(html[:500])

# 7. Close the browser
driver.quit()
