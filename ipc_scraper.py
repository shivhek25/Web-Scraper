import csv
import requests	
import urllib.request
import time
from bs4 import BeautifulSoup

url = "https://devgan.in/all_sections_ipc.php"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.select("#content > div:nth-of-type(2) > a")
ipcDevgan = []
for link in links:
	print(link)
	print(link['href'])
	ipcUrl = "http://devgan.in" + link['href']
	response2 = requests.get(ipcUrl)
	soup2 = BeautifulSoup(response2.text, "html.parser")
	ipc = soup2.select(".mys-head > td:nth-of-type(1) > a > h2")
	chapter = soup2.select(".mys-head > td:nth-of-type(2) > a > h2")
	description = soup2.select(".mys-desc > td > p")
	if(len(description) == 0):
		description = soup2.select(".mys-desc > td > ol")
	temp = {
		"IPC" : ipc[0].text,
		"Chapter" : chapter[0].text,
		"Description" : description[0].text
	}
	ipcDevgan.append(temp)
	print(temp)
with open("Indian Penal Code.csv", "w") as csv_file:
	column_names = ["IPC", "Chapter", "Description"]
	csv_writer = csv.DictWriter(csv_file, fieldnames = column_names, delimiter=',')
	csv_writer.writeheader()
	for line in ipcDevgan:
		csv_writer.writerow(line)

