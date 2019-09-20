'''
This web scraper scrapes the website to get all previous cases 
filed with the Supreme Court and all judgements made by it and lower courts.
'''

import os #Module to create / modify folders
import requests	#Module to access webpages
from bs4 import BeautifulSoup #Module to scrape webpage 

url = "https://www.advocatekhoj.com/library/judgments/announcement.php" #webpage to be scraped
response = requests.get(url) #accessing webpage
soup = BeautifulSoup(response.text, "html.parser") 
links = soup.select("#contentarea > table:nth-of-type(2) > tr > td:nth-of-type(2) > a") #selecting required anchor tags using id found after inspecting
caseNumber = 0
for link in links:
	ipcUrl = "https://www.advocatekhoj.com" + link.get('href') #extracting link of each section of the IPC
	response2 = requests.get(ipcUrl)
	soup2 = BeautifulSoup(response2.text, "html.parser")
	precedent = soup2.findAll("p",{"align": ["right", "justify"]}) #selecting all paragraph tags which contain case details 
	precedentText = ""
	for textTag in precedent:
		precedentText = precedentText + textTag.text #converting p tags to normal text
	caseNumber = caseNumber + 1	
	filename = "Case " + str(caseNumber) + ".txt" 
	print(filename)
	filepath = os.path.join("/Users/shivamsinghal0610/Desktop/Web Scraper/Precedents/Precedents", filename) #specifying path where cases are to be saved
	if not os.path.exists("/Users/shivamsinghal0610/Desktop/Web Scraper/Precedents/Precedents"): 
		os.makedirs("/Users/shivamsinghal0610/Desktop/Web Scraper/Precedents/Precedents") #creating folder if it doesn't exist
	f = open(filepath, "w+") #accessing file where data is to be saved
	f.write(precedentText) #writing into file
	f.close() #closing file 