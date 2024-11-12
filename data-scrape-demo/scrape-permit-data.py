from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import yaml

import logging
from pathlib import Path

class PermitScraper:
    def __init__(self, config_path='config.yml'):
        self.config = self._load_config(config_path)
        self.setup_logging()
        self.driver = None

    def _load_config(self, config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def setup_logging(self):
        logging.basicConfig(
            level=self.config['logging']['level'],
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def setup_driver(self):
        options = webdriver.ChromeOptions()
        # Add all browser arguments from config
        arguments = self.config['browser']['arguments']
        options.add_argument(arguments)
        self.driver = webdriver.Chrome(options=options)
        self.logger.info("WebDriver initialized")

    def scrape_data(self):
        try:
            self.setup_driver()
            self.driver.get(self.config['scraping']['url'])
            time.sleep(self.config['scraping']['wait_time'])

            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            table_id = self.config['scraping']['table_id']
            table = soup.find('table', {'id': table_id})

            if not table:
                raise ValueError("Table not found on page")

            column_names = [th.text.strip() for th in table.find_all('th')]
            table_data = []
            
            for tr in table.find_all('tr'):
                row_data = [td.text.strip() for td in tr.find_all('td')]
                if len(row_data) == len(column_names):
                    table_data.append(row_data)

            return pd.DataFrame(table_data, columns=column_names)

        except Exception as e:
            self.logger.error(f"Error during scraping: {str(e)}")
            raise
        finally:
            if self.driver:
                self.driver.quit()
                self.logger.info("WebDriver closed")

    def save_data(self, df, output_path=None):
        if output_path is None:
            output_path = self.config['output']['file_path']
        
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        df.to_csv(output_path, index=False)
        self.logger.info(f"Data saved to {output_path}")

def main():
    scraper = PermitScraper()
    df = scraper.scrape_data()
    scraper.save_data(df)

if __name__ == "__main__":
    main()
