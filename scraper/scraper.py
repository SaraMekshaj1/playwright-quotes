from typing import List, Dict
from playwright.sync_api import Page
from utils.retry import retry
class QuotesScraper:
    def __init__(self, page: Page, wait_time: int, logger):
        self.page = page
        self.wait_time = wait_time
        self.logger = logger

    def scrape(self, url: str) -> List[Dict]:
        data = []

        try:
            self.logger.info(f"Opening URL: {url}")
            retry(lambda: self.page.goto(url), logger=self.logger)

            while True:
                self.page.wait_for_selector("div.quote", timeout=5000)
                quotes = self.page.query_selector_all("div.quote")

                self.logger.info(f"Found {len(quotes)} quotes on page {self.page.url}")

                for q in quotes:
                    try:
                        data.append({
                            "text": q.query_selector("span.text").inner_text(),
                            "author": q.query_selector("small.author").inner_text()
                        })
                    except Exception as e:
                        self.logger.warning(f"Skipping one quote due to error: {e}")

                next_btn = self.page.query_selector("li.next a")
                if not next_btn:
                    self.logger.info("No more pages found")
                    break

                next_btn.click()

                # Wait for next page content (better than fixed timeout)
                self.page.wait_for_selector("div.quote", timeout=5000)

        except Exception as e:
            self.logger.error(f"Scraping failed: {e}")
            raise

        return data
