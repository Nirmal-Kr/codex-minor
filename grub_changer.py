import requests
import random
from bs4 import BeautifulSoup
def link_creation():

	i=input("Enter a Desired Tag=>")
	r=requests.get("https://alpha.wallhaven.cc/search?q="+i+"&categories=100&purity=100&sorting=date_added&order=desc&page=2")
	soup=BeautifulSoup(r.content,"lxml")
	mylinks=soup.find_all("a",class_="preview")
	i=len(mylinks)
	rand_i=random.randrange(0,i)

	l=mylinks[rand_i].get("href")
	id=l[37:43]
	fst='https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'
	url = fst+id+'.jpg'
	return(url)
def fetching_image(url):
	r = requests.get(url)
	with open('/home/ashispadhi/Downloads/cat.jpg', 'wb') as f:  
		f.write(r.content)

	 #Retrieve HTTP meta-data
	print(r.status_code)  
	print(r.headers['content-type'])  
	print(r.encoding)  
	

fetch_url=link_creation()
fetching_image(fetch_url)




