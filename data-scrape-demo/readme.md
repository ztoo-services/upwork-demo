# Web Scraping Tool for Permit Data

A configurable web scraping tool built with Python to extract permit data from websites.

## Setup and Installation

### 1. Create Virtual Environment
```bash
# Create a new conda environment
conda create -n scraper-env python=3.11

# Activate the environment
conda activate scraper-env
```
### 2. Install Requirements

```bash
pip install -r requirements.txt
```
### 3. Configuration 

Customize the following parameters:
 - url: Target website URL
 - table_id: HTML ID of the table to scrape
 - wait_time: Time to wait for page load (in seconds)
 - file_path: Output file location

### 4. Running the Script 

```bash
# change to app dir 
cd app
# Run the script
python scrape_permit_data.py
```

### Sample Logs 
```bash 
(py311) rajtilak@MacBook-Pro app % python scrape-permit-data.py 
2024-11-12 11:21:38,574 - __main__ - INFO - WebDriver initialized
2024-11-12 11:21:56,663 - __main__ - INFO - WebDriver closed
2024-11-12 11:21:56,665 - __main__ - INFO - Data saved to permits-concord.csv
(py311) rajtilak@MacBook-Pro app % 
```