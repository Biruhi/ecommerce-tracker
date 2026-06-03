# ============================================
# FILE: alerts.py
# PROJECT:
# AI E-COMMERCE PRICE TRACKING SYSTEM
# PROFESSIONAL TELEGRAM SUMMARY ALERTS
# ============================================

# ============================================
# INSTALL REQUIRED LIBRARIES
#
# pip install requests pandas
# ============================================

import pandas as pd
import requests
import os
from datetime import datetime

# ============================================
# TELEGRAM CONFIGURATION
# ============================================

BOT_TOKEN = "8427127415:AAEcW-l9rMDXIzIWtvwLlsj70gc40B_5hwA"

CHAT_ID = "348674606"

# ============================================
# PRICE CHANGES FILE
# ============================================

PRICE_CHANGES_FILE = (

    "data/price_changes.csv"

)

# ============================================
# MAX PRODUCTS IN REPORT
# ============================================

MAX_PRODUCTS = 5

# ============================================
# CHECK FILE EXISTS
# ============================================

if not os.path.exists(

    PRICE_CHANGES_FILE

):

    print()
    print("=" * 60)
    print("PRICE CHANGE FILE NOT FOUND")
    print("=" * 60)

    exit()

# ============================================
# LOAD PRICE CHANGES
# ============================================

df = pd.read_csv(

    PRICE_CHANGES_FILE

)

# ============================================
# CHECK IF EMPTY
# ============================================

if len(df) == 0:

    print()
    print("=" * 60)
    print("NO PRICE CHANGES DETECTED")
    print("=" * 60)

    exit()

# ============================================
# REPORT TIMESTAMP
# ============================================

report_time = datetime.now().strftime(

    "%Y-%m-%d %H:%M:%S"

)

# ============================================
# BUILD SUMMARY MESSAGE
# ============================================

message = f"""
PRICE MONITORING REPORT

Generated At:
{report_time}

Total Price Changes:
{len(df)}

Showing Top {MAX_PRODUCTS} Changes

"""

# ============================================
# ADD PRODUCT CHANGES
# ============================================

for index, row in df.head(MAX_PRODUCTS).iterrows():

    old_price = row["Price_OLD"]

    new_price = row["Price_NEW"]

    difference = old_price - new_price

    message += f"""

--------------------------------

{index + 1}. {row['Title']}

OLD PRICE:
${old_price}

NEW PRICE:
${new_price}

PRICE CHANGE:
${difference}

"""

# ============================================
# REMAINING PRODUCTS
# ============================================

remaining = len(df) - MAX_PRODUCTS

if remaining > 0:

    message += f"""

--------------------------------

And {remaining} more changes...
"""

# ============================================
# TELEGRAM API URL
# ============================================

url = (

    f"https://api.telegram.org/bot"

    f"{BOT_TOKEN}/sendMessage"

)

# ============================================
# PAYLOAD
# ============================================

payload = {

    "chat_id": CHAT_ID,

    "text": message

}

# ============================================
# MESSAGE LENGTH DEBUG
# ============================================

print()
print("=" * 60)
print("MESSAGE LENGTH")
print("=" * 60)

print(len(message))

# ============================================
# SEND TELEGRAM MESSAGE
# ============================================

response = requests.post(

    url,

    data=payload

)

# ============================================
# TERMINAL OUTPUT
# ============================================

print()
print("=" * 60)

if response.status_code == 200:

    print("SUMMARY ALERT SENT SUCCESSFULLY")

else:

    print("FAILED TO SEND ALERT")

    print(response.text)

print("=" * 60)

print()
print("TOTAL CHANGES :", len(df))

print()
print("TELEGRAM REPORT:")
print()

print(message)