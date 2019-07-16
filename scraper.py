import bs4
import requests
import csv

res=requests.get("https://karki23.github.io/Weather-Data/BadgerysCreek.html")#any city for just header
soup=bs4.BeautifulSoup(res.text,"lxml")
a=soup.select("th")#for the heading of each column
a=[i.text for i in a]
length=len(a)#number of columns
with open("project.csv","a") as csvfile:
	csvfilewrite=csv.writer(csvfile)
	csvfilewrite.writerow(a)

#for the data
r=requests.get("https://karki23.github.io/Weather-Data/assignment.html")
s=bs4.BeautifulSoup(r.text,"lxml")
container=s.select("a")
data=[]
for i in container:
	url=i["href"]
	city=url.split(".")[0]
	data.append(city)
#data is list of all cities
q="https://karki23.github.io/Weather-Data/"
data=[q+i+".html" for i in data]

for i in data:
	res=requests.get(i)
	soup=bs4.BeautifulSoup(res.text,"lxml")
	a=soup.select("td")
	a=[i.text for i in a]
	x=0
	c=0
	d=[]
	m=len(a)//length#to get the total number of rows
	for i in range(m):#to get a list of list so that it is in proper type to fit in csv file
		b=[]
		while(c<length):#there are 24 columns we can use c<24 also
			b.append(a[x])
			c+=1
			x+=1
		c=0
		d.append(b)
	with open("project.csv","a") as csvfile:
		csvfilewrite=csv.writer(csvfile)
		csvfilewrite.writerows(d)

