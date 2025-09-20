# DoorDash Store Scraper

A Python scraper to extract product data from DoorDash store pages.

## Features

- Extracts store information (name, address, hours)
- Scrapes product categories and items
- Captures product details including:
  - Name
  - Description
  - Price
  - Image URL
  - Category
  - Availability
- Saves data in JSON format
- Handles dynamic content loading
- Robust error handling

## Installation

1. Install dependencies:
```bash
pip install -e .
```

Or install manually:
```bash
pip install selenium requests beautifulsoup4 lxml webdriver-manager pillow
```

2. Make sure you have Chrome browser installed (the scraper uses ChromeDriver)

## Usage

### Basic Usage
```bash
python main.py
```

This will scrape the default store URL: `https://www.doordash.com/convenience/store/27498004/`

### Custom Store URL
```bash
python main.py "https://www.doordash.com/convenience/store/YOUR_STORE_ID/"
```

### Direct Scraper Usage
```python
from scraper import DoorDashScraper

# Initialize scraper
scraper = DoorDashScraper("https://www.doordash.com/convenience/store/27498004/")

# Run scraping
data = scraper.run()

# Access results
print(f"Store: {data['store_info']['name']}")
print(f"Products: {len(data['products'])}")
```

## Output

The scraper saves data to `output/doordash_data.json` with the following structure:

```json
{
  "store_info": {
    "name": "Store Name",
    "address": "Store Address",
    "hours": "Store Hours",
    "url": "Store URL"
  },
  "categories": {
    "Category Name": {
      "product_count": 10,
      "products": [...]
    }
  },
  "products": [
    {
      "name": "Product Name",
      "description": "Product Description",
      "price": "$9.99",
      "image_url": "https://...",
      "category": "Category Name",
      "availability": "available"
    }
  ]
}
```

## Configuration

You can modify the scraper behavior by editing `scraper.py`:

- `headless=True`: Run browser in headless mode (no GUI)
- Adjust timeouts and wait times as needed
- Modify selectors for different page layouts

## Troubleshooting

1. **ChromeDriver issues**: The scraper automatically downloads ChromeDriver, but ensure Chrome browser is installed
2. **Page loading issues**: Increase wait times in the code if pages load slowly
3. **No data extracted**: DoorDash may have changed their page structure - update selectors in the code
4. **Rate limiting**: Add delays between requests if you encounter rate limiting

## Notes

- The scraper respects DoorDash's robots.txt and terms of service
- Use responsibly and don't overload their servers
- Some data may require JavaScript execution, which is why we use Selenium
- Images are disabled during scraping for speed, but URLs are captured
