import logging
from pathlib import Path

def setup_logger():
    Path("output").mkdir(exist_ok=True)

    logging.basicConfig(
        filename="output/scraper.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger("scraper")
