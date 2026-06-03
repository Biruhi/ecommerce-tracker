# ============================================
# FILE: tracker.py
# PROJECT:
# AI E-COMMERCE PRICE TRACKING SYSTEM
# PHASE 2 — HISTORICAL PRICE TRACKING
# ============================================

# ============================================
# IMPORT LIBRARIES
# ============================================

import pandas as pd
import os
from datetime import datetime

# ============================================
# FILE PATHS
# ============================================

CURRENT_FILE = "data/products.csv"

HISTORICAL_FOLDER = "data/historical"

PRICE_CHANGES_FILE = "data/price_changes.csv"

# ============================================
# CREATE HISTORICAL FOLDER
# ============================================

if not os.path.exists(HISTORICAL_FOLDER):

    os.makedirs(HISTORICAL_FOLDER)

# ============================================
# CURRENT TIMESTAMP
# ============================================

timestamp = datetime.now().strftime(

    "%Y-%m-%d_%H-%M-%S"

)

# ============================================
# HISTORICAL SNAPSHOT FILE
# ============================================

historical_file = (

    f"{HISTORICAL_FOLDER}/products_{timestamp}.csv"

)

# ============================================
# LOAD CURRENT PRODUCTS
# ============================================

current_df = pd.read_csv(

    CURRENT_FILE

)

# ============================================
# SAVE HISTORICAL SNAPSHOT
# ============================================

current_df.to_csv(

    historical_file,

    index=False

)

print()
print("=" * 60)
print("HISTORICAL SNAPSHOT SAVED")
print("=" * 60)

print(historical_file)

# ============================================
# GET PREVIOUS SNAPSHOT
# ============================================

historical_files = sorted(

    os.listdir(HISTORICAL_FOLDER)

)

# ============================================
# NEED AT LEAST 2 FILES TO COMPARE
# ============================================

if len(historical_files) < 2:

    print()
    print("=" * 60)
    print("NOT ENOUGH HISTORICAL FILES")
    print("RUN SCRAPER AGAIN LATER")
    print("=" * 60)

    exit()

# ============================================
# PREVIOUS FILE
# ============================================

previous_file = (

    f"{HISTORICAL_FOLDER}/"

    + historical_files[-2]

)

# ============================================
# CURRENT FILE
# ============================================

latest_file = (

    f"{HISTORICAL_FOLDER}/"

    + historical_files[-1]

)

# ============================================
# LOAD DATA
# ============================================

old_df = pd.read_csv(

    previous_file

)

new_df = pd.read_csv(

    latest_file

)

# ============================================
# CLEAN PRICE COLUMN
# ============================================

old_df["Price"] = (

    old_df["Price"]

    .replace("[$]", "", regex=True)

    .astype(float)

)

new_df["Price"] = (

    new_df["Price"]

    .replace("[$]", "", regex=True)

    .astype(float)

)

# ============================================
# MERGE DATA
# ============================================

merged_df = old_df.merge(

    new_df,

    on="Title",

    suffixes=("_OLD", "_NEW")

)

# ============================================
# DETECT PRICE CHANGES
# ============================================

price_changes = merged_df[

    merged_df["Price_OLD"]

    !=

    merged_df["Price_NEW"]

]

# ============================================
# SAVE PRICE CHANGES
# ============================================

price_changes.to_csv(

    PRICE_CHANGES_FILE,

    index=False

)

# ============================================
# OUTPUT RESULTS
# ============================================

print()
print("=" * 60)
print("PRICE TRACKING COMPLETED")
print("=" * 60)

print()

print(f"OLD FILE : {previous_file}")
print(f"NEW FILE : {latest_file}")

print()

print(

    f"PRICE CHANGES FOUND : "

    f"{len(price_changes)}"

)

print()

# ============================================
# SHOW CHANGES
# ============================================

if len(price_changes) > 0:

    for _, row in price_changes.iterrows():

        print("-" * 60)

        print(

            f"PRODUCT : {row['Title']}"

        )

        print(

            f"OLD PRICE : ${row['Price_OLD']}"

        )

        print(

            f"NEW PRICE : ${row['Price_NEW']}"

        )

else:

    print("NO PRICE CHANGES DETECTED")

print()

print("=" * 60)
print("PRICE CHANGE FILE SAVED")
print("=" * 60)

print(PRICE_CHANGES_FILE)