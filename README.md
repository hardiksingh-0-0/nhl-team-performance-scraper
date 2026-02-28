# 🏒 NHL Team Performance Scraper

A structured web scraping and data analysis pipeline that extracts historical NHL team performance data from a paginated source and generates automated performance insights.

This project demonstrates end-to-end data extraction, cleaning, type conversion, and structured reporting using Python.

---

## 📌 Project Overview

The script scrapes multi-page NHL team statistics from a structured HTML table and converts raw web data into a clean analytical dataset.

It handles:
- Pagination logic
- Structured table parsing
- Numeric type conversion
- Data validation
- Automated Excel reporting
- Basic performance analysis

The result is a ready-to-use dataset suitable for further analytics or reporting workflows.

---

## 🚀 Features

- Paginated web scraping
- Robust HTML table parsing
- Data cleaning and validation
- Automatic type conversion (int/float)
- Excel export for reporting
- Performance insights generation

---

## 📊 Data Extracted

Each record includes:
- Team
- Year
- Wins
- Losses
- OTL (Overtime Losses)
- Win %
- Goals For
- Goals Against

---

## 📈 Insights Generated

The script automatically identifies:
- Season with the highest Win %
- Team with the most Goals Scored
- Structured dataset ready for further statistical analysis

---

## 🛠 Tech Stack

- Python
- requests
- BeautifulSoup
- pandas
- openpyxl

---

## 📂 Project Structure


nhl_performance_scraper.py
requirements.txt
README.md
.gitignore


---

## ▶️ How to Run

1. Clone the repository:


git clone https://github.com/YOUR_USERNAME/nhl-team-performance-scraper.git

cd nhl-team-performance-scraper


2. Install dependencies:


pip install -r requirements.txt


3. Run the scraper:


python nhl_performance_scraper.py


4. The processed dataset will be exported to:


nhl_team_performance_analysis.xlsx


---

## 🎯 Learning Objectives

This project was built to:
- Practice paginated scraping
- Work with structured HTML tables
- Perform data cleaning and type handling
- Build a complete scrape → process → export pipeline
- Generate automated insights from web data

---

## ⚠️ Notes

This project uses a public demo dataset for educational and portfolio purposes.