#!/usr/bin/env python3
"""
HTML Data Extractor for DoorDash Products
Extracts product data from HTML content in data.txt file
"""

import json
import os
import re
from bs4 import BeautifulSoup
from typing import Dict, List


def extract_products_from_html(html_content: str, category: str = "Sparkling & Sweet") -> Dict:
    """
    Extract product data from HTML content
    
    Args:
        html_content: The HTML content to parse
        category: The category name for the products
    
    Returns:
        Dictionary containing extracted product data
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Debug: Check what's actually in the HTML
    print("🔍 Debugging HTML structure...")
    all_divs = soup.find_all('div')
    print(f"   Total div elements: {len(all_divs)}")
    
    # Check for any data-testid attributes
    testid_elements = soup.find_all(attrs={'data-testid': True})
    print(f"   Elements with data-testid: {len(testid_elements)}")
    
    # Check for product name spans
    name_spans = soup.find_all('span', {'data-telemetry-id': 'priceNameInfo.name'})
    print(f"   Product name spans found: {len(name_spans)}")
    
    # Check for any spans that might contain product names
    all_spans = soup.find_all('span')
    product_like_spans = []
    for span in all_spans:
        text = span.get_text().strip()
        if text and ('Bottle' in text or 'ml)' in text or 'L)' in text) and len(text) > 20:
            product_like_spans.append(text)
    print(f"   Spans with product-like text: {len(product_like_spans)}")
    
    # Check for any elements with prices
    price_elements = soup.find_all(text=lambda text: text and '$' in text and any(char.isdigit() for char in text))
    print(f"   Elements with price text: {len(price_elements)}")
    
    # Initialize result structure
    result = {
        "store_info": {
            "name": "Go For it Liquor",
            "address": "Unknown Address", 
            "hours": "Unknown Hours",
            "url": "https://www.doordash.com/convenience/store/27498004/"
        },
        "categories": {},
        "products": []
    }
    
    # Find all product containers - try multiple selectors
    product_containers = soup.find_all('div', {'data-testid': 'LegoFlexibleItemSquareContainer'})
    
    # If no containers found with that selector, try alternative approaches
    if not product_containers:
        print("🔍 Trying alternative selectors...")
        # Try finding containers with product names
        name_spans = soup.find_all('span', {'data-telemetry-id': 'priceNameInfo.name'})
        if name_spans:
            # Get parent containers
            product_containers = [span.find_parent('div') for span in name_spans if span.find_parent('div')]
            print(f"   Found {len(product_containers)} containers via name spans")
        
        # If still no containers, try finding any divs that might contain products
        if not product_containers:
            print("🔍 Trying broader search...")
            # Look for any divs that contain price-like text
            all_divs = soup.find_all('div')
            potential_containers = []
            for div in all_divs:
                text = div.get_text()
                if '$' in text and ('ml)' in text or 'L)' in text):
                    potential_containers.append(div)
            product_containers = potential_containers
            print(f"   Found {len(product_containers)} potential containers via text search")
    
    print(f"🔍 Found {len(product_containers)} product containers")
    
    products = []
    
    for i, container in enumerate(product_containers):
        try:
            product_data = extract_single_product(container)
            if product_data:
                product_data["category"] = category
                products.append(product_data)
                print(f"   Product {i+1}: {product_data['name']} - {product_data['price']}")
        except Exception as e:
            print(f"⚠️ Error extracting product {i+1}: {e}")
            continue
    
    # Add products to result
    if products:
        result["categories"][category] = {
            "product_count": len(products),
            "products": products
        }
        result["products"] = products
    
    return result


def extract_single_product(container) -> Dict:
    """
    Extract data from a single product container
    
    Args:
        container: BeautifulSoup element containing product data
    
    Returns:
        Dictionary with product information
    """
    product_data = {
        "name": "",
        "description": "",
        "price": "",
        "image_url": "",
        "rating": "",
        "review_count": "",
        "availability": "available"
    }
    
    # Extract product name
    name_element = container.find('span', {'data-telemetry-id': 'priceNameInfo.name'})
    if name_element:
        product_data["name"] = name_element.get_text().strip()
    
    # Extract price
    price_container = container.find('div', class_='sc-85923f71-0')
    if price_container:
        price_spans = price_container.find_all('span')
        price_parts = []
        for span in price_spans:
            text = span.get_text().strip()
            if text and text != '$':
                price_parts.append(text)
        if price_parts:
            product_data["price"] = f"${'.'.join(price_parts)}"
    
    # Extract image URL
    img_element = container.find('img')
    if img_element:
        img_src = img_element.get('src')
        if img_src:
            product_data["image_url"] = img_src
    
    # Extract rating
    rating_element = container.find('span', class_='sc-78b48fa8-2')
    if rating_element:
        product_data["rating"] = rating_element.get_text().strip()
    
    # Extract review count
    review_element = container.find('span', class_='dxgIrH')
    if review_element:
        review_text = review_element.get_text().strip()
        product_data["review_count"] = review_text
    
    # Set description as name if no separate description
    if not product_data["description"]:
        product_data["description"] = product_data["name"]
    
    return product_data


def save_data(data: Dict, filename: str = "sparkling_sweet_data.json"):
    """
    Save extracted data to JSON file
    
    Args:
        data: The data to save
        filename: Output filename
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs("output", exist_ok=True)
        filepath = os.path.join("output", filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Data saved to: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error saving data: {e}")
        return None


def main():
    """Main function to extract data from HTML file"""
    import sys
    import os
    
    print("=" * 60)
    print("🍺🍾 DoorDash Products Extractor")
    print("=" * 60)
    
    # Determine input file and category
    input_file = "data.txt"
    category = "Sparkling & Sweet"
    
    # Check command line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if "beer" in input_file.lower():
            category = "Beer"
        elif "vodka" in input_file.lower():
            category = "Vodka"
        elif "seltzer" in input_file.lower():
            category = "Seltzer"
        elif "wine" in input_file.lower() or "sparkling" in input_file.lower():
            category = "Sparkling & Sweet"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} file not found!")
        print("Available files:")
        if os.path.exists("data.txt"):
            print("   - data.txt")
        if os.path.exists("input/beer-data.txt"):
            print("   - input/beer-data.txt")
        if os.path.exists("input/sparkling-sweets-data.txt"):
            print("   - input/sparkling-sweets-data.txt")
        return 1
    
    try:
        # Read HTML content from input file
        with open(input_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        print(f"📄 HTML content loaded from {input_file}")
        print(f"🏷️ Category: {category}")
        
        # Extract products
        result = extract_products_from_html(html_content, category)
        
        # Save results
        output_filename = f"{category.lower().replace(' ', '_').replace('&', 'and')}_data.json"
        output_file = save_data(result, output_filename)
        
        print(f"\n🎉 Extraction completed successfully!")
        print(f"📊 Summary:")
        print(f"   - Store: {result['store_info']['name']}")
        print(f"   - Categories: {len(result['categories'])}")
        print(f"   - Products: {len(result['products'])}")
        print(f"   - Output saved to: {output_file}")
        
        # Show sample products
        if result['products']:
            print(f"\n📋 Sample Products:")
            for i, product in enumerate(result['products'][:5]):
                print(f"   {i+1}. {product['name']} - {product['price']}")
                if product['rating']:
                    print(f"      Rating: {product['rating']} ({product['review_count']})")
                print(f"      Image: {product['image_url'][:50]}...")
                print()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
