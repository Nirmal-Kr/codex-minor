import requests
import random

print('Beginning file download with requests')
fst='https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'
randi=random.randint(1,610000)
url = fst+str(randi)+'.jpg'  

r = requests.get(url)
while(r.headers['content-type']!='image/jpeg'):
	fst='https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'
	randi=random.randint(56000,610000)
	url = fst+str(randi)+'.jpg'  
	r = requests.get(url)
with open('/home/nirmal/Downloads/cat.jpg', 'wb') as f:  
	f.write(r.content)

 #Retrieve HTTP meta-data
print(r.status_code)  
print(r.headers['content-type'])  
print(r.encoding)  


