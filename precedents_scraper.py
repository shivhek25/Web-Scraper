import csv
import requests	
import urllib.request
import time
from bs4 import BeautifulSoup

url = "https://www.advocatekhoj.com/library/judgments/announcement.php"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.select("#contentarea > table:nth-of-type(2) > tr > td:nth-of-type(2) > a")
for link in links:
	ipcUrl = "https://www.advocatekhoj.com" + link.get('href')
	print(ipcUrl)
	response2 = requests.get(ipcUrl)
	soup2 = BeautifulSoup(response2.text, "html.parser")
	precedent = soup2.select("#maincontainer > #content_container > #contentarea > p")
	print(precedent)