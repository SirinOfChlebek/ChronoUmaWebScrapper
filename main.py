import gspread
from google.oauth2.service_account import Credentials
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time


driver = uc.Chrome()

url = "insert chrono url here!"
driver.get(url)
time.sleep(10)

scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_file("credentials.json", scopes = scopes)
admin = gspread.authorize(credentials)

sheet = admin.open("UmaScrapper").sheet1

rows = driver.find_elements(By.TAG_NAME, "tr")

data = []
for row in rows:
    cells = row.find_elements(By.XPATH, ".//th | .//td")
    row_data = []
    for cell in cells:
        text = cell.text.strip()
        row_data.append(text)
    if any(row_data):
        data.append(row_data)


sheet.clear()
sheet.update(values = data, range_name = "A1")
driver.quit()

