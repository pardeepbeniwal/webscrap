from bs4 import BeautifulSoup as soup
from urllib import urlopen  as uReq
import csv

myurl = 'https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=video+card&ignorear=0&N=-1&isNodeId=1'
#opening connection
uClient = uReq(myurl)
page_html  = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,'html.parser')

containers = page_soup.findAll("div", {"class":"item-container"})
filename = 'productlist.csv'
with open(filename, 'w') as outfile:
	f = csv.writer(outfile, delimiter=' ')

	f.writerow("title,description,price\n")
	for container in containers:
	 title = container.div.div.a.img["title"]

	 description = container.findAll("a", {"class":"item-title"})
	 price = container.findAll("li", {"class":"price-current"})

	 description = description[0].text
	 price = price[0].text.strip()
	 price = price.encode('ascii', 'ignore')
	 f.writerow(title+","+description.replace(",","|")+","+price.replace(","," "))
 



