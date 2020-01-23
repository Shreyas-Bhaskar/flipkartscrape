from requests import get
#url = 'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&offer=nb:mp:009b4f9b17&fm=neo%2Fmerchandising&iid=M_bac5b009-8249-414f-b36a-cf6108d0271d_2.829MSL2E4Q5W&ppt=browse&ppn=browse&ssid=sakrql0msoxyff281579753609876&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_4_2.dealCard.OMU_829MSL2E4Q5W_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_4_NA_view-all_2&cid=829MSL2E4Q5W'
#url ='https://www.flipkart.com/air-conditioners/pr?sid=j9e,abm,c54&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.technology%255B%255D%3DInverter&p[]=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Inverter%20AC'
url = "https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DiFFALCON%2Bby%2BTCL&otracker=nmenu_sub_TVs%20%26%20Appliances_0_iFFALCON%20by%20TCL"
category1 =url.partition('.com/')[2]
category2 =category1.partition('/')[2]
cat = category1.replace(category2,'')
cat = cat.replace('/','')

response = get(url)
from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
names=[]
ratings = []
prices =[]
#bs4.BeautifulSoup
product_containers = html_soup.find_all('div', class_ = 'bhgxx2 col-12-12')
print(type(product_containers))
print(len(product_containers))

# Extract data from individual  container
for container in product_containers:
	if container.find('div', class_ = 'col col-7-12') is not None:
		name = container.a.find('div',class_ = 'col col-7-12').div.text
		names.append(name)

#print(names)

for container in product_containers:
	if container.find('div', class_ = 'col col-7-12') is not None:
		rating = container.a.find('div',class_ = 'niH0FQ').span.div.text
		ratings.append(rating)

#print(ratings)

for container in product_containers:
	if container.find('div', class_ = 'col col-5-12 _2o7WAb') is not None:
		price = container.find('div',class_ = '_1vC4OE _2rQ-NK').text
		price = str(price).replace('₹','')
		prices.append(price)



#output to csv 
import csv

print(names)
with open('items.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Sn","Category","Name", "price","rating"])
	i = 1;
	while(i<len(names)):	
		writer.writerow([i,cat,names[i],prices[i],ratings[i]])
		i=i+1
	
	






