'''
This web scraper scrapes the website to get all sections of the Indian Penal Code.
'''

import csv #Module to help create and append data in CSV format
import requests	#Module to access webpages
from bs4 import BeautifulSoup #Module to scrape webpage 

url = "https://devgan.in/all_sections_ipc.php" #link of the webpage to be scraped
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.select("#content > div:nth-of-type(2) > a") #selecting all required anchor tags 
ipcDevgan = []
for link in links:
	ipcUrl = "http://devgan.in" + link['href'] #getting href value from a tag and appending with original link
	response2 = requests.get(ipcUrl)
	soup2 = BeautifulSoup(response2.text, "html.parser")
	ipc = soup2.select(".mys-head > td:nth-of-type(1) > a > h2") #gets section number 
	chapter = soup2.select(".mys-head > td:nth-of-type(2) > a > h2") #gets section heading 
	description = soup2.select(".mys-desc > td > p") #gets section description 
	if(len(description) == 0):
		description = soup2.select(".mys-desc > td > ol") #for cases when p tag isn't present
	#for sections with no description
	if(len(ipc) != 0):
		ipcTemp = ipc[0].text
	if(len(chapter) != 0):
		chp = chapter[0].text
	if(len(description) != 0):
		dsc = description[0].text
	#till here
	temp = {
		"IPC" : ipcTemp,
		"Chapter" : chp,
		"Description" : dsc
	} #dictionary to map heading and description to section number 
	ipcDevgan.append(temp) #creating list of dictionaries 
	print(temp)
with open("Indian Penal Code.csv", "w") as csv_file: #writing into csv with specified name 
	column_names = ["IPC", "Chapter", "Description"] #headers for csv
	csv_writer = csv.DictWriter(csv_file, fieldnames = column_names, delimiter=',')
	csv_writer.writeheader()
	for line in ipcDevgan:
		csv_writer.writerow(line) #accessing data from list and writing it to csv file

