# 📰 News Headline Scraper

## Objective
A simple Python script that scrapes the latest news headlines from a public news website and saves them to a `.txt` file for offline reading or analysis.

---

## Tools Used
- **Python 3.x**
- requests: To fetch web page content
- BeautifulSoup: To parse HTML

---

## 📁 Project Files
- `webscraper.py`: The main Python script
- `headlines.txt`: Output file that contains the scraped headlines

---

## 🚀 How It Works
1. The script sends an HTTP request to the news website.
2. It parses the HTML to find elements containing the headlines (e.g. `<span itemprop="headline">`).
3. The extracted headlines are saved into `headlines.txt`.
4. Optionally, you can modify the code to scrape other websites or headline formats.

