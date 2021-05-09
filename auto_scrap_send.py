import requests
from bs4 import BeautifulSoup
import time
import csv
import re
from email import encoders
import func_email


urls=["https://ticker.finology.in/Company/TVSMOTOR","https://ticker.finology.in/Company/BAJAJ-AUTO","https://ticker.finology.in/Company/EICHERMOT","https://ticker.finology.in/Company/HEROMOTOCO"]

csv_file= open("scrape.csv" ,"w",encoding="utf-8")
csv_writer= csv.writer(csv_file)

csv_writer.writerow(["stock_name","stock_price","Market Cap","Enterprise Value","No. Of Shares","P/E","P/B",'Face Value',"Div Yield","Book Value","Cash","Debt","Promoter Holding","EPS","Sales Growth","Roe","Roce","Profit Growth"])

for url in urls:
    
    stock=[]

    headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

    html_page = requests.get(url,headers=headers)

#print(html_page.content)

    soup= BeautifulSoup(html_page.content,'lxml')

#below line are for finding title of a perticular website in text formate
    '''title=soup.find('title').get_text()  
    print(title)

    we can use this or insted of this we use
    stock_title = soup.find_all("div",id="compheader")[0].find("h1").get_text()

    print(stock_title)'''


    title_header=soup.find_all("div" ,id="compheader")[0]

    stock_name=title_header.find("span",id="mainContent_ltrlCompName").get_text()

    stock_price=title_header.find("span",class_="Number").get_text()

    '''
    heading=soup.find_all("div",id="companyessentials")[0].find_all("div",class_="col-6 col-md-4 compess")[0].find("small").get_text()

    value=soup.find_all("div",id="companyessentials")[0].find_all("div",class_="col-6 col-md-4 compess")[0].find("span",class_="Number").get_text()
    '''
# now instead of individual value scrap all by applying for loop 
    
    stock.append(stock_name)
    stock.append(stock_price) 

    #print('stock name :',stock_name)
    #print('stock_price :',stock_price)
    
    for i in range(0,3):
        #heading=soup.find_all("div",id="mainContent_updAddRatios")[0].find_all("div",class_="col-6 col-md-4 compess")[i].find("small").get_text()
    
        
        value=soup.find_all("div",id="companyessentials")[0].find_all("div",class_="col-6 col-md-4 compess")[i].find("span",class_="Number").get_text()
        stock.append(value)
        
    for j in range(3,5):
        value=soup.find_all("div",id="mainContent_updAddRatios")[0].find_all("div",class_="col-6 col-md-4 compess")[j].find("p").get_text()
        stock.append(value)
        #print(heading + "    :    " + value)
    
    value=soup.find_all("div",id="mainContent_updAddRatios")[0].find_all("div",class_="col-6 col-md-4 compess")[5].find("p").get_text()
    stock.append(value)

    value=soup.find_all("div",id="mainContent_updAddRatios")[0].find_all("div",class_="col-6 col-md-4 compess")[6].find("p").get_text()
    stock.append(value)

    for k in range(7,10):
        value=soup.find_all("div",id="companyessentials")[0].find_all("div",class_="col-6 col-md-4 compess")[k].find("span",class_="Number").get_text()
        stock.append(value)

    value=soup.find_all("div",id="mainContent_updAddRatios")[0].find_all("div",class_="col-6 col-md-4 compess")[10].find("p").get_text()
    stock.append(value)
    
    for l in range(11,16):
        value=soup.find_all("div",id="companyessentials")[0].find_all("div",class_="col-6 col-md-4 compess")[l].find("span",class_="Number").get_text()
        stock.append(value)


    csv_writer.writerow(stock)        
    time.sleep(5)
csv_file.close()

func_email.send(file_name='scrape.csv')
