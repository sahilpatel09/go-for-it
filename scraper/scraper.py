#!/usr/bin/env python3
"""
DoorDash Store Scraper
Scrapes product data from a specific DoorDash store URL
"""

import json
import time
import os
import requests
from typing import Dict, List, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re


class DoorDashScraper:
    def __init__(self, store_url: str, headless: bool = True):
        """
        Initialize the DoorDash scraper
        
        Args:
            store_url: The DoorDash store URL to scrape
            headless: Whether to run browser in headless mode
        """
        self.store_url = store_url
        self.headless = headless
        self.driver = None
        self.scraped_data = {
            "store_info": {},
            "categories": {},
            "products": []
        }
        
    def setup_driver(self):
        """Setup Chrome WebDriver with appropriate options to bypass Cloudflare"""
        chrome_options = Options()
        
        # Don't run headless to avoid detection
        # if self.headless:
        #     chrome_options.add_argument("--headless")
        
        # Stealth options to avoid detection
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Additional options for better compatibility
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-plugins")
        chrome_options.add_argument("--disable-images")
        
        # Use a realistic user agent
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        # Disable images to speed up loading (we'll get image URLs separately)
        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_setting_values.notifications": 2
        }
        chrome_options.add_experimental_option("prefs", prefs)
        
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Execute script to remove webdriver property
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            self.driver.implicitly_wait(10)
            print("✅ Chrome WebDriver initialized successfully")
        except Exception as e:
            print(f"❌ Error setting up WebDriver: {e}")
            raise
    
    def load_store_page(self):
        """Load the DoorDash store page with Cloudflare handling"""
        try:
            print(f"🌐 Loading store page: {self.store_url}")
            self.driver.get(self.store_url)
            
            # Wait for page to load
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Check for Cloudflare challenge
            if self.handle_cloudflare_challenge():
                print("✅ Cloudflare challenge handled")
            
            # Additional wait for dynamic content
            time.sleep(5)
            print("✅ Store page loaded successfully")
            
        except Exception as e:
            print(f"❌ Error loading store page: {e}")
            raise
    
    def handle_cloudflare_challenge(self):
        """Handle Cloudflare verification challenge"""
        try:
            # Check if we're on a Cloudflare challenge page
            page_title = self.driver.title.lower()
            page_source = self.driver.page_source.lower()
            
            if "cloudflare" in page_title or "cloudflare" in page_source or "checking your browser" in page_source:
                print("🛡️ Cloudflare challenge detected, waiting for verification...")
                
                # Wait for the challenge to complete (up to 30 seconds)
                for i in range(30):
                    time.sleep(1)
                    current_title = self.driver.title.lower()
                    current_source = self.driver.page_source.lower()
                    
                    # Check if we're past the challenge
                    if ("cloudflare" not in current_title and 
                        "checking your browser" not in current_source and
                        "doordash" in current_title):
                        print("✅ Cloudflare challenge completed")
                        return True
                    
                    # Check if there's a manual verification button
                    try:
                        verify_button = self.driver.find_element(By.CSS_SELECTOR, 
                            "input[type='button'][value*='Verify'], button:contains('Verify'), .cf-browser-verification")
                        if verify_button.is_displayed():
                            print("🔘 Manual verification required - please complete the challenge in the browser")
                            # Wait for user to complete verification
                            for j in range(60):  # Wait up to 60 seconds
                                time.sleep(1)
                                if "doordash" in self.driver.title.lower():
                                    print("✅ Manual verification completed")
                                    return True
                            break
                    except:
                        pass
                
                print("⚠️ Cloudflare challenge timeout")
                return False
            
            return True
            
        except Exception as e:
            print(f"⚠️ Error handling Cloudflare challenge: {e}")
            return False
    
    def extract_store_info(self):
        """Extract basic store information"""
        try:
            print("📋 Extracting store information...")
            
            # Try to get store name
            store_name = "Unknown Store"
            try:
                name_element = self.driver.find_element(By.CSS_SELECTOR, "h1, [data-testid='store-name'], .store-name")
                store_name = name_element.text.strip()
            except:
                # Fallback selectors
                try:
                    name_element = self.driver.find_element(By.CSS_SELECTOR, "h1")
                    store_name = name_element.text.strip()
                except:
                    pass
            
            # Try to get store address
            address = "Unknown Address"
            try:
                address_element = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='store-address'], .store-address, address")
                address = address_element.text.strip()
            except:
                pass
            
            # Try to get store hours
            hours = "Unknown Hours"
            try:
                hours_element = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='store-hours'], .store-hours")
                hours = hours_element.text.strip()
            except:
                pass
            
            self.scraped_data["store_info"] = {
                "name": store_name,
                "address": address,
                "hours": hours,
                "url": self.store_url
            }
            
            print(f"✅ Store info extracted: {store_name}")
            
        except Exception as e:
            print(f"⚠️ Error extracting store info: {e}")
    
    def extract_categories_and_products(self):
        """Extract product categories and items"""
        try:
            print("🛍️ Extracting categories and products...")
            
            # Wait for menu content to load
            time.sleep(5)
            
            # Debug: Save page source to see what we're working with
            self.debug_page_structure()
            
            # Try different selectors for categories - updated for current DoorDash structure
            category_selectors = [
                "[data-testid='menu-category']",
                "[data-testid='category']",
                ".menu-category",
                "[class*='category']",
                "[class*='Category']",
                "h2", "h3", "h4",
                "[role='tab']",
                "[role='button']",
                "button[class*='category']",
                "div[class*='category']"
            ]
            
            categories = []
            for selector in category_selectors:
                try:
                    categories = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if categories:
                        print(f"✅ Found {len(categories)} categories using selector: {selector}")
                        # Print first few category names for debugging
                        for i, cat in enumerate(categories[:3]):
                            print(f"   Category {i+1}: '{cat.text.strip()}'")
                        break
                except:
                    continue
            
            if not categories:
                print("⚠️ No categories found, trying alternative approach...")
                # Try to find any menu items directly
                self.extract_products_directly()
                return
            
            for i, category_element in enumerate(categories):
                try:
                    category_name = category_element.text.strip()
                    if not category_name or len(category_name) < 2:
                        continue
                    
                    print(f"📂 Processing category: {category_name}")
                    
                    # Click on category to expand it (if needed)
                    try:
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", category_element)
                        time.sleep(1)
                        category_element.click()
                        time.sleep(3)
                    except:
                        pass
                    
                    # Extract products in this category
                    products = self.extract_products_in_category(category_name)
                    
                    if products:
                        self.scraped_data["categories"][category_name] = {
                            "product_count": len(products),
                            "products": products
                        }
                        
                        # Add products to main products list
                        for product in products:
                            product["category"] = category_name
                            self.scraped_data["products"].append(product)
                    
                except Exception as e:
                    print(f"⚠️ Error processing category {i}: {e}")
                    continue
            
            print(f"✅ Extracted {len(self.scraped_data['products'])} products from {len(self.scraped_data['categories'])} categories")
            
        except Exception as e:
            print(f"❌ Error extracting categories and products: {e}")
    
    def debug_page_structure(self):
        """Debug function to analyze page structure"""
        try:
            print("🔍 Analyzing page structure...")
            
            # Get all elements with common product-related classes
            debug_selectors = [
                "[class*='item']",
                "[class*='product']",
                "[class*='menu']",
                "[class*='card']",
                "[class*='listing']",
                "[data-testid*='item']",
                "[data-testid*='product']",
                "[data-testid*='menu']"
            ]
            
            for selector in debug_selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        print(f"   Found {len(elements)} elements with selector: {selector}")
                        # Show first few element texts
                        for i, elem in enumerate(elements[:3]):
                            text = elem.text.strip()
                            if text and len(text) < 100:
                                print(f"     Element {i+1}: '{text[:50]}...'")
                except:
                    continue
            
            # Check for common DoorDash patterns
            doordash_patterns = [
                "div[class*='StoreMenu']",
                "div[class*='MenuCategory']",
                "div[class*='MenuItem']",
                "div[class*='ProductCard']",
                "div[class*='ItemCard']"
            ]
            
            for pattern in doordash_patterns:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, pattern)
                    if elements:
                        print(f"   Found {len(elements)} DoorDash pattern elements: {pattern}")
                except:
                    continue
                    
        except Exception as e:
            print(f"⚠️ Debug error: {e}")
    
    def extract_products_in_category(self, category_name: str) -> List[Dict]:
        """Extract products within a specific category"""
        products = []
        
        # Try different selectors for product items - updated for current DoorDash structure
        product_selectors = [
            "[data-testid='menu-item']",
            "[data-testid='item']",
            "[data-testid='product']",
            ".menu-item",
            "[class*='MenuItem']",
            "[class*='ProductCard']",
            "[class*='ItemCard']",
            "[class*='item']",
            "[class*='product']",
            "[class*='card']",
            "div[class*='StoreMenuItem']",
            "div[class*='MenuCard']"
        ]
        
        product_elements = []
        for selector in product_selectors:
            try:
                product_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if product_elements:
                    print(f"   Found {len(product_elements)} products using selector: {selector}")
                    break
            except:
                continue
        
        if not product_elements:
            print(f"   No products found for category: {category_name}")
            return products
        
        for i, product_element in enumerate(product_elements):
            try:
                product_data = self.extract_product_data(product_element)
                if product_data:
                    products.append(product_data)
                    if i < 3:  # Show first few products for debugging
                        print(f"     Product {i+1}: {product_data['name']} - {product_data['price']}")
            except Exception as e:
                print(f"⚠️ Error extracting product {i}: {e}")
                continue
        
        return products
    
    def extract_product_data(self, product_element) -> Optional[Dict]:
        """Extract data from a single product element"""
        try:
            product_data = {
                "name": "",
                "description": "",
                "price": "",
                "image_url": "",
                "category": "",
                "availability": "available"
            }
            
            # Extract product name
            name_selectors = [
                "[data-testid='menu-item-name']",
                ".menu-item-name",
                "h3", "h4", "h5",
                "[class*='name']",
                "[class*='title']"
            ]
            
            for selector in name_selectors:
                try:
                    name_element = product_element.find_element(By.CSS_SELECTOR, selector)
                    product_data["name"] = name_element.text.strip()
                    if product_data["name"]:
                        break
                except:
                    continue
            
            # Extract description
            desc_selectors = [
                "[data-testid='menu-item-description']",
                ".menu-item-description",
                "[class*='description']",
                "p"
            ]
            
            for selector in desc_selectors:
                try:
                    desc_element = product_element.find_element(By.CSS_SELECTOR, selector)
                    product_data["description"] = desc_element.text.strip()
                    if product_data["description"]:
                        break
                except:
                    continue
            
            # Extract price
            price_selectors = [
                "[data-testid='menu-item-price']",
                ".menu-item-price",
                "[class*='price']",
                "[class*='cost']"
            ]
            
            for selector in price_selectors:
                try:
                    price_element = product_element.find_element(By.CSS_SELECTOR, selector)
                    price_text = price_element.text.strip()
                    # Clean price text
                    price_match = re.search(r'\$[\d,]+\.?\d*', price_text)
                    if price_match:
                        product_data["price"] = price_match.group()
                        break
                except:
                    continue
            
            # Extract image URL
            try:
                img_element = product_element.find_element(By.CSS_SELECTOR, "img")
                img_src = img_element.get_attribute("src")
                if img_src:
                    # Convert relative URLs to absolute
                    product_data["image_url"] = urljoin(self.store_url, img_src)
            except:
                pass
            
            # Only return product if we have at least a name
            if product_data["name"]:
                return product_data
            
        except Exception as e:
            print(f"⚠️ Error extracting product data: {e}")
        
        return None
    
    def extract_products_directly(self):
        """Extract products directly without categories (optimized method)"""
        try:
            print("🔄 Extracting products directly...")
            
            # Focus on the elements we know contain products
            product_selectors = [
                "[class*='card']",  # We saw 54 elements with this
                "[class*='item']",  # We saw 60 elements with this
                "[data-testid*='item']"  # We saw 6 elements with this
            ]
            
            products = []
            seen_products = set()
            
            for selector in product_selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    print(f"   Processing {len(elements)} elements with selector: {selector}")
                    
                    for i, element in enumerate(elements):
                        try:
                            text = element.text.strip()
                            
                            # Look for price pattern
                            price_match = re.search(r'\$[\d,]+\.?\d*', text)
                            if price_match and len(text) > 10 and len(text) < 500:
                                
                                # Extract product name - look for text before "Add" or first line
                                lines = text.split('\n')
                                name = ""
                                
                                # Find the product name (usually before "Add" button)
                                for line in lines:
                                    line = line.strip()
                                    if line and not line.startswith('Add') and not line.startswith('$') and len(line) > 3:
                                        name = line
                                        break
                                
                                if not name:
                                    name = lines[0].strip() if lines else text[:50]
                                
                                # Clean up name
                                name = re.sub(r'\s+', ' ', name).strip()
                                if len(name) > 100:
                                    name = name[:100] + "..."
                                
                                # Skip duplicates
                                if name in seen_products:
                                    continue
                                seen_products.add(name)
                                
                                # Extract image URL if available
                                image_url = ""
                                try:
                                    img_element = element.find_element(By.CSS_SELECTOR, "img")
                                    img_src = img_element.get_attribute("src")
                                    if img_src:
                                        image_url = urljoin(self.store_url, img_src)
                                except:
                                    pass
                                
                                product_data = {
                                    "name": name,
                                    "description": text[:200] if len(text) > 200 else text,
                                    "price": price_match.group(),
                                    "image_url": image_url,
                                    "category": "General",
                                    "availability": "available"
                                }
                                products.append(product_data)
                                
                                if len(products) <= 10:  # Show first 10 for debugging
                                    print(f"     Product {len(products)}: {name} - {price_match.group()}")
                                
                                # Limit to reasonable number of products
                                if len(products) >= 100:
                                    break
                                    
                        except Exception as e:
                            continue
                    
                    if products:
                        break  # Found products, no need to try other selectors
                        
                except Exception as e:
                    continue
            
            if products:
                self.scraped_data["categories"]["General"] = {
                    "product_count": len(products),
                    "products": products
                }
                self.scraped_data["products"] = products
                print(f"✅ Extracted {len(products)} products successfully")
            else:
                print("   No products found with direct extraction")
            
        except Exception as e:
            print(f"❌ Error in direct product extraction: {e}")
    
    def save_data(self, filename: str = "doordash_data.json"):
        """Save scraped data to JSON file"""
        try:
            # Create output directory if it doesn't exist
            os.makedirs("output", exist_ok=True)
            filepath = os.path.join("output", filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.scraped_data, f, indent=2, ensure_ascii=False)
            
            print(f"💾 Data saved to: {filepath}")
            return filepath
            
        except Exception as e:
            print(f"❌ Error saving data: {e}")
            return None
    
    def run(self):
        """Run the complete scraping process"""
        try:
            print("🚀 Starting DoorDash scraper...")
            
            # Try Selenium approach first
            try:
                self.setup_driver()
                self.load_store_page()
                
                # Extract data
                self.extract_store_info()
                self.extract_categories_and_products()
                
            except Exception as selenium_error:
                print(f"⚠️ Selenium approach failed: {selenium_error}")
                print("🔄 Trying requests-based approach...")
                
                # Fallback to requests approach
                self.try_requests_approach()
            
            # Save results
            output_file = self.save_data()
            
            print(f"✅ Scraping completed successfully!")
            print(f"📊 Results:")
            print(f"   - Store: {self.scraped_data['store_info'].get('name', 'Unknown')}")
            print(f"   - Categories: {len(self.scraped_data['categories'])}")
            print(f"   - Products: {len(self.scraped_data['products'])}")
            
            return self.scraped_data
            
        except Exception as e:
            print(f"❌ Scraping failed: {e}")
            return None
        
        finally:
            if self.driver:
                self.driver.quit()
                print("🔒 Browser closed")
    
    def try_requests_approach(self):
        """Fallback method using requests and BeautifulSoup"""
        try:
            print("🌐 Trying requests-based scraping...")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }
            
            response = requests.get(self.store_url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract store info
            store_name = "Unknown Store"
            try:
                title_tag = soup.find('title')
                if title_tag:
                    store_name = title_tag.get_text().strip()
            except:
                pass
            
            self.scraped_data["store_info"] = {
                "name": store_name,
                "address": "Unknown Address",
                "hours": "Unknown Hours", 
                "url": self.store_url
            }
            
            # Try to extract products from static content
            products = []
            
            # Look for any elements containing prices
            price_elements = soup.find_all(text=re.compile(r'\$[\d,]+\.?\d*'))
            
            for price_element in price_elements:
                try:
                    parent = price_element.parent
                    if parent:
                        text_content = parent.get_text().strip()
                        if len(text_content) > 5 and len(text_content) < 300:
                            # Extract product name (first line)
                            lines = text_content.split('\n')
                            name = lines[0].strip() if lines else text_content[:50]
                            
                            product_data = {
                                "name": name,
                                "description": text_content,
                                "price": re.search(r'\$[\d,]+\.?\d*', text_content).group(),
                                "image_url": "",
                                "category": "General",
                                "availability": "available"
                            }
                            products.append(product_data)
                except:
                    continue
            
            if products:
                self.scraped_data["categories"]["General"] = {
                    "product_count": len(products),
                    "products": products
                }
                self.scraped_data["products"] = products
                print(f"✅ Extracted {len(products)} products using requests")
            else:
                print("⚠️ No products found with requests approach")
                
        except Exception as e:
            print(f"❌ Requests approach failed: {e}")


def main():
    """Main function to run the scraper"""
    store_url = "https://www.doordash.com/convenience/store/27498004/"
    
    print("=" * 60)
    print("🛒 DoorDash Store Scraper")
    print("=" * 60)
    
    scraper = DoorDashScraper(store_url, headless=False)  # Set to True for headless mode
    result = scraper.run()
    
    if result:
        print("\n🎉 Scraping completed successfully!")
    else:
        print("\n💥 Scraping failed!")


if __name__ == "__main__":
    main()