from core.browser import BrowserManager
from scraper.scraper import QuotesScraper
from utils.logger import setup_logger
from utils.file_handler import save_to_csv
import config

def main():
    logger = setup_logger()
    logger.info("Starting scraping job")

    browser_manager = None

    try:
        browser_manager = BrowserManager(
            headless=config.HEADLESS,
            logger=logger
        )
        page = browser_manager.start()

        scraper = QuotesScraper(
            page,
            config.WAIT_TIME_MS,
            logger
        )
        data = scraper.scrape(config.BASE_URL)

        save_to_csv(data, config.OUTPUT_FILE, logger)

        logger.info(f"Finished scraping {len(data)} quotes")

    except Exception as e:
        logger.critical(f"Fatal error: {e}")

    finally:
        if browser_manager:
            browser_manager.close()

if __name__ == "__main__":
    main()
