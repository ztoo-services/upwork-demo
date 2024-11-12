from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

# Set up the driver
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

# Load the page
url = "https://permiteyes.us/concord/publicview.php"
driver.get(url)

# Extract the data
time.sleep(10)

# Parse HTML and find the table
soup = BeautifulSoup(driver.page_source, "html.parser")
table = soup.find('table', {'id': 'BuildingPublicHome'}) # Find the table  

# Extract the data
column_names = [th.text.strip() for th in table.find_all('th')]
table_data = []
for tr in table.find_all('tr'):
    row_data = [td.text.strip() for td in tr.find_all('td')]
    if len(row_data) == len(column_names):
        table_data.append(row_data)

# Save the data
df = pd.DataFrame(table_data, columns=column_names)
df.to_csv("permits.csv", index=False)

# Close the driver
driver.quit()
