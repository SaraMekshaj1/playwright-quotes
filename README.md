# Playwright Quotes Scraper

## Overview
This project demonstrates a production-style web scraping pipeline using Python and Playwright to extract dynamically loaded content from a JavaScript-rendered website.

The scraper handles pagination, structured data extraction, logging, and clean output generation.

## Features
- Scrapes JavaScript-rendered pages using Playwright
- Handles pagination automatically
- Object-Oriented project structure
- Centralized configuration
- Logging system for monitoring execution
- Error handling for robustness
- CSV export for data analysis

## Project Structure
quotes_scraper/
│
├── scraper/
│ ├── browser.py
│ ├── scraper.py
│ └── utils.py
│
├── output/
├── logs/
├── main.py
├── config.py
├── requirements.txt
└── README.md


## Technologies Used
- Python
- Playwright
- Pandas

## Installation
- pip install -r requirements.txt
- playwright install


## Output
- CSV file saved in `/output`
- Logs saved in `/logs/scraper.log`

## What This Project Demonstrates
- Scraping dynamic websites
- Handling pagination
- Writing reusable, maintainable scraping code
- Production-style structure suitable for freelance work

## Future Improvements
- Async Playwright version
- Proxy rotation
- Scraping login-protected sites
- Docker containerization


