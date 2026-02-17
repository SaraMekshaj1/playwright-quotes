from playwright.sync_api import sync_playwright
class BrowserManager:
    def __init__(self, headless=True, logger=None):
        self.headless = headless
        self.logger = logger

    def start(self):
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=self.headless)
            self.page = self.browser.new_page()

            if self.logger:
                self.logger.info("Browser started")

            return self.page

        except Exception as e:
            if self.logger:
                self.logger.error(f"Browser start failed: {e}")
            raise

    def close(self):
        try:
            self.browser.close()
            self.playwright.stop()

            if self.logger:
                self.logger.info("Browser closed")

        except Exception as e:
            if self.logger:
                self.logger.error(f"Error closing browser: {e}")
