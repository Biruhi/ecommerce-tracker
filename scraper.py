# ============================================
# FILE: scraper.py
# PROJECT:
# AI E-COMMERCE PRICE TRACKING SYSTEM
# ADVANCED PROFESSIONAL VERSION
# ============================================

# ============================================
# INSTALL REQUIRED LIBRARIES
#
# pip install playwright pandas beautifulsoup4
#
# playwright install
# ============================================

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

# ============================================
# WEBSITE URLS
# ============================================

BASE_URL = "https://webscraper.io"

START_URL = (
    "https://webscraper.io/test-sites/"
    "e-commerce/allinone/computers/laptops"
)

# ============================================
# STORAGE
# ============================================

all_products = []

# ============================================
# CREATE DATA FOLDER
# ============================================

if not os.path.exists("data"):

    os.makedirs("data")

# ============================================
# START PLAYWRIGHT
# ============================================

with sync_playwright() as p:

    # ----------------------------------------
    # BROWSER CONFIGURATION
    # ----------------------------------------

    browser = p.chromium.launch(

        headless=False,

        slow_mo=300

    )

    # ----------------------------------------
    # CREATE PAGE
    # ----------------------------------------

    page = browser.new_page()

    # ----------------------------------------
    # OPEN WEBSITE
    # ----------------------------------------

    print()
    print("=" * 60)
    print("OPENING WEBSITE")
    print("=" * 60)

    page.goto(

        START_URL,

        timeout=60000

    )

    # ----------------------------------------
    # WAIT FOR NETWORK
    # ----------------------------------------

    page.wait_for_load_state(

        "networkidle"

    )

    # ----------------------------------------
    # WAIT UNTIL PRODUCTS APPEAR
    # ----------------------------------------

    page.wait_for_selector(

        "div.col-md-4.col-xl-4.col-lg-4",

        timeout=15000

    )

    current_page = 1

    # ========================================
    # PAGINATION LOOP
    # ========================================

    while True:

        print()
        print("=" * 60)
        print(f"SCRAPING PAGE {current_page}")
        print("=" * 60)

        # ------------------------------------
        # GET PAGE HTML
        # ------------------------------------

        html = page.content()

        soup = BeautifulSoup(

            html,

            "html.parser"

        )

        # ------------------------------------
        # FIND PRODUCTS
        # ------------------------------------

        products = soup.find_all(

            "div",

            class_="col-md-4 col-xl-4 col-lg-4"

        )

        print(f"FOUND {len(products)} PRODUCTS")

        # ====================================
        # SCRAPE PRODUCTS
        # ====================================

        for product in products:

            try:

                # ----------------------------
                # TITLE
                # ----------------------------

                title_element = product.find(

                    "a",

                    class_="title"

                )

                if title_element:

                    title_text = title_element.get(

                        "title",

                        ""

                    ).strip()

                else:

                    title_text = "N/A"

                # ----------------------------
                # PRICE
                # ----------------------------

                price_element = product.find(

                    "h4",

                    class_="price"

                )

                if price_element:

                    price_text = (

                        price_element.text.strip()

                    )

                else:

                    price_text = "N/A"

                # ----------------------------
                # DESCRIPTION
                # ----------------------------

                description_element = product.find(

                    "p",

                    class_="description"

                )

                if description_element:

                    description_text = (

                        description_element.text.strip()

                    )

                else:

                    description_text = "N/A"

                # ----------------------------
                # REVIEWS
                # ----------------------------

                reviews_element = product.find(

                    "p",

                    class_="review-count"

                )

                if reviews_element:

                    reviews_text = (

                        reviews_element.text.strip()

                    )

                else:

                    reviews_text = "N/A"

                # ----------------------------
                # PRODUCT URL
                # ----------------------------

                if title_element:

                    product_url = (

                        BASE_URL

                        + title_element.get(

                            "href",

                            ""

                        )

                    )

                else:

                    product_url = "N/A"

                # ----------------------------
                # SCRAPE TIMESTAMP
                # ----------------------------

                scraped_at = datetime.now().strftime(

                    "%Y-%m-%d %H:%M:%S"

                )

                # ----------------------------
                # SAVE DATA
                # ----------------------------

                all_products.append({

                    "Title": title_text,

                    "Price": price_text,

                    "Description": description_text,

                    "Reviews": reviews_text,

                    "Product URL": product_url,

                    "Scraped At": scraped_at

                })

                # ----------------------------
                # TERMINAL OUTPUT
                # ----------------------------

                print()
                print("-" * 60)
                print("TITLE :", title_text)
                print("PRICE :", price_text)
                print("REVIEWS :", reviews_text)

            except Exception as e:

                print()
                print("ERROR SCRAPING PRODUCT")
                print(e)

        # ====================================
        # FIND NEXT BUTTON
        # ====================================

        next_button = page.locator(

            "li.next a"

        )

        # ------------------------------------
        # CHECK IF NEXT PAGE EXISTS
        # ------------------------------------

        if next_button.count() > 0:

            print()
            print("MOVING TO NEXT PAGE...")

            next_button.click()

            # --------------------------------
            # WAIT FOR PAGE LOAD
            # --------------------------------

            page.wait_for_load_state(

                "networkidle"

            )

            # --------------------------------
            # WAIT UNTIL PRODUCTS APPEAR
            # --------------------------------

            page.wait_for_selector(

                "div.col-md-4.col-xl-4.col-lg-4",

                timeout=15000

            )

            current_page += 1

        else:

            print()
            print("=" * 60)
            print("NO MORE PAGES")
            print("=" * 60)

            break

    # ========================================
    # CLOSE BROWSER
    # ========================================

    browser.close()

# ============================================
# CREATE DATAFRAME
# ============================================

df = pd.DataFrame(

    all_products

)

# ============================================
# REMOVE DUPLICATES
# ============================================

df.drop_duplicates(

    inplace=True

)

# ============================================
# SAVE CSV
# ============================================

csv_file = (

    "data/products.csv"

)

df.to_csv(

    csv_file,

    index=False

)

# ============================================
# FINAL OUTPUT
# ============================================

print()
print("=" * 60)
print("SCRAPING COMPLETED")
print("=" * 60)

print(f"TOTAL PRODUCTS : {len(df)}")
print(f"CSV SAVED : {csv_file}")

print()
print(df.head())