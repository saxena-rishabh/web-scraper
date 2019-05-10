# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:24:16 2019

@author: Rishabh
"""


from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# URl to web scrap from.
page_url = "https://droom.in/search?category=&q=baleno"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.

page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# name the output file to write to local disk
out_filename = "Used_Car_Data_By_Rishabh.csv"

# header of csv file to be written
headers = "S.no,Car,Brand,Model,Variant,Fuel Type,Model Year,Mileage,Price,City,Site,Url \n"

# opens file, and writes headers
f = open(out_filename, "w", encoding='utf-8')
f.write(headers)


########## For 1st Website ##############

test1 = page_soup.findAll("div", {"class": "details"})
test2 = page_soup.findAll("h4", {"class": "heading"})
test3 = page_soup.findAll("div", {"class": "price"})
test4 = page_soup.findAll("div", {"class": "info icons"})
sno = 0

for i in range(len(test4)):
    carname = test2[i].a.text.replace("\n", "").strip()
    carnamelist = carname.split()
    t6 = test4[i].div.text.replace("\n", " ").strip().split()
    sno = sno + 1
    name = carname
    brand = carnamelist[0] + " " + carnamelist[1]
    model = carnamelist[2]
    variant = carnamelist[3]
    fuel = t6[0]
    year = carnamelist[-1]
    mileage = t6[2] + " " + t6[3]
    price = test3[i].text.replace("\n", "").strip()[-8:-1]
    city = t6[1]
    site = 'Droom'
    url = str(test2[i].a["href"])
    f.write(str(sno) + ", " + name.replace(",", "") + ", " + brand.replace(",", "")
    + ", " + model.replace(",", "")+ ", " + variant.replace(",", "")
    + ", " + fuel.replace(",", "")+ ", " + year.replace(",", "")
    + ", " + mileage.replace(",", "")+ ", " + price.replace(",", "")
    + ", "  + city.replace(",", "")+ ", " + site.replace(",", "")
    + ", " + url  + "\n")




################# for 2nd Website ###########

# URl to web scrap from.
page_url = "https://www.cartrade.com/buy-used-cars/hyundai/eon/mm"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()


#Assign Website Name
site = 'Cartrade'

test5 = page_soup.findAll("h2", {"class": "h2heading"})
price_container = page_soup.findAll("div", {"class": "cr_prc"})
test6 = page_soup.findAll("div", {"class": "info_cr_new"})
 
for i in range(len(test4)):
    try:
        sno = sno+1
        carname = test5[i].a.text.replace("\r\n", "").strip()
        carnamelist = carname.split()
        name = carname
        brand = carnamelist[0]
        model = carnamelist[1]
        variant = carnamelist[2]  + carnamelist[3]
        price = ''.join(filter(lambda x: x.isdigit(), price_container[i].text))
        test7 = test6[i].text.replace("\n", " ").strip().split()
        mileage = test7[0]+test7[1]
        fuel = test7[3]
        year = test7[8]
        city = test7[9]
        url = "https://www.cartrade.com" + test5[0].a["href"]
        f.write(str(sno) + ", " + name.replace(",", "") + ", " + brand.replace(",", "")
        + ", " + model.replace(",", "")+ ", " + variant.replace(",", "")
        + ", " + fuel.replace(",", "")+ ", " + year.replace(",", "")
        + ", " + mileage.replace(",", "")+ ", " + price.replace(",", "")
        + ", "  + city.replace(",", "")+ ", " + site.replace(",", "")
        + ", " + url  + "\n")
    except:
        print("Error Occured")

f.close()  # Close the file













