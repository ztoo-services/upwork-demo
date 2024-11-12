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
# Run the script
python scrape_permit_data.py
```