# 🛒 Ecommerce Tracker

Ecommerce Tracker is a product monitoring and price intelligence platform built with Python and Streamlit. It helps users track product prices, monitor price changes over time, receive Telegram notifications, and generate analytics dashboards for better purchasing and market decisions.

---

## 🚀 Features

### 🔍 Product Monitoring

Track products from e-commerce websites and monitor:

* Product Name
* Current Price
* Product URL
* Price History

---

### 📈 Price Change Tracking

Automatically detects:

* Price Increases
* Price Decreases
* Historical Price Trends

All changes are stored for future analysis.

---

### 🔔 Telegram Notifications

Receive instant Telegram alerts when:

* Product prices drop
* Significant price changes occur
* New tracking events are detected

---

### 📊 Analytics Dashboard

Generate insights including:

* Products Tracked
* Average Price
* Highest Price
* Lowest Price
* Price Trend Analysis

---

### 📉 Historical Tracking

Maintain historical records of:

* Product Prices
* Price Change Events
* Tracking History

---

### 📤 Export Options

Export tracking data to:

* CSV
* Excel (XLSX)

---

## 📂 Sample Data

The repository includes sample tracking files:

```text
data/

├── products.csv
├── price_changes.csv
└── historical/
```

These files demonstrate product monitoring and price tracking workflows.

---

## 🛠 Technology Stack

* Python
* Streamlit
* Pandas
* Requests
* Telegram Bot API
* OpenPyXL

---

## 📁 Project Structure

```text
ecommerce-tracker/

├── ecommerce_tracker/
│   ├── alerts.py
│   ├── app.py
│   ├── scraper.py
│   ├── tracker.py
│   └── requirements.txt
│
├── data/
│   ├── products.csv
│   ├── price_changes.csv
│   └── historical/
│
├── README.md
└── .gitignore
```

---

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

---

## 🔔 Telegram Configuration

Configure your Telegram Bot credentials before enabling notifications.

Store credentials securely and avoid committing bot tokens to public repositories.

---

## 📈 Key Capabilities

* Product Price Tracking
* Price Change Detection
* Historical Analytics
* Telegram Notifications
* Dashboard Reporting
* Data Export

---

## 🎯 Business Use Cases

* Competitive Price Monitoring
* Product Tracking
* E-commerce Intelligence
* Market Analysis
* Consumer Price Alerts

---

## 🔮 Future Enhancements

* Multi-Website Tracking
* Price Forecasting
* Email Notifications
* Product Availability Monitoring
* AI-Powered Market Insights

---

## 👨‍💻 Author

**Biruhi Tesfaye Abeje**

Built as a portfolio project showcasing:

* Python Development
* Web Scraping
* Automation
* Telegram Bot Integration
* Data Analytics
* Streamlit Dashboard Development
