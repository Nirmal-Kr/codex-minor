import requests
import random
from tkinter import *
from bs4 import BeautifulSoup


	
	
def link_creation():
	root =Tk()
	root.geometry("640x640+0+0")
	root.title("Grub Changer")
	heading=Label(root, text="Enter your favourite tag:", font=("arial", 40, "bold"), fg="steelblue").pack()
	def do_it():
		global t
		inputValue=textBox.get("1.0","end-1c")
		print(inputValue)
		r=requests.get("https://alpha.wallhaven.cc/search?q="+inputValue+"&categories=100&purity=100&sorting=date_added&order=desc&page=2")
		soup=BeautifulSoup(r.content,"lxml")
		mylinks=soup.find_all("a",class_="preview")
		i=len(mylinks)
		if(i==0):
			print("The tag you entered is not present")
		else:
			rand_i=random.randrange(0,i)

			l=mylinks[rand_i].get("href")
			id=l[37:43]
			fst='https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'
			url = fst+id+'.jpg'
			t=url
	
	
	textBox=Text(root,height=2,width=10)
	textBox.pack()
	work=Button(root, text="Download", width=30, height=3,bg="lightblue",command=lambda:do_it()).place(x=250, y=300)
	root.mainloop()
	return(t)
		
def fetching_image(url):
	r = requests.get(url)
	with open('/home/ashispadhi/Downloads/cat.jpg', 'wb') as f:  
		f.write(r.content)

	 #Retrieve HTTP meta-data
	print(r.status_code)  
	print(r.headers['content-type'])  
	print(r.encoding)  
	
t=" "
fetch_url=link_creation()
if(fetch_url!=0):
	fetching_image(fetch_url)
	

	



