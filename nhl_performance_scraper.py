import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://www.scrapethissite.com/pages/forms/"
OUTPUT_FILE = "nhl_team_performance_analysis.xlsx"


# ---------- Utility Cleaning Functions ----------

def safe_int(value):
    value = value.strip()
    return int(value) if value.isdigit() else 0


def safe_float(value):
    value = value.strip()
    try:
        return float(value)
    except ValueError:
        return 0.0


# ---------- Fetch Page ----------

def fetch_page(page):
    url = f"{BASE_URL}?page_num={page}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed on page {page}: {e}")
        return None

    return BeautifulSoup(response.text, "html.parser")


# ---------- Parse Page ----------

def parse_page(soup):
    rows = soup.find_all("tr", class_="team")
    page_data = []

    for row in rows:
        cols = row.find_all("td")

        if len(cols) >= 8:
            page_data.append({
                "Team": cols[0].text.strip(),
                "Year": safe_int(cols[1].text),
                "Wins": safe_int(cols[2].text),
                "Losses": safe_int(cols[3].text),
                "OTL": safe_int(cols[4].text),   # Some seasons are blank → handled
                "Win%": safe_float(cols[5].text),
                "Goals For": safe_int(cols[6].text),
                "Goals Against": safe_int(cols[7].text)
            })

    return page_data


# ---------- Scrape All Pages ----------

def scrape_all_pages():
    page = 1
    all_data = []

    while True:
        print(f"Scraping page {page}...")

        soup = fetch_page(page)
        if soup is None:
            break

        page_data = parse_page(soup)

        if not page_data:
            break

        all_data.extend(page_data)
        page += 1

    return all_data


# ---------- Basic Analysis ----------

def analyze_data(df):
    print("\n🏆 Best Win% Season:")
    print(df.loc[df["Win%"].idxmax()])

    print("\n🔥 Most Goals Scored in a Season:")
    print(df.loc[df["Goals For"].idxmax()])


# ---------- Main ----------

def main():
    data = scrape_all_pages()

    if not data:
        print("No data scraped.")
        return

    df = pd.DataFrame(data)

    # Sort by Win% descending
    df = df.sort_values(by="Win%", ascending=False)

    # Export to Excel
    df.to_excel(OUTPUT_FILE, index=False)

    analyze_data(df)

    print(f"\n✅ Scraped {len(df)} records successfully.")
    print(f"📁 Data saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()