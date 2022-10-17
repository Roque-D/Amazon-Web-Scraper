#!/usr/bin/env python
# coding: utf-8

# In[44]:


# import libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import pandas as pd

import smtplib


# In[45]:


# Connect to the Webpage

URL = 'https://www.amazon.com/AmazonBasics-High-Capacity-Rechargeable-Batteries-Pre-charged/dp/B00HZV9WTM/ref=dp_fod_2?pd_rd_w=rTe8O&content-id=amzn1.sym.c84ea9cd-a597-4c46-9e5a-55d1a6e6df1c&pf_rd_p=c84ea9cd-a597-4c46-9e5a-55d1a6e6df1c&pf_rd_r=S4403C5QGDN99GF8HWSA&pd_rd_wg=DcIpC&pd_rd_r=c1e9320c-d281-4bad-976e-1ff9857c7145&pd_rd_i=B00HZV9WTM&psc=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2= BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()
print(title)

price = soup2.find(id='sns-base-price').get_text()
print(price)


# In[46]:


price = price.strip()[1:6]
title = title.strip()

print(title)
print(price)


# In[47]:


today = datetime.date.today()
print(today)


# In[48]:


header = ['Title', 'Price', 'Data']
data = [title, price, today]

with open('AmznWebScraperData.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[49]:


df = pd.read_csv(r'C:\Users\HP\AmznWebScraperData.csv')
print(df)


# In[55]:


def check_price():
    URL = 'https://www.amazon.com/AmazonBasics-High-Capacity-Rechargeable-Batteries-Pre-charged/dp/B00HZV9WTM/ref=dp_fod_2?pd_rd_w=rTe8O&content-id=amzn1.sym.c84ea9cd-a597-4c46-9e5a-55d1a6e6df1c&pf_rd_p=c84ea9cd-a597-4c46-9e5a-55d1a6e6df1c&pf_rd_r=S4403C5QGDN99GF8HWSA&pd_rd_wg=DcIpC&pd_rd_r=c1e9320c-d281-4bad-976e-1ff9857c7145&pd_rd_i=B00HZV9WTM&psc=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2= BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='sns-base-price').get_text()
    
    price = price.strip()[1:6]
    title = title.strip()
    
    today = datetime.date.today()
    
    header = ['Title', 'Price', 'Data']
    
    data = [title, price, today]

    with open('AmznWebScraperData.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


while(True):
    check_price()
    time.sleep(5)


# In[ ]:


df = pd.read_csv(r'C:\Users\HP\AmznWebScraperData.csv')
print(df)


# In[ ]:


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('demonstration@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Hey, This is the moment we have been waiting for. Don't mess it up! Link here: https://www.amazon.com/AmazonBasics-High-Capacity-Rechargeable-Batteries-Pre-charged/dp/B00HZV9WTM/ref=dp_fod_2?pd_rd_w=rTe8O&content-id=amzn1.sym.c84ea9cd-a597-4c46-9e5a-55d1a6e6df1c&pf_rd_p=c84ea9cd-a597-4c46-9e5a-55d1a6e6df1c&pf_rd_r=S4403C5QGDN99GF8HWSA&pd_rd_wg=DcIpC&pd_rd_r=c1e9320c-d281-4bad-976e-1ff9857c7145&pd_rd_i=B00HZV9WTM&psc=1"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'demonstration@gmail.com',
        msg
     
    )

