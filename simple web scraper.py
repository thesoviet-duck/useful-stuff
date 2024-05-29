from bs4 import BeautifulSoup
import requests
import csv

# get the link and thing
page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

# get the quotes and authors
qoutes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})

# make a new csv file
file = open("scraped_quotes.csv", "w")
# create a writer
writer = csv.writer(file)

# create title column of the csv file
writer.writerow(["AUTHORS", "QUOTES"])

# do some fancy stuff to print and add the stuff to the csv file
for qoute, author in zip(qoutes, authors):
	print(qoute.text + "-" + author.text + "\n")
	writer.writerow([author.text, qoute.text])

# close da file
file.close()
