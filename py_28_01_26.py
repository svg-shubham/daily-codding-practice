# Extract all emails from text (Regex)
import re
text = "Contact me at test@gmail.com or hr@company.co.in"
email = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}', text)
# print(email)

# Count word frequency (unstructured text)
text = "python scraping python data mining"
words = {}
for i in text.split(" "):
    if i not in words:
        words[i] = 1
    else:
        words[i] += 1
# print(words)

# Remove special characters from text

text = "Hello!! Python@@#123"
clean = re.sub(r'[^a-zA-Z0-9 ]', '', text)
# print(clean)

# Read CSV and find max value (Pandas)
# import pandas as pd 
# df = pd.read_csv("data.csv")
# print(df['salary'].max())

# Scrape titles from webpage (BeautifulSoup)
import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_6o3s351fev_e&adgrpid=150668181581&hvpone=&hvptwo=&hvadid=674842289449&hvpos=&hvnetw=g&hvrand=10283708900956104782&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062097&hvtargid=kwd-300061672064&hydadcr=5621_2359492&gad_source=1").text
soup = BeautifulSoup(html,'html.parser')
# titles = [h.text for h in soup.find_all("h2")]
# print(titles)
# for h in soup:
#     print(h.text)

#Handle pagination in scraping
for page in range(1, 6):
    url = f"https://example.com/jobs?page={page}"
    print("Scraping:", url)